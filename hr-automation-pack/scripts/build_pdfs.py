"""
Generate setup-guide PDFs for all 5 HR Automation flows
+ the master product guide PDF.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
import os

BASE = "/Users/liamfrazer/Documents/flowtech/products/hr-automation-pack/flows"

# ── Brand colours ─────────────────────────────────────────────────────────────
NAVY   = colors.HexColor("#1B2A4A")
TEAL   = colors.HexColor("#00A3A3")
LIGHT  = colors.HexColor("#F4F7FA")
WHITE  = colors.white
GREY   = colors.HexColor("#6B7280")
BORDER = colors.HexColor("#E5E7EB")

# ── Styles ────────────────────────────────────────────────────────────────────
def make_styles():
    s = getSampleStyleSheet()
    return {
        "cover_title": ParagraphStyle("cover_title", fontSize=26, textColor=WHITE,
                                       fontName="Helvetica-Bold", spaceAfter=6, alignment=TA_CENTER),
        "cover_sub": ParagraphStyle("cover_sub", fontSize=13, textColor=colors.HexColor("#B0C4DE"),
                                     fontName="Helvetica", spaceAfter=4, alignment=TA_CENTER),
        "cover_badge": ParagraphStyle("cover_badge", fontSize=10, textColor=TEAL,
                                       fontName="Helvetica-Bold", alignment=TA_CENTER),
        "h1": ParagraphStyle("h1", fontSize=18, textColor=NAVY, fontName="Helvetica-Bold",
                              spaceBefore=10, spaceAfter=6),
        "h2": ParagraphStyle("h2", fontSize=13, textColor=TEAL, fontName="Helvetica-Bold",
                              spaceBefore=8, spaceAfter=4),
        "h3": ParagraphStyle("h3", fontSize=11, textColor=NAVY, fontName="Helvetica-Bold",
                              spaceBefore=6, spaceAfter=3),
        "body": ParagraphStyle("body", fontSize=10, textColor=colors.HexColor("#374151"),
                                fontName="Helvetica", spaceAfter=4, leading=15),
        "bullet": ParagraphStyle("bullet", fontSize=10, textColor=colors.HexColor("#374151"),
                                  fontName="Helvetica", spaceAfter=3, leading=14,
                                  leftIndent=16, bulletIndent=4),
        "code": ParagraphStyle("code", fontSize=9, textColor=NAVY, fontName="Courier",
                                backColor=LIGHT, spaceAfter=4, leading=13,
                                leftIndent=10, rightIndent=10),
        "note": ParagraphStyle("note", fontSize=9, textColor=GREY, fontName="Helvetica-Oblique",
                                spaceAfter=4, leading=13),
        "label": ParagraphStyle("label", fontSize=9, textColor=GREY, fontName="Helvetica-Bold",
                                 spaceAfter=2),
        "footer": ParagraphStyle("footer", fontSize=8, textColor=GREY, fontName="Helvetica",
                                  alignment=TA_CENTER),
    }

def divider(color=BORDER):
    return HRFlowable(width="100%", thickness=1, color=color, spaceAfter=8, spaceBefore=4)

def info_box(st, label, items):
    """Teal-bordered info box with bullet points."""
    content = [Paragraph(label, st["h3"])]
    for item in items:
        content.append(Paragraph(f"• {item}", st["bullet"]))
    t = Table([[content]], colWidths=[155*mm])
    t.setStyle(TableStyle([
        ("BOX", (0,0), (-1,-1), 1.5, TEAL),
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#F0FAFA")),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    return t

def step_table(st, steps):
    """Numbered step table."""
    rows = []
    for i, (title, detail) in enumerate(steps, 1):
        num = Paragraph(f"<b>{i}</b>", ParagraphStyle("n", fontSize=13, textColor=WHITE,
                         fontName="Helvetica-Bold", alignment=TA_CENTER))
        txt = [Paragraph(title, st["h3"]), Paragraph(detail, st["body"])]
        rows.append([num, txt])
    t = Table(rows, colWidths=[12*mm, 143*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), TEAL),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (0,-1), 3),
        ("RIGHTPADDING", (0,0), (0,-1), 3),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (1,0), (1,-1), 10),
        ("LINEABOVE", (0,1), (-1,-1), 0.5, BORDER),
        ("ROWBACKGROUNDS", (1,0), (1,-1), [WHITE, LIGHT]),
    ]))
    return t

def sharepoint_schema_table(st, title, columns):
    header = [Paragraph(c, ParagraphStyle("th", fontSize=9, textColor=WHITE,
               fontName="Helvetica-Bold")) for c in ["Column Name","Type","Required","Notes"]]
    rows = [header]
    for col in columns:
        rows.append([Paragraph(c, st["body"]) for c in col])
    t = Table(rows, colWidths=[45*mm, 28*mm, 22*mm, 60*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT]),
        ("GRID", (0,0), (-1,-1), 0.5, BORDER),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    return [Paragraph(title, st["h3"]), t]

def cover_banner(st, flow_num, flow_title, tagline):
    data = [[
        Paragraph("FLOWTECH ADVISORY", st["cover_badge"]),
        Paragraph(f"Flow {flow_num} of 5 — HR Automation Pack", st["cover_badge"]),
    ]]
    banner = Table(data, colWidths=[77.5*mm, 77.5*mm])
    banner.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), NAVY),
        ("TOPPADDING", (0,0), (-1,-1), 14),
        ("BOTTOMPADDING", (0,0), (-1,-1), 14),
    ]))

    title_data = [[Paragraph(flow_title, st["cover_title"])]]
    title_t = Table(title_data, colWidths=[155*mm])
    title_t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), TEAL),
        ("TOPPADDING", (0,0), (-1,-1), 18),
        ("BOTTOMPADDING", (0,0), (-1,-1), 18),
    ]))

    sub_data = [[Paragraph(tagline, st["cover_sub"])]]
    sub_t = Table(sub_data, colWidths=[155*mm])
    sub_t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#0D1F36")),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))

    return [banner, title_t, sub_t, Spacer(1, 10*mm)]

# ══════════════════════════════════════════════════════════════════════════════
# FLOW 1 — New Employee Onboarding
# ══════════════════════════════════════════════════════════════════════════════
def build_flow1_pdf(path, st):
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=27*mm, rightMargin=27*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    story = []
    story += cover_banner(st, 1, "New Employee\nOnboarding Flow",
                          "Automate SharePoint task creation + Teams & email welcome on every new hire")

    story.append(Paragraph("What This Flow Does", st["h1"]))
    story.append(divider())
    story.append(Paragraph(
        "When a new item is added to the <b>HR-Onboarding-Requests</b> SharePoint list, this flow automatically:",
        st["body"]))
    for item in [
        "Creates a set of onboarding tasks in SharePoint (IT setup, HR induction, manager 1:1)",
        "Posts a welcome announcement to your HR Teams channel",
        "Sends a personal welcome email to the new employee's personal address",
        "Notifies HR if any step fails — so nothing slips through",
    ]:
        story.append(Paragraph(f"• {item}", st["bullet"]))
    story.append(Spacer(1, 6*mm))

    story.append(info_box(st, "Connectors Required", [
        "SharePoint Online (standard — included in M365)",
        "Microsoft Teams (standard)",
        "Office 365 Outlook (standard)",
    ]))
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("Before You Import", st["h2"]))
    story.append(step_table(st, [
        ("Create the SharePoint Lists",
         "In your HR SharePoint site, create two lists: <b>HR-Onboarding-Requests</b> (trigger list) and "
         "<b>Onboarding-Tasks</b> (task output list). Column schemas are shown below."),
        ("Note your SharePoint Site URL",
         "You will need the full URL: e.g. https://yourtenant.sharepoint.com/sites/HR"),
        ("Identify your Teams Group + Channel IDs",
         "In Teams, right-click your HR channel > Get link. The groupId and channelId are in the URL."),
        ("Have HR team email addresses ready",
         "The flow sends error alerts to hr@yourdomain.com.au — update this to your real HR inbox."),
    ]))
    story.append(Spacer(1, 4*mm))

    story += sharepoint_schema_table(st, "HR-Onboarding-Requests list columns", [
        ["EmployeeFullName", "Single line text", "Yes", "Full name of new hire"],
        ["EmployeeFirstName", "Single line text", "Yes", "First name (for email greeting)"],
        ["PersonalEmail", "Single line text", "Yes", "Personal email before M365 provisioned"],
        ["StartDate", "Date", "Yes", "First day of employment"],
        ["Department", "Single line text", "Yes", "e.g. Finance, Operations"],
        ["ManagerEmail", "Single line text", "Yes", "Manager's M365 email"],
        ["ManagerName", "Single line text", "Yes", "Manager's display name"],
    ])
    story.append(Spacer(1, 4*mm))
    story += sharepoint_schema_table(st, "Onboarding-Tasks list columns", [
        ["Title", "Single line text", "Yes", "Auto-populated by flow"],
        ["AssignedTo", "Person or Group / text", "No", "IT Team, HR Team, or Manager email"],
        ["DueDate", "Date", "No", "Auto-calculated from StartDate"],
        ["Status", "Choice", "Yes", "Not Started / In Progress / Complete"],
        ["Category", "Choice", "No", "IT Setup / HR Admin / Manager Action"],
    ])
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("Import Steps", st["h2"]))
    story.append(step_table(st, [
        ("Download the ZIP", "Locate <b>flow-template.zip</b> from this folder."),
        ("Open Power Automate", "Go to make.powerautomate.com and sign in with your M365 account."),
        ("Import the flow",
         "My Flows > Import > Import Package (Legacy) > Upload the ZIP > click Import."),
        ("Update SharePoint site URL",
         "Open the imported flow. Search for 'yourtenant' and replace all instances with your actual "
         "SharePoint site URL."),
        ("Update Teams Group + Channel IDs",
         "Find the 'Send Teams Welcome Message' action. Replace YOUR_TEAMS_GROUP_ID and "
         "YOUR_CHANNEL_ID with your actual values."),
        ("Update HR email address",
         "Find the Catch Block action and update hr@yourdomain.com.au to your HR inbox."),
        ("Update connection references",
         "Each connector action will prompt for a connection. Select your existing SharePoint, "
         "Teams, and Outlook connections."),
        ("Save and test",
         "Save the flow. Add a test row to HR-Onboarding-Requests in SharePoint and confirm "
         "tasks appear in Onboarding-Tasks and the Teams message is sent."),
    ]))

    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("Troubleshooting", st["h2"]))
    story.append(Paragraph(
        "If the flow fails, check <b>My Flows > [Flow Name] > Run History</b> and click the failed run "
        "to see which action errored. Common issues:", st["body"]))
    for tip in [
        "SharePoint URL mismatch — double-check the site URL and list names are exact (case-sensitive)",
        "Teams channel not found — verify the Group ID and Channel ID are correct",
        "Connection reference errors — re-authenticate each connector in the flow editor",
    ]:
        story.append(Paragraph(f"• {tip}", st["bullet"]))

    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Questions? Email support@flowtech.com.au with your order number.", st["note"]))
    story.append(divider(TEAL))
    story.append(Paragraph("Flowtech Advisory — Power Automate HR Automation Pack | flowtech.com.au", st["footer"]))

    doc.build(story)
    print(f"Built: {path}")


# ══════════════════════════════════════════════════════════════════════════════
# FLOW 2 — Leave Request Approval
# ══════════════════════════════════════════════════════════════════════════════
def build_flow2_pdf(path, st):
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=27*mm, rightMargin=27*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    story = []
    story += cover_banner(st, 2, "Leave Request\nApproval Flow",
                          "Microsoft Forms submission → manager approval → HR calendar update + employee notification")

    story.append(Paragraph("What This Flow Does", st["h1"]))
    story.append(divider())
    story.append(Paragraph(
        "When an employee submits the <b>Leave Request Microsoft Form</b>, this flow:", st["body"]))
    for item in [
        "Retrieves the full form response details",
        "Sends an approval request to the manager via the built-in Approvals connector",
        "If APPROVED: adds the leave to the HR Outlook calendar, logs it in the SharePoint Leave Register, and emails the employee a confirmation",
        "If DECLINED: emails the employee with the outcome and next steps",
        "On any error: notifies HR to handle the request manually",
    ]:
        story.append(Paragraph(f"• {item}", st["bullet"]))
    story.append(Spacer(1, 5*mm))

    story.append(info_box(st, "Connectors Required", [
        "Microsoft Forms (standard)",
        "Approvals (standard — included in M365)",
        "Office 365 Outlook (standard)",
        "SharePoint Online (standard)",
    ]))
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("Before You Import", st["h2"]))
    story.append(step_table(st, [
        ("Create the Leave Request Form in Microsoft Forms",
         "Go to forms.microsoft.com. Create a form with the fields listed in the schema table below. "
         "Note the Form ID from the URL after creating it."),
        ("Create the SharePoint Leave Register list",
         "In your HR SharePoint site, create a list called <b>Leave-Register</b> with the columns below."),
        ("Create a shared HR Outlook calendar",
         "In Outlook, create a shared calendar named 'HR Leave Calendar' that the HR team can view."),
        ("Note manager email addresses",
         "The form should include a field where employees enter their manager's email. "
         "Alternatively, look this up from Azure AD using the Graph API."),
    ]))
    story.append(Spacer(1, 4*mm))

    story += sharepoint_schema_table(st, "Microsoft Forms — Leave Request fields", [
        ["r1 (auto)", "Date/time", "Auto", "Submission timestamp"],
        ["r2 (Email)", "Email", "Yes", "Employee work email"],
        ["r3 (Name)", "Text", "Yes", "Employee full name"],
        ["r4 (Leave type)", "Choice", "Yes", "Annual / Sick / Personal / Unpaid / Other"],
        ["r5 (Days)", "Number", "Yes", "Number of working days requested"],
        ["r6 (From date)", "Date", "Yes", "First day of leave"],
        ["r7 (To date)", "Date", "Yes", "Last day of leave"],
        ["r8 (Reason)", "Text", "No", "Optional reason"],
        ["managerEmail", "Text", "Yes", "Direct manager's M365 email"],
    ])
    story.append(Spacer(1, 4*mm))
    story += sharepoint_schema_table(st, "Leave-Register SharePoint list columns", [
        ["Title", "Single line text", "Yes", "Employee name (auto-set)"],
        ["LeaveType", "Choice", "Yes", "Annual / Sick / Personal / Unpaid"],
        ["StartDate", "Date", "Yes", "Auto-populated"],
        ["EndDate", "Date", "Yes", "Auto-populated"],
        ["Days", "Number", "Yes", "Auto-populated"],
        ["Status", "Choice", "Yes", "Approved / Declined / Pending"],
        ["ApprovedBy", "Single line text", "No", "Manager email auto-populated"],
    ])
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("Import Steps", st["h2"]))
    story.append(step_table(st, [
        ("Import the flow ZIP", "My Flows > Import > Import Package (Legacy) > Upload flow-template.zip."),
        ("Connect to Microsoft Forms",
         "In the trigger action, select your connection and set the Form ID to your Leave Request form."),
        ("Update the Get Response Details action",
         "Set the Form ID in 'Get form response details' to match the trigger."),
        ("Configure the Approvals action",
         "The flow uses the 'Start and wait for an approval' action. The assignedTo field reads the "
         "manager email from the form response — no changes needed if your form includes managerEmail."),
        ("Connect your HR Outlook calendar",
         "In 'Add to HR Leave Calendar', authenticate with the M365 account that owns the HR shared calendar."),
        ("Update SharePoint site URL",
         "Replace 'yourtenant.sharepoint.com/sites/HR' with your actual SharePoint HR site URL."),
        ("Update HR error email",
         "In the Catch Block, update hr@yourdomain.com.au to your HR inbox address."),
        ("Save, test, and validate",
         "Submit a test leave request through the form. Confirm the manager receives an approval email, "
         "approve it, then verify the calendar entry and SharePoint row are created and the employee "
         "receives a confirmation email."),
    ]))

    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Questions? Email support@flowtech.com.au with your order number.", st["note"]))
    story.append(divider(TEAL))
    story.append(Paragraph("Flowtech Advisory — Power Automate HR Automation Pack | flowtech.com.au", st["footer"]))
    doc.build(story)
    print(f"Built: {path}")


# ══════════════════════════════════════════════════════════════════════════════
# FLOW 3 — Monthly Timesheet Reminder
# ══════════════════════════════════════════════════════════════════════════════
def build_flow3_pdf(path, st):
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=27*mm, rightMargin=27*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    story = []
    story += cover_banner(st, 3, "Monthly Timesheet\nReminder Flow",
                          "Scheduled reminder every 25th — Teams channel post + all-staff email")

    story.append(Paragraph("What This Flow Does", st["h1"]))
    story.append(divider())
    story.append(Paragraph(
        "On the <b>25th of every month at 9:00 AM (AUS Eastern)</b>, this flow:", st["body"]))
    for item in [
        "Calculates the current month name dynamically (no manual updates needed)",
        "Posts a rich-text reminder to your designated Teams channel",
        "Sends a reminder email to your all-staff distribution list",
        "Alerts HR if the flow fails so the reminder can be sent manually",
    ]:
        story.append(Paragraph(f"• {item}", st["bullet"]))
    story.append(Spacer(1, 5*mm))

    story.append(info_box(st, "Connectors Required", [
        "Microsoft Teams (standard)",
        "Office 365 Outlook (standard)",
    ]))
    story.append(Paragraph(
        "This is the simplest flow in the pack — no SharePoint lists required. "
        "It's ready to use in under 10 minutes.", st["note"]))
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("Before You Import", st["h2"]))
    story.append(step_table(st, [
        ("Identify your Teams Group and Channel IDs",
         "Right-click the target channel in Teams > Get link. Extract the groupId and channelId from the URL."),
        ("Confirm your all-staff email address",
         "Typically an M365 distribution group like all-staff@yourdomain.com.au or a Teams group email."),
        ("Decide the reminder day",
         "The default is the 25th. If your payroll deadline is different, update the recurrence trigger."),
        ("Confirm your timezone",
         "Default is AUS Eastern Standard Time. Update if your team is in a different timezone."),
    ]))
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("Import Steps", st["h2"]))
    story.append(step_table(st, [
        ("Import the flow ZIP", "My Flows > Import > Import Package (Legacy) > Upload flow-template.zip."),
        ("Update Teams Group ID",
         "In the 'Post Teams message' action, replace YOUR_GROUP_ID with your actual Teams Group ID."),
        ("Update Teams Channel ID",
         "In the same action, replace YOUR_CHANNEL_ID with your HR or General channel ID."),
        ("Update the all-staff email address",
         "In 'Send Timesheet Reminder Email', update all-staff@yourdomain.com.au to your distribution list."),
        ("Update HR error email",
         "In the Catch Block, update hr@yourdomain.com.au to your HR inbox."),
        ("Adjust the reminder day (optional)",
         "In the Recurrence trigger, change the monthDays value (default: [25]) to your preferred day."),
        ("Save and test",
         "Use 'Test > Manually' in Power Automate to trigger the flow immediately and confirm both "
         "the Teams message and email arrive correctly."),
    ]))

    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("Customisation Tips", st["h2"]))
    for tip in [
        "Change the reminder message text in both actions to match your company's tone",
        "Add a manager approval step after timesheet submission by chaining with Flow 2",
        "Add additional reminder days (e.g. also on the 28th) by duplicating the two message actions",
    ]:
        story.append(Paragraph(f"• {tip}", st["bullet"]))

    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Questions? Email support@flowtech.com.au with your order number.", st["note"]))
    story.append(divider(TEAL))
    story.append(Paragraph("Flowtech Advisory — Power Automate HR Automation Pack | flowtech.com.au", st["footer"]))
    doc.build(story)
    print(f"Built: {path}")


# ══════════════════════════════════════════════════════════════════════════════
# FLOW 4 — Performance Review Reminder Sequence
# ══════════════════════════════════════════════════════════════════════════════
def build_flow4_pdf(path, st):
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=27*mm, rightMargin=27*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    story = []
    story += cover_banner(st, 4, "Performance Review\nReminder Sequence",
                          "Automated 30 / 14 / 7-day email reminders to managers and employees for every scheduled review")

    story.append(Paragraph("What This Flow Does", st["h1"]))
    story.append(divider())
    story.append(Paragraph(
        "This flow runs <b>daily at 8:00 AM (AUS Eastern)</b> and checks the "
        "<b>Performance-Reviews</b> SharePoint list for any reviews with status = 'Scheduled'. "
        "For each upcoming review, it automatically sends:", st["body"]))

    data = [
        ["Trigger Point", "Who Receives It", "Purpose"],
        ["30 days before review", "Manager + Employee (CC)", "Plan ahead — gather evidence, block calendars, self-assessment notice"],
        ["14 days before review", "Manager + Employee (CC)", "Mid-point check — confirm self-assessment submitted, KPIs documented"],
        ["7 days before review", "Manager + Employee (CC) + HR Teams alert", "Final reminder — urgent, all prep must be complete"],
    ]
    t = Table(data, colWidths=[42*mm, 50*mm, 63*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("TEXTCOLOR", (0,0), (-1,0), WHITE),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 9),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT]),
        ("GRID", (0,0), (-1,-1), 0.5, BORDER),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    story.append(t)
    story.append(Spacer(1, 5*mm))

    story.append(info_box(st, "Connectors Required", [
        "SharePoint Online (standard)",
        "Office 365 Outlook (standard)",
        "Microsoft Teams (standard)",
    ]))
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("Before You Import", st["h2"]))
    story.append(step_table(st, [
        ("Create the Performance-Reviews SharePoint list",
         "This list stores all scheduled reviews and is the data source for the flow. "
         "See the column schema below."),
        ("Populate initial review data",
         "Add one row per employee review (name, dates, manager email, status = Scheduled). "
         "Update the Status to 'Completed' after each review so it stops triggering reminders."),
        ("Identify your HR Teams channel IDs",
         "The 7-day reminder posts a Teams alert to your HR channel. Note the Group ID and Channel ID."),
    ]))
    story.append(Spacer(1, 4*mm))

    story += sharepoint_schema_table(st, "Performance-Reviews SharePoint list columns", [
        ["EmployeeName", "Single line text", "Yes", "Full name of employee"],
        ["EmployeeEmail", "Single line text", "Yes", "Employee M365 email"],
        ["ManagerName", "Single line text", "Yes", "Manager display name"],
        ["ManagerEmail", "Single line text", "Yes", "Manager M365 email"],
        ["ReviewDate", "Date", "Yes", "Scheduled date of the review meeting"],
        ["ReviewPeriod", "Single line text", "No", "e.g. Q1 2025, FY2024-25"],
        ["ReviewStatus", "Choice", "Yes", "Scheduled / Completed / Deferred"],
    ])
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("Import Steps", st["h2"]))
    story.append(step_table(st, [
        ("Import the flow ZIP", "My Flows > Import > Import Package (Legacy) > Upload flow-template.zip."),
        ("Update SharePoint site URL",
         "Replace 'yourtenant.sharepoint.com/sites/HR' with your actual HR SharePoint site URL in "
         "the 'Get All Employees' action."),
        ("Update Teams Group + Channel IDs",
         "In the 7-day reminder 'Post Teams Alert' action, replace YOUR_HR_GROUP_ID and "
         "YOUR_HR_CHANNEL_ID with your actual values."),
        ("Update the SharePoint list name",
         "If you named the list differently, update the table reference in the 'Get All Employees' action."),
        ("Update HR error email",
         "In the Catch Block, update hr@yourdomain.com.au to your HR inbox."),
        ("Verify the review link URL",
         "In the email body, update the SharePoint link to point to your actual Performance-Reviews list."),
        ("Save and test",
         "Add a test row with ReviewDate = today + 30 days, status = Scheduled. "
         "Trigger the flow manually and confirm the 30-day email is sent."),
    ]))

    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Questions? Email support@flowtech.com.au with your order number.", st["note"]))
    story.append(divider(TEAL))
    story.append(Paragraph("Flowtech Advisory — Power Automate HR Automation Pack | flowtech.com.au", st["footer"]))
    doc.build(story)
    print(f"Built: {path}")


# ══════════════════════════════════════════════════════════════════════════════
# FLOW 5 — Offboarding Checklist
# ══════════════════════════════════════════════════════════════════════════════
def build_flow5_pdf(path, st):
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=27*mm, rightMargin=27*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    story = []
    story += cover_banner(st, 5, "Employee Offboarding\nChecklist Flow",
                          "Auto-create tasks for IT, HR, and manager — plus Teams notification — on every departure")

    story.append(Paragraph("What This Flow Does", st["h1"]))
    story.append(divider())
    story.append(Paragraph(
        "When a new row is added to the <b>Offboarding-Requests</b> SharePoint list, "
        "this flow creates a complete set of offboarding tasks and notifies all stakeholders:", st["body"]))

    tasks_data = [
        ["Task", "Assigned To", "Due Date"],
        ["Revoke M365 access", "IT Team", "Last day"],
        ["Collect laptop, phone, and access cards", "IT Team", "Last day"],
        ["Conduct exit interview", "HR Team", "3 days before last day"],
        ["Process final pay, leave payout, separation docs", "HR Team", "Last day"],
        ["Arrange knowledge transfer and handover", "Line Manager", "5 days before last day"],
    ]
    t = Table(tasks_data, colWidths=[75*mm, 40*mm, 40*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("TEXTCOLOR", (0,0), (-1,0), WHITE),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 9),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT]),
        ("GRID", (0,0), (-1,-1), 0.5, BORDER),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    story.append(t)
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph(
        "After creating all tasks, the flow posts a summary to your HR Teams channel and "
        "emails the line manager with their specific actions.", st["body"]))
    story.append(Spacer(1, 5*mm))

    story.append(info_box(st, "Connectors Required", [
        "SharePoint Online (standard)",
        "Microsoft Teams (standard)",
        "Office 365 Outlook (standard)",
    ]))
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("Before You Import", st["h2"]))
    story.append(step_table(st, [
        ("Create the Offboarding-Requests SharePoint list",
         "HR adds a new row to this list to trigger the flow. See the schema below."),
        ("Create the Offboarding-Tasks SharePoint list",
         "This is where tasks are written to. IT, HR, and the manager check this list. "
         "See schema below."),
        ("Identify your HR Teams channel",
         "The flow posts a summary notification to your HR Teams channel. Note the Group ID and Channel ID."),
        ("Ensure HR has access to both lists",
         "All team members who need to action tasks must have Contribute access to Offboarding-Tasks."),
    ]))
    story.append(Spacer(1, 4*mm))

    story += sharepoint_schema_table(st, "Offboarding-Requests SharePoint list columns", [
        ["EmployeeFullName", "Single line text", "Yes", "Full name of departing employee"],
        ["LastDay", "Date", "Yes", "Final working day"],
        ["Department", "Single line text", "Yes", "Employee's department"],
        ["ManagerEmail", "Single line text", "Yes", "Direct manager's M365 email"],
        ["ManagerName", "Single line text", "Yes", "Manager display name (for email greeting)"],
        ["ReasonForLeaving", "Choice", "No", "Resignation / Redundancy / End of Contract / Other"],
    ])
    story.append(Spacer(1, 4*mm))
    story += sharepoint_schema_table(st, "Offboarding-Tasks SharePoint list columns", [
        ["Title", "Single line text", "Yes", "Auto-populated by flow"],
        ["AssignedTo", "Single line text", "Yes", "IT Team / HR Team / Manager email"],
        ["DueDate", "Date", "Yes", "Auto-calculated from LastDay"],
        ["Status", "Choice", "Yes", "Not Started / In Progress / Complete"],
        ["Category", "Choice", "No", "IT / HR / Manager"],
        ["EmployeeName", "Single line text", "No", "Auto-populated from trigger"],
        ["Priority", "Choice", "No", "High / Normal"],
    ])
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("Import Steps", st["h2"]))
    story.append(step_table(st, [
        ("Import the flow ZIP", "My Flows > Import > Import Package (Legacy) > Upload flow-template.zip."),
        ("Update SharePoint site URL",
         "Replace 'yourtenant.sharepoint.com/sites/HR' with your actual HR SharePoint site URL "
         "throughout all SharePoint actions."),
        ("Update Teams Group + Channel IDs",
         "In 'Send Offboarding Summary Teams Message', replace YOUR_HR_GROUP_ID and "
         "YOUR_HR_CHANNEL_ID."),
        ("Update HR email in Catch Block",
         "Replace hr@yourdomain.com.au with your HR inbox."),
        ("Update the manager email action",
         "In 'Send Farewell Preparation Email to Manager', verify the CC address is your HR inbox."),
        ("Save and test",
         "Add a test row to Offboarding-Requests with LastDay = 2 weeks from today. "
         "Trigger the flow manually and confirm tasks appear in Offboarding-Tasks, "
         "the Teams message posts, and the manager email arrives."),
    ]))

    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Questions? Email support@flowtech.com.au with your order number.", st["note"]))
    story.append(divider(TEAL))
    story.append(Paragraph("Flowtech Advisory — Power Automate HR Automation Pack | flowtech.com.au", st["footer"]))
    doc.build(story)
    print(f"Built: {path}")


# ══════════════════════════════════════════════════════════════════════════════
# MASTER PRODUCT GUIDE
# ══════════════════════════════════════════════════════════════════════════════
def build_master_guide(path, st):
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=27*mm, rightMargin=27*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    story = []

    # Cover
    cover_header = Table([[Paragraph("FLOWTECH ADVISORY", st["cover_badge"])]],
                         colWidths=[155*mm])
    cover_header.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), NAVY),
        ("TOPPADDING", (0,0), (-1,-1), 16),
        ("BOTTOMPADDING", (0,0), (-1,-1), 16),
    ]))
    story.append(cover_header)

    title_t = Table([[Paragraph("Power Automate\nHR Automation Pack", st["cover_title"])]],
                    colWidths=[155*mm])
    title_t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), TEAL),
        ("TOPPADDING", (0,0), (-1,-1), 22),
        ("BOTTOMPADDING", (0,0), (-1,-1), 22),
    ]))
    story.append(title_t)

    sub_t = Table([[Paragraph("5 Ready-to-Use M365 Flow Templates for HR Teams", st["cover_sub"])]],
                  colWidths=[155*mm])
    sub_t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#0D1F36")),
        ("TOPPADDING", (0,0), (-1,-1), 12),
        ("BOTTOMPADDING", (0,0), (-1,-1), 12),
    ]))
    story.append(sub_t)
    story.append(Spacer(1, 10*mm))

    story.append(Paragraph("Welcome", st["h1"]))
    story.append(divider())
    story.append(Paragraph(
        "Thank you for purchasing the <b>Power Automate HR Automation Pack</b> from Flowtech Advisory. "
        "This pack gives your HR team 5 production-ready Power Automate flows that cover the full "
        "employee lifecycle — from onboarding to offboarding.", st["body"]))
    story.append(Paragraph(
        "Each flow comes with a detailed setup guide (in its own folder). This master guide gives "
        "you an overview of all 5 flows, what they automate, and how to get started quickly.", st["body"]))
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("What's in the Pack", st["h1"]))
    story.append(divider())

    flows_summary = [
        ("Flow 1", "New Employee Onboarding",
         "Triggered from SharePoint. Creates task checklist for IT, HR, and the manager. "
         "Posts Teams welcome message. Emails new hire at personal address."),
        ("Flow 2", "Leave Request Approval",
         "Triggered by Microsoft Forms. Routes to manager approval. Updates HR Outlook calendar "
         "and SharePoint Leave Register. Emails employee outcome."),
        ("Flow 3", "Monthly Timesheet Reminder",
         "Scheduled on the 25th of every month. Posts to Teams channel and emails all staff. "
         "Zero configuration after initial setup."),
        ("Flow 4", "Performance Review Reminder Sequence",
         "Daily check against SharePoint list. Sends 30-day, 14-day, and 7-day email reminders "
         "to managers and employees. Teams alert at 7-day mark."),
        ("Flow 5", "Offboarding Checklist",
         "Triggered from SharePoint. Creates tasks for IT (access revocation, equipment), "
         "HR (exit interview, final pay), and the manager (knowledge transfer). "
         "Teams notification and manager email."),
    ]

    for num, title, desc in flows_summary:
        row = Table([[
            Paragraph(num, ParagraphStyle("fn", fontSize=9, textColor=WHITE,
                       fontName="Helvetica-Bold", alignment=TA_CENTER)),
            [Paragraph(title, st["h3"]), Paragraph(desc, st["body"])]
        ]], colWidths=[16*mm, 139*mm])
        row.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (0,-1), TEAL),
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("TOPPADDING", (0,0), (-1,-1), 8),
            ("BOTTOMPADDING", (0,0), (-1,-1), 8),
            ("LEFTPADDING", (1,0), (1,-1), 10),
            ("LINEBELOW", (0,0), (-1,-1), 0.5, BORDER),
        ]))
        story.append(row)
        story.append(Spacer(1, 2*mm))

    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("Requirements", st["h1"]))
    story.append(divider())
    for req in [
        "<b>Microsoft 365 Business Standard or above</b> (for Approvals connector and full Teams integration)",
        "<b>Power Automate</b> — included in most M365 plans, access at make.powerautomate.com",
        "<b>SharePoint Online</b> — for list-based triggers and task management",
        "<b>Microsoft Teams</b> — for channel notifications",
        "<b>Office 365 Outlook</b> — for email notifications and calendar updates",
        "<b>Microsoft Forms</b> — for Flow 2 leave request trigger",
        "<b>Basic Power Automate familiarity</b> — ability to import a flow and update connections",
    ]:
        story.append(Paragraph(f"• {req}", st["bullet"]))
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("How to Import a Flow", st["h1"]))
    story.append(divider())
    story.append(Paragraph(
        "All 5 flows are standard Power Automate packages (ZIP files). Import using these steps:", st["body"]))
    story.append(step_table(st, [
        ("Go to make.powerautomate.com", "Sign in with your Microsoft 365 account."),
        ("Navigate to My Flows", "Click 'My Flows' in the left navigation."),
        ("Click Import", "Click 'Import' at the top > 'Import Package (Legacy)'."),
        ("Upload the ZIP", "Click 'Upload' and select the flow-template.zip from the flow folder."),
        ("Review import settings", "Ensure 'Create as new' is selected for the flow. Click Import."),
        ("Update connections",
         "Open the imported flow and connect each action to your M365 connections "
         "(SharePoint, Teams, Outlook, Forms, Approvals)."),
        ("Update placeholders",
         "Search for 'yourtenant' and 'YOUR_' and replace with your actual site URLs and IDs. "
         "Each setup guide lists every placeholder to update."),
        ("Save and test", "Save the flow, then use 'Test > Manually' to run it and verify the output."),
    ]))
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("Frequently Asked Questions", st["h1"]))
    story.append(divider())
    faqs = [
        ("Do these work with Power Automate free?",
         "The Approvals connector in Flow 2 requires a paid M365 licence. All other connectors are "
         "standard and included in Business Basic and above. Flow 3 (Timesheet Reminder) works with "
         "any M365 plan."),
        ("Can I customise the flows?",
         "Absolutely. Every action is labelled clearly. Add conditions, extra notifications, or "
         "additional steps as needed. The flow definitions are not locked."),
        ("Are these solution-aware (Dataverse)?",
         "No — these are standard flow packages. You can import them directly via Power Automate or "
         "manually add them to a Dataverse solution after import."),
        ("What if a flow fails?",
         "Every flow includes a Catch Block that emails your HR inbox when a failure occurs. "
         "Check My Flows > Run History for the full error details."),
        ("Can I use these with Power Automate Desktop?",
         "No — these are cloud flows designed for the Power Automate web service, not desktop automation."),
        ("Do you offer setup support?",
         "Yes — email support@flowtech.com.au with your order number and we'll help you get configured."),
    ]
    for q, a in faqs:
        story.append(Paragraph(q, st["h3"]))
        story.append(Paragraph(a, st["body"]))
        story.append(Spacer(1, 3*mm))

    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("About Flowtech Advisory", st["h1"]))
    story.append(divider())
    story.append(Paragraph(
        "Flowtech Advisory builds automation solutions for Australian businesses running on "
        "Microsoft 365. We specialise in Power Automate, SharePoint, and Teams integrations — "
        "from quick wins to enterprise rollouts.", st["body"]))
    story.append(Paragraph(
        "Website: <b>flowtech.com.au</b> | Support: <b>support@flowtech.com.au</b>", st["body"]))
    story.append(Spacer(1, 8*mm))
    story.append(divider(TEAL))
    story.append(Paragraph(
        "Flowtech Advisory — Power Automate HR Automation Pack | flowtech.com.au | April 2026",
        st["footer"]))

    doc.build(story)
    print(f"Built: {path}")


# ── Run everything ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    st = make_styles()

    build_flow1_pdf(f"{BASE}/01-employee-onboarding/setup-guide.pdf", st)
    build_flow2_pdf(f"{BASE}/02-leave-request-approval/setup-guide.pdf", st)
    build_flow3_pdf(f"{BASE}/03-timesheet-reminder/setup-guide.pdf", st)
    build_flow4_pdf(f"{BASE}/04-performance-review-reminders/setup-guide.pdf", st)
    build_flow5_pdf(f"{BASE}/05-offboarding-checklist/setup-guide.pdf", st)

    master_path = "/Users/liamfrazer/Documents/flowtech/products/hr-automation-pack/HR-Automation-Pack-Guide.pdf"
    build_master_guide(master_path, st)

    print("\nAll PDFs built successfully.")
