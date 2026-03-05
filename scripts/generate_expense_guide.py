#!/usr/bin/env python3
"""Generate Expense Claim Automation Guide PDF."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, ListFlowable, ListItem, KeepTogether
)

OUTPUT = os.environ.get("OUTPUT_DIR", ".") + "/expense-claim-automation-guide.pdf"
BRAND_BLUE = colors.HexColor("#2F5496")
BRAND_ORANGE = colors.HexColor("#F97316")
LIGHT_BLUE = colors.HexColor("#D6E4F0")
LIGHT_GRAY = colors.HexColor("#F5F5F5")
CODE_BG = colors.HexColor("#1E1E1E")


def get_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        "CoverTitle", parent=styles["Title"], fontSize=32, leading=38,
        textColor=BRAND_BLUE, alignment=TA_CENTER, spaceAfter=20
    ))
    styles.add(ParagraphStyle(
        "CoverSubtitle", parent=styles["Normal"], fontSize=14, leading=18,
        textColor=colors.gray, alignment=TA_CENTER, spaceAfter=12
    ))
    styles.add(ParagraphStyle(
        "CoverAuthor", parent=styles["Normal"], fontSize=12,
        textColor=BRAND_ORANGE, alignment=TA_CENTER, spaceBefore=40
    ))
    styles.add(ParagraphStyle(
        "ChapterTitle", parent=styles["Heading1"], fontSize=22, leading=26,
        textColor=BRAND_BLUE, spaceBefore=30, spaceAfter=16,
        borderWidth=2, borderColor=BRAND_ORANGE, borderPadding=8
    ))
    styles.add(ParagraphStyle(
        "SectionHeading", parent=styles["Heading2"], fontSize=14, leading=18,
        textColor=BRAND_BLUE, spaceBefore=16, spaceAfter=8
    ))
    styles.add(ParagraphStyle(
        "BodyText2", parent=styles["Normal"], fontSize=10, leading=14,
        alignment=TA_JUSTIFY, spaceAfter=8
    ))
    styles.add(ParagraphStyle(
        "BulletText", parent=styles["Normal"], fontSize=10, leading=14,
        leftIndent=20, spaceAfter=4
    ))
    styles.add(ParagraphStyle(
        "CodeBlock", parent=styles["Normal"], fontSize=9, leading=12,
        fontName="Courier", backColor=LIGHT_GRAY, leftIndent=15,
        rightIndent=15, spaceBefore=8, spaceAfter=8, borderPadding=8
    ))
    styles.add(ParagraphStyle(
        "TOCEntry", parent=styles["Normal"], fontSize=11, leading=16,
        leftIndent=20, spaceAfter=4
    ))
    styles.add(ParagraphStyle(
        "FooterStyle", parent=styles["Normal"], fontSize=8,
        textColor=colors.gray, alignment=TA_CENTER
    ))
    styles.add(ParagraphStyle(
        "Callout", parent=styles["Normal"], fontSize=10, leading=14,
        backColor=LIGHT_BLUE, borderPadding=10, spaceBefore=10, spaceAfter=10,
        leftIndent=10, rightIndent=10
    ))
    return styles


def add_header_footer(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.gray)
        canvas.drawString(2 * cm, 1.2 * cm, "Expense Claim Automation Guide | Flowtech Advisory")
        canvas.drawRightString(A4[0] - 2 * cm, 1.2 * cm, f"Page {doc.page}")
        canvas.setStrokeColor(BRAND_ORANGE)
        canvas.setLineWidth(0.5)
        canvas.line(2 * cm, 1.5 * cm, A4[0] - 2 * cm, 1.5 * cm)
    canvas.restoreState()


def build_cover(styles):
    elements = []
    elements.append(Spacer(1, 6 * cm))
    elements.append(Paragraph("Expense Claim<br/>Automation Guide", styles["CoverTitle"]))
    elements.append(Spacer(1, 1 * cm))
    elements.append(Paragraph(
        "A Step-by-Step Guide to Automating Expense Claims<br/>"
        "with Power Automate &amp; AI Builder", styles["CoverSubtitle"]
    ))
    elements.append(Spacer(1, 2 * cm))
    elements.append(Paragraph("Liam Frazer", styles["CoverAuthor"]))
    elements.append(Paragraph("Flowtech Advisory", styles["CoverSubtitle"]))
    elements.append(Spacer(1, 3 * cm))
    elements.append(Paragraph("Version 1.0 | 2026", styles["CoverSubtitle"]))
    elements.append(PageBreak())
    return elements


def build_toc(styles):
    elements = []
    elements.append(Paragraph("Table of Contents", styles["ChapterTitle"]))
    elements.append(Spacer(1, 0.5 * cm))
    chapters = [
        ("Chapter 1: The Problem", "Manual Expense Processing Pain Points"),
        ("Chapter 2: Solution Architecture", "Components Overview & System Design"),
        ("Chapter 3: Setting Up AI Builder", "Model Training & Receipt Parsing"),
        ("Chapter 4: Building the Flow", "Step-by-Step Flow Construction"),
        ("Chapter 5: Excel Integration", "Office Scripts & Data Formatting"),
        ("Chapter 6: Testing & Deployment", "Test Scenarios & Go-Live Steps"),
        ("Chapter 7: Maintenance & Monitoring", "Error Alerts & Flow Analytics"),
        ("Chapter 8: Appendix", "Expression Reference & Troubleshooting"),
    ]
    for title, desc in chapters:
        elements.append(Paragraph(f"<b>{title}</b> — {desc}", styles["TOCEntry"]))
    elements.append(PageBreak())
    return elements


def bullet_list(items, styles):
    return ListFlowable(
        [ListItem(Paragraph(item, styles["BulletText"])) for item in items],
        bulletType="bullet", start="circle", leftIndent=10
    )


def build_chapter1(styles):
    elements = []
    elements.append(Paragraph("Chapter 1: The Problem", styles["ChapterTitle"]))
    elements.append(Paragraph(
        "Construction companies process hundreds of expense claims monthly. From site managers "
        "buying materials at Bunnings to project engineers expensing client lunches, the volume "
        "of paper receipts and manual data entry creates a significant administrative burden.",
        styles["BodyText2"]
    ))
    elements.append(Paragraph("Common Pain Points", styles["SectionHeading"]))
    elements.append(bullet_list([
        "<b>Lost receipts:</b> Paper receipts fade, get damaged, or disappear entirely. "
        "By the time finance chases them up, the details are forgotten.",
        "<b>Manual data entry:</b> Accounts staff spend 15-20 hours per week re-typing "
        "receipt data into spreadsheets and accounting systems.",
        "<b>Slow approvals:</b> Email chains for approvals average 3-5 days. Managers "
        "on site rarely check email promptly.",
        "<b>Policy violations:</b> Without real-time checks, 12-18% of claims violate "
        "company expense policies (wrong category, over limit, missing info).",
        "<b>Delayed reimbursements:</b> Employees wait 2-4 weeks for reimbursement, "
        "causing frustration and impacting morale.",
        "<b>Audit risk:</b> Inconsistent records make BAS reporting difficult and "
        "increase the risk of ATO audit findings.",
    ], styles))
    elements.append(Spacer(1, 0.5 * cm))
    elements.append(Paragraph("The Cost of Manual Processing", styles["SectionHeading"]))
    cost_data = [
        ["Metric", "Manual Process", "Automated Process"],
        ["Processing time per claim", "12-15 minutes", "< 2 minutes"],
        ["Average approval time", "3-5 business days", "< 4 hours"],
        ["Error rate", "8-12%", "< 1%"],
        ["Cost per claim", "$15-25", "$2-4"],
        ["Monthly admin hours (200 claims)", "50-60 hours", "5-8 hours"],
    ]
    t = Table(cost_data, colWidths=[5.5 * cm, 4.5 * cm, 4.5 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BRAND_BLUE),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.gray),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GRAY]),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.5 * cm))
    elements.append(Paragraph(
        "For a mid-size construction company processing 200+ expense claims per month, "
        "automation can save over $4,000/month in direct processing costs alone — not "
        "counting the reduction in errors, faster reimbursements, and improved compliance.",
        styles["BodyText2"]
    ))
    elements.append(PageBreak())
    return elements


def build_chapter2(styles):
    elements = []
    elements.append(Paragraph("Chapter 2: Solution Architecture", styles["ChapterTitle"]))
    elements.append(Paragraph(
        "The automated expense claim solution uses Microsoft's Power Platform ecosystem "
        "to create an end-to-end digital process — from receipt capture to reimbursement approval.",
        styles["BodyText2"]
    ))
    elements.append(Paragraph("Architecture Overview", styles["SectionHeading"]))
    elements.append(Paragraph(
        "The solution consists of five core components working together:",
        styles["BodyText2"]
    ))
    arch_data = [
        ["Component", "Technology", "Role"],
        ["Receipt Capture", "PowerApps / Mobile Camera", "Employees photograph receipts"],
        ["Data Extraction", "AI Builder (Receipt Processing)", "OCR extracts vendor, amount, date, GST"],
        ["Workflow Engine", "Power Automate (Cloud Flows)", "Orchestrates approval, validation, routing"],
        ["Data Storage", "SharePoint Online Lists", "Stores claims, receipts, audit trail"],
        ["Reporting", "Excel Online + Office Scripts", "Generates expense reports, BAS summaries"],
    ]
    t = Table(arch_data, colWidths=[3.5 * cm, 4.5 * cm, 6.5 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BRAND_BLUE),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.gray),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GRAY]),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.5 * cm))
    elements.append(Paragraph("Data Flow", styles["SectionHeading"]))
    elements.append(Paragraph(
        "1. Employee opens PowerApp on their phone and photographs the receipt.<br/>"
        "2. AI Builder processes the image, extracting key fields (vendor, amount, date, GST).<br/>"
        "3. Employee reviews extracted data, selects expense category, adds notes.<br/>"
        "4. On submission, Power Automate creates a SharePoint list item with all data.<br/>"
        "5. Flow routes the claim to the appropriate manager based on amount thresholds.<br/>"
        "6. Manager receives an Approval request in Teams with full claim details.<br/>"
        "7. On approval, the claim is recorded in Excel for monthly reporting.<br/>"
        "8. Employee receives a Teams notification with the outcome.",
        styles["BodyText2"]
    ))
    elements.append(Spacer(1, 0.3 * cm))
    elements.append(Paragraph(
        "<b>Tip:</b> The entire process runs in Microsoft 365 — no third-party tools, "
        "no custom code, no Azure subscriptions required.",
        styles["Callout"]
    ))
    elements.append(Paragraph("Licensing Requirements", styles["SectionHeading"]))
    elements.append(bullet_list([
        "<b>Power Automate per-user plan</b> ($15/user/month) — for flow creators",
        "<b>AI Builder add-on</b> ($500/month for 1M credits) — for receipt processing",
        "<b>Microsoft 365 E3/E5</b> — for SharePoint, Teams, Excel Online",
        "<b>Power Apps per-app plan</b> ($5/user/month) — for the mobile capture app",
    ], styles))
    elements.append(Paragraph(
        "For a team of 50 employees submitting expenses, the total platform cost is approximately "
        "$800-1,200/month — significantly less than the manual processing cost it replaces.",
        styles["BodyText2"]
    ))
    elements.append(PageBreak())
    return elements


def build_chapter3(styles):
    elements = []
    elements.append(Paragraph("Chapter 3: Setting Up AI Builder", styles["ChapterTitle"]))
    elements.append(Paragraph(
        "AI Builder's pre-built receipt processing model can extract data from receipts "
        "with high accuracy. This chapter walks through configuration and optimization.",
        styles["BodyText2"]
    ))
    elements.append(Paragraph("Step 1: Enable AI Builder", styles["SectionHeading"]))
    elements.append(Paragraph(
        "Navigate to make.powerapps.com > AI Builder > Explore. The receipt processing "
        "model is a pre-built model — no training data required. It supports receipts in "
        "English and several other languages.",
        styles["BodyText2"]
    ))
    elements.append(Paragraph("Step 2: Test the Pre-built Model", styles["SectionHeading"]))
    elements.append(Paragraph(
        "Before building the full solution, test the model with sample receipts from your "
        "typical vendors (Bunnings, Officeworks, fuel stations, restaurants).",
        styles["BodyText2"]
    ))
    elements.append(bullet_list([
        "Go to AI Builder > Models > Receipt processing > Try it out",
        "Upload 5-10 sample receipts from different vendors",
        "Check extraction accuracy for: Merchant name, Total, Date, GST amount",
        "Note any vendors where extraction is unreliable — you may need fallback logic",
    ], styles))
    elements.append(Paragraph("Step 3: Understand Extracted Fields", styles["SectionHeading"]))
    fields_data = [
        ["Field", "Description", "Confidence Threshold"],
        ["MerchantName", "Vendor/store name", "80%"],
        ["MerchantAddress", "Store address", "70%"],
        ["TransactionDate", "Receipt date", "90%"],
        ["Total", "Total amount inc GST", "95%"],
        ["Subtotal", "Amount before tax", "85%"],
        ["Tax", "GST amount", "85%"],
        ["Items", "Line items array", "75%"],
    ]
    t = Table(fields_data, colWidths=[4 * cm, 5.5 * cm, 4 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BRAND_BLUE),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.gray),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GRAY]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.5 * cm))
    elements.append(Paragraph("Step 4: Configure Confidence Thresholds", styles["SectionHeading"]))
    elements.append(Paragraph(
        "In your Power Automate flow, always check the confidence score for each extracted field. "
        "If confidence is below the threshold, flag the claim for manual review.",
        styles["BodyText2"]
    ))
    elements.append(Paragraph(
        "if(greater(outputs('Process_Receipt')?['body/result/total/confidence'], 0.9),<br/>"
        "&nbsp;&nbsp;outputs('Process_Receipt')?['body/result/total/value'],<br/>"
        "&nbsp;&nbsp;'MANUAL_REVIEW_REQUIRED'<br/>)",
        styles["CodeBlock"]
    ))
    elements.append(Paragraph(
        "<b>Important:</b> AI Builder credits are consumed per document processed. Monitor usage "
        "in the Power Platform admin center to avoid hitting limits.",
        styles["Callout"]
    ))
    elements.append(PageBreak())
    return elements


def build_chapter4(styles):
    elements = []
    elements.append(Paragraph("Chapter 4: Building the Flow", styles["ChapterTitle"]))
    elements.append(Paragraph(
        "This chapter walks through building the core expense claim approval flow in "
        "Power Automate. We will build it step by step with error handling.",
        styles["BodyText2"]
    ))
    elements.append(Paragraph("Flow Overview", styles["SectionHeading"]))
    elements.append(bullet_list([
        "Trigger: When a new item is created in the Expense Claims SharePoint list",
        "Action 1: Get claimant details from Office 365",
        "Action 2: Process receipt image with AI Builder",
        "Action 3: Validate extracted data against policy rules",
        "Action 4: Route to appropriate approver based on amount",
        "Action 5: Update SharePoint with approval outcome",
        "Action 6: Notify claimant via Teams",
        "Error handling: Scope blocks with Configure Run After",
    ], styles))
    elements.append(Paragraph("Step 1: Create the Trigger", styles["SectionHeading"]))
    elements.append(Paragraph(
        "In Power Automate, create a new Automated cloud flow. Select the trigger "
        "'When an item is created' from the SharePoint connector. Configure it to point "
        "to your Expense Claims list.",
        styles["BodyText2"]
    ))
    elements.append(Paragraph(
        "<b>[Screenshot placeholder: SharePoint trigger configuration]</b>",
        styles["Callout"]
    ))
    elements.append(Paragraph("Step 2: Get User Details", styles["SectionHeading"]))
    elements.append(Paragraph(
        "Add a 'Get user profile (V2)' action from the Office 365 Users connector. "
        "Use the ClaimantEmail column from the trigger as the User (UPN). This gives "
        "you the claimant's display name, department, and manager.",
        styles["BodyText2"]
    ))
    elements.append(Paragraph("Step 3: Process Receipt with AI Builder", styles["SectionHeading"]))
    elements.append(Paragraph(
        "Add the 'Process and save information from receipts' action. Point the Document "
        "input to the receipt attachment from the SharePoint item.",
        styles["BodyText2"]
    ))
    elements.append(Paragraph(
        "To get the attachment:<br/>"
        "1. Add 'Get attachments' (SharePoint) after the trigger<br/>"
        "2. Add 'Get attachment content' for the first attachment<br/>"
        "3. Pass the content to AI Builder",
        styles["BodyText2"]
    ))
    elements.append(Paragraph("Step 4: Policy Validation", styles["SectionHeading"]))
    elements.append(Paragraph(
        "Add a Compose action to validate against company policy. Common rules include:",
        styles["BodyText2"]
    ))
    elements.append(bullet_list([
        "Maximum single transaction: $500 (meals), $2,000 (materials), $5,000 (equipment)",
        "Receipt must be dated within 30 days",
        "GST must be present for claims over $82.50",
        "Merchant name must be captured (not blank)",
    ], styles))
    elements.append(Paragraph(
        "// Check if claim amount exceeds policy limit<br/>"
        "if(<br/>"
        "&nbsp;&nbsp;and(<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;equals(triggerBody()?['Category'], 'Meals'),<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;greater(float(triggerBody()?['Amount']), 500)<br/>"
        "&nbsp;&nbsp;),<br/>"
        "&nbsp;&nbsp;'POLICY_VIOLATION',<br/>"
        "&nbsp;&nbsp;'OK'<br/>)",
        styles["CodeBlock"]
    ))
    elements.append(Paragraph("Step 5: Approval Routing", styles["SectionHeading"]))
    elements.append(Paragraph(
        "Use a Switch action on the claim amount to route to the right approver:",
        styles["BodyText2"]
    ))
    routing_data = [
        ["Amount Range", "Approver", "Approval Type"],
        ["$0 - $500", "Direct Manager", "First to respond"],
        ["$501 - $2,000", "Project Manager", "First to respond"],
        ["$2,001 - $5,000", "Project Director", "Everyone must approve"],
        ["$5,001+", "CFO + Project Director", "Everyone must approve"],
    ]
    t = Table(routing_data, colWidths=[4 * cm, 4.5 * cm, 5 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BRAND_BLUE),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.gray),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GRAY]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    elements.append(t)
    elements.append(PageBreak())
    return elements


def build_chapter5(styles):
    elements = []
    elements.append(Paragraph("Chapter 5: Excel Integration", styles["ChapterTitle"]))
    elements.append(Paragraph(
        "Once claims are approved, they need to be recorded in Excel for reporting. "
        "We use Office Scripts to handle complex data formatting that the standard "
        "Excel connector cannot achieve.",
        styles["BodyText2"]
    ))
    elements.append(Paragraph("Why Office Scripts?", styles["SectionHeading"]))
    elements.append(bullet_list([
        "The Excel 'Add a row into a table' connector has known bugs with large tables",
        "Office Scripts provide full control over formatting, validation, and calculations",
        "Scripts can handle complex operations like finding the next empty row, formatting currency, adding conditional formatting",
        "Rate limit: 3 calls per 10 seconds, 1,600 calls per day (plan accordingly)",
    ], styles))
    elements.append(Paragraph("Office Script: Add Expense Row", styles["SectionHeading"]))
    elements.append(Paragraph(
        "function main(workbook: ExcelScript.Workbook,<br/>"
        "&nbsp;&nbsp;claimId: string, claimant: string, amount: string,<br/>"
        "&nbsp;&nbsp;category: string, vendor: string, date: string,<br/>"
        "&nbsp;&nbsp;gst: string, status: string) {<br/>"
        "&nbsp;&nbsp;const sheet = workbook.getWorksheet('Expenses');<br/>"
        "&nbsp;&nbsp;const table = sheet.getTable('ExpenseTable');<br/>"
        "&nbsp;&nbsp;table.addRow(-1, [claimId, claimant, parseFloat(amount),<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;category, vendor, date, parseFloat(gst), status,<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;new Date().toISOString()]);<br/>}",
        styles["CodeBlock"]
    ))
    elements.append(Paragraph("Connecting the Flow to Office Scripts", styles["SectionHeading"]))
    elements.append(Paragraph(
        "In Power Automate, add the 'Run script' action from the Excel Online (Business) "
        "connector. Key configuration:",
        styles["BodyText2"]
    ))
    elements.append(bullet_list([
        "Location: Your SharePoint site or OneDrive",
        "Document Library: Documents",
        "File: /Expense Reports/Monthly-Tracker.xlsx",
        "Script: Add Expense Row",
        "Pass dynamic content from the approval step as parameters",
    ], styles))
    elements.append(Paragraph(
        "<b>Important:</b> The script must be saved in the default Office Scripts location "
        "(OneDrive > Documents > Office Scripts) or a SharePoint library. Use RunScriptProd "
        "for OneDrive scripts, RunScriptProdV2 for SharePoint scripts.",
        styles["Callout"]
    ))
    elements.append(PageBreak())
    return elements


def build_chapter6(styles):
    elements = []
    elements.append(Paragraph("Chapter 6: Testing & Deployment", styles["ChapterTitle"]))
    elements.append(Paragraph("Test Scenarios", styles["SectionHeading"]))
    test_data = [
        ["Scenario", "Input", "Expected Result"],
        ["Happy path", "$150 meal receipt, clear image", "AI extracts data, PM approves, added to Excel"],
        ["Low confidence", "Faded receipt, poor image", "Flagged for manual review"],
        ["Over policy limit", "$600 meal receipt", "Policy violation flag, escalated approval"],
        ["Missing GST", "$100 receipt, no GST shown", "Warning to claimant, manual GST entry"],
        ["Large claim", "$3,500 equipment purchase", "Director + CFO dual approval required"],
        ["Rejection", "Non-business expense", "Rejected, claimant notified with reason"],
    ]
    t = Table(test_data, colWidths=[3.5 * cm, 4.5 * cm, 6 * cm])
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
    elements.append(t)
    elements.append(Spacer(1, 0.5 * cm))
    elements.append(Paragraph("Deployment Checklist", styles["SectionHeading"]))
    elements.append(bullet_list([
        "Create a Power Platform Solution to package the flow",
        "Add environment variables for all configurable values (site URL, list IDs, emails)",
        "Export the solution as managed for production deployment",
        "Test import in a staging environment first",
        "Verify all connection references are mapped correctly",
        "Turn on the flow and submit a test claim end-to-end",
        "Monitor the first 10 real claims closely for issues",
        "Brief all users on the new process with a short training session",
    ], styles))
    elements.append(Paragraph("Go-Live Recommendations", styles["SectionHeading"]))
    elements.append(bullet_list([
        "Run old and new processes in parallel for 2 weeks",
        "Assign a flow champion in each team to handle questions",
        "Set up a Teams channel for reporting issues",
        "Review flow analytics weekly for the first month",
    ], styles))
    elements.append(PageBreak())
    return elements


def build_chapter7(styles):
    elements = []
    elements.append(Paragraph("Chapter 7: Maintenance & Monitoring", styles["ChapterTitle"]))
    elements.append(Paragraph("Setting Up Error Alerts", styles["SectionHeading"]))
    elements.append(Paragraph(
        "The flow uses Scope blocks with 'Configure Run After' set to Failed and TimedOut. "
        "When an error occurs, the Catch scope sends a Teams notification to the admin with "
        "the error details.",
        styles["BodyText2"]
    ))
    elements.append(Paragraph(
        "Additionally, set up a monitoring flow that runs daily to check:",
        styles["BodyText2"]
    ))
    elements.append(bullet_list([
        "Number of failed runs in the last 24 hours",
        "Claims stuck in 'Pending' status for more than 48 hours",
        "AI Builder credit usage approaching limits",
        "Approval requests that have been pending for more than 5 days",
    ], styles))
    elements.append(Paragraph("Flow Analytics", styles["SectionHeading"]))
    elements.append(Paragraph(
        "Power Automate provides built-in analytics. Check these metrics monthly:",
        styles["BodyText2"]
    ))
    elements.append(bullet_list([
        "<b>Success rate:</b> Target 98%+ (investigate anything below 95%)",
        "<b>Average run time:</b> Should be under 5 minutes for non-approval steps",
        "<b>Approval turnaround:</b> Track how long approvals take",
        "<b>AI Builder accuracy:</b> Monitor extraction confidence scores",
    ], styles))
    elements.append(Paragraph("Updating the AI Model", styles["SectionHeading"]))
    elements.append(Paragraph(
        "The pre-built receipt model is updated by Microsoft regularly. However, if you "
        "notice consistent extraction issues with specific vendors, consider training a "
        "custom AI Builder document processing model with your own receipt samples.",
        styles["BodyText2"]
    ))
    elements.append(PageBreak())
    return elements


def build_chapter8(styles):
    elements = []
    elements.append(Paragraph("Chapter 8: Appendix", styles["ChapterTitle"]))
    elements.append(Paragraph("Common Power Automate Expressions", styles["SectionHeading"]))
    expr_data = [
        ["Expression", "Description"],
        ["formatDateTime(utcNow(),'dd/MM/yyyy')", "Current date in AU format"],
        ["float(triggerBody()?['Amount'])", "Convert text amount to number"],
        ["if(equals(x,'Approve'),'Yes','No')", "Conditional text output"],
        ["addDays(utcNow(), 30)", "Date 30 days from now"],
        ["div(float(body('Amount')),11)", "Calculate GST (1/11th of total)"],
        ["concat('EXP-',formatDateTime(utcNow(),'yyyyMMdd'),'-',rand(100,999))", "Generate claim ID"],
        ["length(body('Get_items')?['value'])", "Count items in an array"],
    ]
    t = Table(expr_data, colWidths=[8 * cm, 6.5 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BRAND_BLUE),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (0, -1), "Courier"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.gray),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GRAY]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.5 * cm))
    elements.append(Paragraph("Troubleshooting FAQ", styles["SectionHeading"]))
    faq = [
        ("Q: AI Builder says 'No receipt detected'",
         "A: Ensure the image is clear, well-lit, and the receipt fills most of the frame. "
         "Minimum resolution: 50x50 pixels. Supported formats: JPEG, PNG, PDF."),
        ("Q: Approval emails not arriving",
         "A: Check the Approvals connector is properly authenticated. Verify the approver's "
         "email is correct. Check their junk/spam folder."),
        ("Q: Office Script fails with 'Table not found'",
         "A: Ensure the Excel table is named exactly 'ExpenseTable'. The script is "
         "case-sensitive on table names."),
        ("Q: Flow runs but no data appears in Excel",
         "A: Check that the Excel file is not open by another user in desktop Excel. "
         "Online editing is fine, but desktop locks can block script execution."),
    ]
    for q, a in faq:
        elements.append(Paragraph(f"<b>{q}</b>", styles["BodyText2"]))
        elements.append(Paragraph(a, styles["BodyText2"]))
        elements.append(Spacer(1, 0.3 * cm))
    elements.append(Spacer(1, 1 * cm))
    elements.append(Paragraph(
        "Thank you for purchasing this guide. For questions, updates, or custom consulting, "
        "visit flowtechadvisory.com or email support@flowtechadvisory.com.",
        styles["CoverSubtitle"]
    ))
    return elements


def main():
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2.5 * cm, bottomMargin=2.5 * cm
    )
    styles = get_styles()
    elements = []
    elements.extend(build_cover(styles))
    elements.extend(build_toc(styles))
    elements.extend(build_chapter1(styles))
    elements.extend(build_chapter2(styles))
    elements.extend(build_chapter3(styles))
    elements.extend(build_chapter4(styles))
    elements.extend(build_chapter5(styles))
    elements.extend(build_chapter6(styles))
    elements.extend(build_chapter7(styles))
    elements.extend(build_chapter8(styles))
    doc.build(elements, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f"Created: {OUTPUT}")


if __name__ == "__main__":
    main()
