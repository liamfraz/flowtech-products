#!/usr/bin/env python3
"""Generate Power Automate Beginner's Blueprint PDF."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, ListFlowable, ListItem
)

OUTPUT = os.environ.get("OUTPUT_DIR", ".") + "/power-automate-beginners-blueprint.pdf"
BRAND_BLUE = colors.HexColor("#2F5496")
BRAND_ORANGE = colors.HexColor("#F97316")
LIGHT_BLUE = colors.HexColor("#D6E4F0")
LIGHT_GRAY = colors.HexColor("#F5F5F5")


def get_styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle("CoverTitle", parent=s["Title"], fontSize=32, leading=38,
                          textColor=BRAND_BLUE, alignment=TA_CENTER, spaceAfter=20))
    s.add(ParagraphStyle("CoverSub", parent=s["Normal"], fontSize=14, leading=18,
                          textColor=colors.gray, alignment=TA_CENTER, spaceAfter=12))
    s.add(ParagraphStyle("CoverAuthor", parent=s["Normal"], fontSize=12,
                          textColor=BRAND_ORANGE, alignment=TA_CENTER, spaceBefore=40))
    s.add(ParagraphStyle("ChTitle", parent=s["Heading1"], fontSize=22, leading=26,
                          textColor=BRAND_BLUE, spaceBefore=30, spaceAfter=16))
    s.add(ParagraphStyle("SecHead", parent=s["Heading2"], fontSize=14, leading=18,
                          textColor=BRAND_BLUE, spaceBefore=16, spaceAfter=8))
    s.add(ParagraphStyle("SubHead", parent=s["Heading3"], fontSize=12, leading=15,
                          textColor=BRAND_ORANGE, spaceBefore=12, spaceAfter=6))
    s.add(ParagraphStyle("BodyPara", parent=s["Normal"], fontSize=10, leading=14,
                          alignment=TA_JUSTIFY, spaceAfter=8))
    s.add(ParagraphStyle("BulletItem", parent=s["Normal"], fontSize=10, leading=14,
                          leftIndent=20, spaceAfter=4))
    s.add(ParagraphStyle("CodeBlock", parent=s["Normal"], fontSize=9, leading=12,
                          fontName="Courier", backColor=LIGHT_GRAY, leftIndent=15,
                          rightIndent=15, spaceBefore=8, spaceAfter=8, borderPadding=8))
    s.add(ParagraphStyle("Callout", parent=s["Normal"], fontSize=10, leading=14,
                          backColor=LIGHT_BLUE, borderPadding=10, spaceBefore=10,
                          spaceAfter=10, leftIndent=10, rightIndent=10))
    s.add(ParagraphStyle("TOCEntry", parent=s["Normal"], fontSize=11, leading=16,
                          leftIndent=20, spaceAfter=4))
    s.add(ParagraphStyle("Exercise", parent=s["Normal"], fontSize=10, leading=14,
                          backColor=colors.HexColor("#FFF3CD"), borderPadding=10,
                          spaceBefore=10, spaceAfter=10, leftIndent=10, rightIndent=10))
    s.add(ParagraphStyle("Summary", parent=s["Normal"], fontSize=10, leading=14,
                          backColor=colors.HexColor("#D4EDDA"), borderPadding=10,
                          spaceBefore=10, spaceAfter=10, leftIndent=10, rightIndent=10))
    return s


def add_header_footer(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.gray)
        canvas.drawString(2 * cm, 1.2 * cm, "Power Automate Beginner's Blueprint | Flowtech Advisory")
        canvas.drawRightString(A4[0] - 2 * cm, 1.2 * cm, f"Page {doc.page}")
        canvas.setStrokeColor(BRAND_ORANGE)
        canvas.setLineWidth(0.5)
        canvas.line(2 * cm, 1.5 * cm, A4[0] - 2 * cm, 1.5 * cm)
    canvas.restoreState()


def bullets(items, st):
    return ListFlowable(
        [ListItem(Paragraph(i, st["BulletItem"])) for i in items],
        bulletType="bullet", start="circle", leftIndent=10
    )


def make_table(data, widths):
    t = Table(data, colWidths=widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BRAND_BLUE),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.gray),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GRAY]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


def cover(st):
    e = [Spacer(1, 5 * cm)]
    e.append(Paragraph("Power Automate<br/>Beginner's Blueprint", st["CoverTitle"]))
    e.append(Spacer(1, 1 * cm))
    e.append(Paragraph("From Zero to Automated<br/>Master Power Automate in 8 Modules", st["CoverSub"]))
    e.append(Spacer(1, 2 * cm))
    e.append(Paragraph("Liam Frazer", st["CoverAuthor"]))
    e.append(Paragraph("Flowtech Advisory", st["CoverSub"]))
    e.append(Spacer(1, 3 * cm))
    e.append(Paragraph("Version 1.0 | 2026", st["CoverSub"]))
    e.append(PageBreak())
    return e


def toc(st):
    e = [Paragraph("Table of Contents", st["ChTitle"]), Spacer(1, 0.5 * cm)]
    modules = [
        ("Module 1: What is Power Automate?", "Overview, licensing, ecosystem"),
        ("Module 2: Your First Flow", "Button trigger, send email, test it"),
        ("Module 3: Triggers & Actions Deep Dive", "Trigger types, action types, dynamic content"),
        ("Module 4: Connectors", "SharePoint, Outlook, Teams, Excel, HTTP"),
        ("Module 5: Working with Data", "Expressions, variables, arrays, parse JSON"),
        ("Module 6: Conditions & Loops", "Conditions, switch, apply to each, do until"),
        ("Module 7: Error Handling", "Scope, configure run after, try-catch pattern"),
        ("Module 8: Going to Production", "Solutions, environment variables, ALM"),
    ]
    for title, desc in modules:
        e.append(Paragraph(f"<b>{title}</b> — {desc}", st["TOCEntry"]))
    e.append(PageBreak())
    return e


def module1(st):
    e = [Paragraph("Module 1: What is Power Automate?", st["ChTitle"])]
    e.append(Paragraph(
        "<b>Learning Objectives:</b> Understand what Power Automate is, how it fits into the "
        "Microsoft ecosystem, what licensing is needed, and when to use it vs alternatives.",
        st["Callout"]
    ))
    e.append(Paragraph("Overview", st["SecHead"]))
    e.append(Paragraph(
        "Power Automate (formerly Microsoft Flow) is a cloud-based service that lets you create "
        "automated workflows between apps and services. It connects to over 1,000 data sources "
        "and services via pre-built connectors — no code required.",
        st["BodyPara"]
    ))
    e.append(Paragraph(
        "Think of it as the glue between your business applications. When something happens in "
        "one system (a trigger), Power Automate can automatically do things in other systems (actions). "
        "For example: when a new email arrives with an attachment, save it to SharePoint and notify "
        "your team in Teams.",
        st["BodyPara"]
    ))
    e.append(Paragraph("Flow Types", st["SecHead"]))
    flow_data = [
        ["Type", "Trigger", "Best For"],
        ["Cloud flow - Automated", "Event-based (email arrives, item created)", "Business process automation"],
        ["Cloud flow - Instant", "Button press (manual)", "On-demand tasks, reports"],
        ["Cloud flow - Scheduled", "Time-based (daily, weekly)", "Regular maintenance, reminders"],
        ["Desktop flow", "UI automation (RPA)", "Legacy app automation"],
        ["Business process flow", "Guided stages", "Multi-stage processes (e.g., sales pipeline)"],
    ]
    e.append(make_table(flow_data, [3.5 * cm, 4 * cm, 6 * cm]))
    e.append(Spacer(1, 0.5 * cm))
    e.append(Paragraph("Licensing", st["SecHead"]))
    e.append(Paragraph(
        "Power Automate offers several licensing tiers. Understanding which you need is critical "
        "before building production flows.",
        st["BodyPara"]
    ))
    lic_data = [
        ["Plan", "Price (AUD/mo)", "Includes"],
        ["Microsoft 365 (included)", "$0 extra", "Standard connectors, 6,000 runs/day"],
        ["Power Automate Premium", "~$22/user", "Premium connectors, 40,000 runs/day, AI Builder, RPA"],
        ["Power Automate Process", "~$220/flow", "Per-flow, unattended RPA, premium connectors"],
    ]
    e.append(make_table(lic_data, [4 * cm, 3.5 * cm, 6 * cm]))
    e.append(Spacer(1, 0.3 * cm))
    e.append(Paragraph(
        "<b>Key insight:</b> Most M365 users already have a basic Power Automate license included. "
        "You only need Premium for connectors like HTTP, custom connectors, or AI Builder.",
        st["Callout"]
    ))
    e.append(Paragraph("When to Use Power Automate", st["SecHead"]))
    e.append(bullets([
        "<b>Use it when:</b> Connecting Microsoft 365 services, approval workflows, notifications, "
        "data sync between systems, scheduled reporting",
        "<b>Consider alternatives when:</b> Complex data transformations (use Power Query), "
        "real-time event processing (use Azure Functions), heavy compute workloads (use Azure Logic Apps)",
    ], st))
    e.append(Paragraph(
        "<b>Module 1 Summary:</b> Power Automate is Microsoft's workflow automation platform. "
        "It connects 1,000+ services via connectors, requires minimal coding, and is included "
        "with most M365 licenses for standard use cases.",
        st["Summary"]
    ))
    e.append(PageBreak())
    return e


def module2(st):
    e = [Paragraph("Module 2: Your First Flow", st["ChTitle"])]
    e.append(Paragraph(
        "<b>Learning Objectives:</b> Create a working flow from scratch, understand the "
        "trigger-action model, test your flow, and read the run history.",
        st["Callout"]
    ))
    e.append(Paragraph("Building a Button-Triggered Email Flow", st["SecHead"]))
    e.append(Paragraph(
        "Let's build the simplest possible flow: press a button, send an email. This teaches "
        "the fundamental concepts without any complexity.",
        st["BodyPara"]
    ))
    e.append(Paragraph("Step 1: Create the Flow", st["SubHead"]))
    e.append(bullets([
        "Go to <b>make.powerautomate.com</b>",
        "Click <b>+ Create</b> in the left navigation",
        "Select <b>Instant cloud flow</b>",
        "Name it: 'My First Flow - Button Email'",
        "Select trigger: <b>Manually trigger a flow</b>",
        "Click <b>Create</b>",
    ], st))
    e.append(Paragraph("Step 2: Add an Input to the Button", st["SubHead"]))
    e.append(Paragraph(
        "Click the trigger step and select <b>+ Add an input</b>. Choose <b>Text</b> and "
        "label it 'Your Message'. This creates an input field that appears when you press the button.",
        st["BodyPara"]
    ))
    e.append(Paragraph("Step 3: Add the Send Email Action", st["SubHead"]))
    e.append(bullets([
        "Click <b>+ New step</b>",
        "Search for <b>Send an email (V2)</b> from Office 365 Outlook",
        "To: your own email address",
        "Subject: 'Test from Power Automate'",
        "Body: Click in the body field, then select <b>Your Message</b> from Dynamic content",
    ], st))
    e.append(Paragraph("Step 4: Test It", st["SubHead"]))
    e.append(Paragraph(
        "Click <b>Test</b> in the top-right corner. Select <b>Manually</b> and click <b>Test</b>. "
        "Enter a message and click <b>Run flow</b>. Check your email — you should receive it "
        "within seconds.",
        st["BodyPara"]
    ))
    e.append(Paragraph("Understanding Run History", st["SecHead"]))
    e.append(Paragraph(
        "After running the flow, you can see the results in the run history. Each step shows "
        "a green checkmark (success) or red X (failure). Click any step to see its inputs "
        "and outputs — this is your primary debugging tool.",
        st["BodyPara"]
    ))
    e.append(Paragraph(
        "<b>Try It Yourself:</b> Modify the flow to also post a message to a Teams channel "
        "when the button is pressed. Hint: Add a 'Post message in a chat or channel' action "
        "from the Teams connector.",
        st["Exercise"]
    ))
    e.append(Paragraph(
        "<b>Module 2 Summary:</b> Every flow has a trigger and one or more actions. The button "
        "trigger is the simplest way to start. Dynamic content lets you pass data between steps. "
        "Run history shows you exactly what happened in each run.",
        st["Summary"]
    ))
    e.append(PageBreak())
    return e


def module3(st):
    e = [Paragraph("Module 3: Triggers & Actions Deep Dive", st["ChTitle"])]
    e.append(Paragraph(
        "<b>Learning Objectives:</b> Understand trigger types (polling vs webhook), action "
        "categories, dynamic content, and how data flows between steps.",
        st["Callout"]
    ))
    e.append(Paragraph("Trigger Types", st["SecHead"]))
    trig_data = [
        ["Type", "How It Works", "Example"],
        ["Polling", "Checks for changes on a schedule (every 1-5 min)", "SharePoint 'When an item is created'"],
        ["Webhook", "Service notifies Power Automate immediately", "HTTP webhook trigger"],
        ["Recurrence", "Runs on a fixed schedule", "Every Monday at 9am"],
        ["Manual", "User presses a button", "Instant cloud flow button"],
        ["PowerApps", "Called from a PowerApp", "PowerApps trigger (V2)"],
    ]
    e.append(make_table(trig_data, [2.5 * cm, 5 * cm, 6 * cm]))
    e.append(Spacer(1, 0.3 * cm))
    e.append(Paragraph(
        "<b>Polling vs Webhook:</b> Polling triggers check periodically and may have a delay "
        "of up to 5 minutes. Webhook triggers fire instantly but aren't available for all connectors. "
        "SharePoint and Outlook use polling; HTTP and Dataverse support webhooks.",
        st["Callout"]
    ))
    e.append(Paragraph("Action Categories", st["SecHead"]))
    e.append(bullets([
        "<b>Standard actions:</b> Office 365, SharePoint, OneDrive, Outlook, Teams — included with M365",
        "<b>Premium actions:</b> HTTP, SQL Server, Dataverse, AI Builder — require Premium license",
        "<b>Custom connectors:</b> Connect to any REST API — require Premium license",
        "<b>Built-in actions:</b> Compose, Variable, Condition, Loop, Delay — always free",
    ], st))
    e.append(Paragraph("Dynamic Content", st["SecHead"]))
    e.append(Paragraph(
        "Dynamic content is how you pass data between steps. When you click in an input field, "
        "Power Automate shows you all the data available from previous steps. This includes "
        "trigger outputs and the outputs of every action that ran before.",
        st["BodyPara"]
    ))
    e.append(Paragraph(
        "// Behind the scenes, dynamic content is an expression:<br/>"
        "triggerBody()?['field_name']    // Data from the trigger<br/>"
        "body('Action_Name')?['field']   // Data from a previous action<br/>"
        "outputs('Compose_Step')         // Output of a Compose action",
        st["CodeBlock"]
    ))
    e.append(Paragraph(
        "<b>Try It Yourself:</b> Create a flow triggered by a new email. Add a Compose action "
        "that outputs the sender's name, subject, and received date using dynamic content. "
        "Then add a 'Create item' action in SharePoint to log the email details.",
        st["Exercise"]
    ))
    e.append(Paragraph(
        "<b>Module 3 Summary:</b> Triggers start flows (polling, webhook, scheduled, manual). "
        "Actions perform work. Dynamic content passes data between steps using expressions. "
        "Understanding this data flow is fundamental to building reliable flows.",
        st["Summary"]
    ))
    e.append(PageBreak())
    return e


def module4(st):
    e = [Paragraph("Module 4: Connectors", st["ChTitle"])]
    e.append(Paragraph(
        "<b>Learning Objectives:</b> Master the top 6 connectors used in business automation — "
        "SharePoint, Outlook, Teams, Excel, HTTP, and custom connectors.",
        st["Callout"]
    ))
    e.append(Paragraph("SharePoint Connector", st["SecHead"]))
    e.append(Paragraph(
        "SharePoint is the most commonly used connector. Key actions:",
        st["BodyPara"]
    ))
    sp_data = [
        ["Action", "Use Case", "Key Notes"],
        ["Get items", "Read list data with filters", "Max 5,000 items; use $top and $filter OData"],
        ["Create item", "Add new list item", "Map columns to dynamic content"],
        ["Update item", "Modify existing item", "Requires item ID"],
        ["Get file content", "Download a file", "Returns binary; use with other actions"],
        ["Create file", "Upload a file", "Specify folder path and file name"],
    ]
    e.append(make_table(sp_data, [3.5 * cm, 4 * cm, 6 * cm]))
    e.append(Spacer(1, 0.3 * cm))
    e.append(Paragraph("Outlook Connector", st["SecHead"]))
    e.append(Paragraph(
        "The Office 365 Outlook connector handles email operations. The 'When a new email arrives' "
        "trigger is extremely popular. Important settings: SubjectFilter, IncludeAttachments, "
        "Importance filter, and FolderPath.",
        st["BodyPara"]
    ))
    e.append(Paragraph("Teams Connector", st["SecHead"]))
    e.append(Paragraph(
        "Use Teams for notifications, approvals, and Adaptive Cards. Key actions include "
        "'Post message in a chat or channel', 'Post Adaptive Card', and 'Create a chat'. "
        "Adaptive Cards provide rich, interactive messages with buttons and forms.",
        st["BodyPara"]
    ))
    e.append(Paragraph("Excel Online Connector", st["SecHead"]))
    e.append(Paragraph(
        "The Excel connector works with Excel files stored in SharePoint or OneDrive. "
        "Data must be in a formatted Table (not just a range). Key actions: 'List rows present "
        "in a table', 'Add a row into a table', 'Update a row'. For complex operations, "
        "use the Office Scripts connector (Run Script action).",
        st["BodyPara"]
    ))
    e.append(Paragraph("HTTP Connector (Premium)", st["SecHead"]))
    e.append(Paragraph(
        "The HTTP connector lets you call any REST API. This is the most powerful connector "
        "but requires a Premium license. Use it for: calling Graph API directly, integrating "
        "with third-party APIs, webhooks, and custom API endpoints.",
        st["BodyPara"]
    ))
    e.append(Paragraph(
        "// Example: Call Microsoft Graph API to get user's manager<br/>"
        "Method: GET<br/>"
        "URI: https://graph.microsoft.com/v1.0/users/{userId}/manager<br/>"
        "Headers: Authorization: Bearer @{body('Get_Token')?['access_token']}",
        st["CodeBlock"]
    ))
    e.append(Paragraph(
        "<b>Try It Yourself:</b> Create a flow that monitors a SharePoint list for new items. "
        "When an item is created, send a summary email via Outlook AND post a message to a "
        "Teams channel. Use dynamic content to include the item's title and created date.",
        st["Exercise"]
    ))
    e.append(Paragraph(
        "<b>Module 4 Summary:</b> Connectors are the building blocks. SharePoint for data, "
        "Outlook for email, Teams for notifications, Excel for reporting, HTTP for everything else. "
        "Master these 5 and you can automate 90% of business processes.",
        st["Summary"]
    ))
    e.append(PageBreak())
    return e


def module5(st):
    e = [Paragraph("Module 5: Working with Data", st["ChTitle"])]
    e.append(Paragraph(
        "<b>Learning Objectives:</b> Write expressions, use variables, manipulate arrays, "
        "and parse JSON responses.",
        st["Callout"]
    ))
    e.append(Paragraph("Expressions", st["SecHead"]))
    e.append(Paragraph(
        "Expressions are the programming language of Power Automate. They follow the "
        "Workflow Definition Language (WDL) syntax. You access them via the 'Expression' "
        "tab in the dynamic content panel.",
        st["BodyPara"]
    ))
    expr_data = [
        ["Category", "Examples"],
        ["String", "concat(), substring(), replace(), split(), toLower(), toUpper(), trim()"],
        ["Date/Time", "utcNow(), addDays(), formatDateTime(), ticks(), startOfDay()"],
        ["Math", "add(), sub(), mul(), div(), mod(), min(), max(), rand()"],
        ["Logical", "if(), equals(), and(), or(), not(), greater(), less()"],
        ["Collection", "length(), first(), last(), contains(), join(), union(), intersection()"],
        ["Conversion", "int(), float(), string(), bool(), json(), xml(), base64()"],
    ]
    e.append(make_table(expr_data, [3 * cm, 11 * cm]))
    e.append(Spacer(1, 0.3 * cm))
    e.append(Paragraph("Variables", st["SecHead"]))
    e.append(Paragraph(
        "Variables store data that changes during flow execution. Always initialize them at "
        "the top level of your flow (not inside conditions or loops).",
        st["BodyPara"]
    ))
    e.append(bullets([
        "<b>Initialize variable:</b> Declare type and optional default value",
        "<b>Set variable:</b> Overwrite the entire value",
        "<b>Append to string variable:</b> Add text to existing string",
        "<b>Append to array variable:</b> Add item to existing array",
        "<b>Increment variable:</b> Add a number to an integer variable",
    ], st))
    e.append(Paragraph("Parse JSON", st["SecHead"]))
    e.append(Paragraph(
        "When working with HTTP responses or complex data, you'll need Parse JSON to make "
        "fields available as dynamic content. The key is providing the correct schema.",
        st["BodyPara"]
    ))
    e.append(Paragraph(
        "Tip: Run the flow once, copy the output from the preceding action, then use "
        "'Generate from sample' in the Parse JSON schema editor. This auto-creates the schema.",
        st["BodyPara"]
    ))
    e.append(Paragraph(
        "// Example schema for a simple API response<br/>"
        "{<br/>"
        '&nbsp;&nbsp;"type": "object",<br/>'
        '&nbsp;&nbsp;"properties": {<br/>'
        '&nbsp;&nbsp;&nbsp;&nbsp;"name": { "type": "string" },<br/>'
        '&nbsp;&nbsp;&nbsp;&nbsp;"email": { "type": "string" },<br/>'
        '&nbsp;&nbsp;&nbsp;&nbsp;"amount": { "type": "number" }<br/>'
        "&nbsp;&nbsp;}<br/>}",
        st["CodeBlock"]
    ))
    e.append(Paragraph(
        "<b>Try It Yourself:</b> Create a flow with a Compose action that outputs a JSON object "
        "with 3 fields. Add a Parse JSON action. Then use the parsed fields in a Send Email action. "
        "Bonus: Initialize a string variable and build it up using Append actions in a loop.",
        st["Exercise"]
    ))
    e.append(Paragraph(
        "<b>Module 5 Summary:</b> Expressions transform data (strings, dates, math, logic). "
        "Variables store changing state. Parse JSON makes API responses usable. These three "
        "skills unlock complex automation scenarios.",
        st["Summary"]
    ))
    e.append(PageBreak())
    return e


def module6(st):
    e = [Paragraph("Module 6: Conditions & Loops", st["ChTitle"])]
    e.append(Paragraph(
        "<b>Learning Objectives:</b> Implement branching logic with Conditions and Switch, "
        "iterate with Apply to Each and Do Until loops.",
        st["Callout"]
    ))
    e.append(Paragraph("Conditions (If/Else)", st["SecHead"]))
    e.append(Paragraph(
        "The Condition action splits your flow into two branches: 'If yes' and 'If no'. "
        "You can use simple comparisons or advanced expressions.",
        st["BodyPara"]
    ))
    e.append(Paragraph(
        "// Simple: Is the amount greater than 500?<br/>"
        "triggerBody()?['Amount'] is greater than 500<br/><br/>"
        "// Advanced: Multiple conditions with AND/OR<br/>"
        "@and(greater(triggerBody()?['Amount'],500),equals(triggerBody()?['Category'],'Meals'))",
        st["CodeBlock"]
    ))
    e.append(Paragraph("Switch (Multiple Branches)", st["SecHead"]))
    e.append(Paragraph(
        "Use Switch when you have more than 2 possible outcomes. It evaluates an expression "
        "and routes to the matching case. Always include a Default case.",
        st["BodyPara"]
    ))
    e.append(Paragraph(
        "Switch on: triggerBody()?['Priority']<br/>"
        "Case 'High': Send to director + Teams alert<br/>"
        "Case 'Medium': Send to manager<br/>"
        "Case 'Low': Log to SharePoint only<br/>"
        "Default: Send to admin for review",
        st["CodeBlock"]
    ))
    e.append(Paragraph("Apply to Each (For Loop)", st["SecHead"]))
    e.append(Paragraph(
        "Apply to Each iterates over an array. It's automatically added when you use dynamic "
        "content from an action that returns multiple items (like 'Get items' from SharePoint).",
        st["BodyPara"]
    ))
    e.append(bullets([
        "By default, iterations run in parallel (up to 20 concurrent)",
        "To run sequentially: Settings > Concurrency Control > On > Degree of Parallelism: 1",
        "Access the current item with: items('Apply_to_each')?['field_name']",
        "Avoid putting heavy actions inside loops — consider batching instead",
    ], st))
    e.append(Paragraph("Do Until (While Loop)", st["SecHead"]))
    e.append(Paragraph(
        "Do Until repeats actions until a condition is met OR a limit is reached. "
        "Always set a count limit and timeout to prevent infinite loops.",
        st["BodyPara"]
    ))
    e.append(Paragraph(
        "// Example: Retry an HTTP call until success or 5 attempts<br/>"
        "Do Until: variables('RetryCount') >= 5 OR variables('Success') = true<br/>"
        "&nbsp;&nbsp;> HTTP action<br/>"
        "&nbsp;&nbsp;> Set Success = (statusCode == 200)<br/>"
        "&nbsp;&nbsp;> Increment RetryCount<br/>"
        "&nbsp;&nbsp;> Delay 10 seconds",
        st["CodeBlock"]
    ))
    e.append(Paragraph(
        "<b>Try It Yourself:</b> Create a flow that gets all items from a SharePoint list. "
        "Use Apply to Each to check each item's 'Status' field. If Status = 'Overdue', "
        "send an email to the assigned person. Use a variable to count how many emails were sent. "
        "After the loop, post the total count to Teams.",
        st["Exercise"]
    ))
    e.append(Paragraph(
        "<b>Module 6 Summary:</b> Conditions branch on true/false. Switch handles multiple "
        "outcomes. Apply to Each iterates arrays. Do Until retries or waits. Combine these "
        "for sophisticated business logic.",
        st["Summary"]
    ))
    e.append(PageBreak())
    return e


def module7(st):
    e = [Paragraph("Module 7: Error Handling", st["ChTitle"])]
    e.append(Paragraph(
        "<b>Learning Objectives:</b> Implement the try-catch pattern with Scope blocks, "
        "use Configure Run After, set up error alerts, and build resilient flows.",
        st["Callout"]
    ))
    e.append(Paragraph("The Problem with No Error Handling", st["SecHead"]))
    e.append(Paragraph(
        "Without error handling, a flow fails silently. The flow owner gets a notification "
        "email (if enabled), but the business process stops. Data may be partially processed, "
        "leaving systems in an inconsistent state. Production flows MUST have error handling.",
        st["BodyPara"]
    ))
    e.append(Paragraph("Scope Blocks = Try/Catch", st["SecHead"]))
    e.append(Paragraph(
        "Power Automate doesn't have native try/catch, but you can build it with Scope blocks:",
        st["BodyPara"]
    ))
    e.append(bullets([
        "<b>Scope 'Try':</b> Contains all your main business logic actions",
        "<b>Scope 'Catch':</b> Contains error notification/recovery actions",
        "Set the Catch scope's <b>Configure Run After</b> to: 'has failed' and 'has timed out'",
        "The Catch scope runs ONLY when the Try scope fails",
    ], st))
    e.append(Paragraph("Configure Run After", st["SecHead"]))
    e.append(Paragraph(
        "Every action has a 'Configure Run After' setting (click the ... menu > Configure run after). "
        "Options are:",
        st["BodyPara"]
    ))
    conf_data = [
        ["Setting", "When It Runs", "Use Case"],
        ["is successful", "Previous action succeeded", "Normal flow (default)"],
        ["has failed", "Previous action failed", "Error handling"],
        ["is skipped", "Previous action was skipped", "Alternative path"],
        ["has timed out", "Previous action timed out", "Timeout recovery"],
    ]
    e.append(make_table(conf_data, [3 * cm, 4.5 * cm, 6 * cm]))
    e.append(Spacer(1, 0.3 * cm))
    e.append(Paragraph("Getting Error Details", st["SecHead"]))
    e.append(Paragraph(
        "Inside your Catch scope, use the result() function to get error details:<br/><br/>"
        "result('Try_Scope')?[0]?['error']?['message']<br/><br/>"
        "Or use actions('Failed_Action')?['error'] to get specific action errors.",
        st["CodeBlock"]
    ))
    e.append(Paragraph("Best Practices", st["SecHead"]))
    e.append(bullets([
        "Every production flow should have a Try/Catch pattern",
        "Send error alerts to a Teams channel or email (not just the flow owner notification)",
        "Include the flow name, run ID, and error message in alerts",
        "Log errors to a SharePoint list for trend analysis",
        "Set reasonable timeouts on HTTP actions (default is 30 days!)",
        "Use Terminate action in Catch to set the flow run status to Failed",
    ], st))
    e.append(Paragraph(
        "<b>Try It Yourself:</b> Take your flow from Module 6 and wrap all the logic in a "
        "Try scope. Add a Catch scope that sends you a Teams message with the error details. "
        "Test it by intentionally misconfiguring a SharePoint list name.",
        st["Exercise"]
    ))
    e.append(Paragraph(
        "<b>Module 7 Summary:</b> Use Scope blocks for try/catch. Configure Run After controls "
        "when actions execute. Always add error handling to production flows. Log errors and "
        "send proactive alerts. The result() function gives you error details.",
        st["Summary"]
    ))
    e.append(PageBreak())
    return e


def module8(st):
    e = [Paragraph("Module 8: Going to Production", st["ChTitle"])]
    e.append(Paragraph(
        "<b>Learning Objectives:</b> Package flows in Solutions, use environment variables, "
        "implement ALM (Application Lifecycle Management), and follow best practices.",
        st["Callout"]
    ))
    e.append(Paragraph("Solutions", st["SecHead"]))
    e.append(Paragraph(
        "A Solution is a container that packages your flows (and other Power Platform components) "
        "for deployment. Think of it like a deployment package. Benefits:",
        st["BodyPara"]
    ))
    e.append(bullets([
        "Move flows between environments (Dev > Test > Production)",
        "Version control your flows",
        "Manage dependencies between components",
        "Export/import as managed or unmanaged solutions",
    ], st))
    e.append(Paragraph("Environment Variables", st["SecHead"]))
    e.append(Paragraph(
        "Never hardcode environment-specific values (site URLs, email addresses, list IDs) "
        "in your flows. Use Environment Variables instead:",
        st["BodyPara"]
    ))
    e.append(bullets([
        "Create environment variables in your Solution",
        "Reference them in flows using the Environment Variable dynamic content",
        "Set different values in each environment (Dev, Test, Prod)",
        "Supported types: String, Number, Boolean, JSON, Data Source",
    ], st))
    e.append(Paragraph("Connection References", st["SecHead"]))
    e.append(Paragraph(
        "Connection References decouple your flow from specific user connections. When you "
        "import a solution, you map connection references to connections in the target environment. "
        "This means the flow doesn't break when the original creator's account changes.",
        st["BodyPara"]
    ))
    e.append(Paragraph("ALM Workflow", st["SecHead"]))
    alm_data = [
        ["Step", "Environment", "Action"],
        ["1. Develop", "Dev", "Build and test flows in personal dev environment"],
        ["2. Export", "Dev", "Export solution as unmanaged (for further editing) or managed"],
        ["3. Test", "Test/UAT", "Import solution, run test scenarios, validate"],
        ["4. Deploy", "Production", "Import managed solution with force-overwrite"],
        ["5. Monitor", "Production", "Track flow runs, error rates, performance"],
    ]
    e.append(make_table(alm_data, [2.5 * cm, 3.5 * cm, 8 * cm]))
    e.append(Spacer(1, 0.3 * cm))
    e.append(Paragraph("Production Best Practices", st["SecHead"]))
    e.append(bullets([
        "<b>Naming convention:</b> Use prefixes like 'PROD-' or 'FlowTech-' for easy identification",
        "<b>Documentation:</b> Add descriptions to every action explaining what it does and why",
        "<b>Error handling:</b> Every flow must have try/catch (Module 7)",
        "<b>Testing:</b> Create a test plan with edge cases before deployment",
        "<b>Monitoring:</b> Set up a daily monitoring flow that checks for failed runs",
        "<b>Backup:</b> Export your solution weekly as a backup",
        "<b>Ownership:</b> Use service accounts as flow owners, not personal accounts",
        "<b>Performance:</b> Minimize API calls, use parallel branches, avoid unnecessary loops",
    ], st))
    e.append(Paragraph(
        "<b>Try It Yourself:</b> Create a new Solution. Add your flow from the previous modules "
        "to the solution. Create environment variables for the SharePoint site URL and notification "
        "email. Export the solution and import it into a test environment.",
        st["Exercise"]
    ))
    e.append(Paragraph(
        "<b>Module 8 Summary:</b> Solutions package flows for deployment. Environment variables "
        "separate configuration from logic. Connection references make flows portable. Follow ALM "
        "practices: develop, test, deploy, monitor. Use service accounts in production.",
        st["Summary"]
    ))
    e.append(Spacer(1, 2 * cm))
    e.append(Paragraph("Congratulations!", st["ChTitle"]))
    e.append(Paragraph(
        "You've completed the Power Automate Beginner's Blueprint. You now have the knowledge "
        "to build, test, and deploy production-ready automated workflows. The key to mastery is "
        "practice — start with simple flows and gradually increase complexity.",
        st["BodyPara"]
    ))
    e.append(Spacer(1, 1 * cm))
    e.append(Paragraph(
        "For advanced topics, custom consulting, or hands-on workshops, visit "
        "flowtechadvisory.com or email support@flowtechadvisory.com.",
        st["CoverSub"]
    ))
    return e


def main():
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    doc = SimpleDocTemplate(OUTPUT, pagesize=A4,
                            leftMargin=2 * cm, rightMargin=2 * cm,
                            topMargin=2.5 * cm, bottomMargin=2.5 * cm)
    st = get_styles()
    elems = []
    elems.extend(cover(st))
    elems.extend(toc(st))
    elems.extend(module1(st))
    elems.extend(module2(st))
    elems.extend(module3(st))
    elems.extend(module4(st))
    elems.extend(module5(st))
    elems.extend(module6(st))
    elems.extend(module7(st))
    elems.extend(module8(st))
    doc.build(elems, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f"Created: {OUTPUT}")


if __name__ == "__main__":
    main()
