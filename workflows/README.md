# Power Automate Template Pack for Construction

## Setup Guide

### Prerequisites
- Microsoft 365 Business Basic (or higher) license
- Power Automate per-user or per-flow plan
- SharePoint Online site for your project
- Microsoft Teams for notifications
- Microsoft Forms for form-based triggers

### How to Import Workflows

#### Method 1: Import via Power Automate Portal

1. Go to [Power Automate](https://make.powerautomate.com)
2. Click **My flows** in the left navigation
3. Click **Import** > **Import Package (Legacy)** or use **Solutions** for managed deployment
4. Upload the JSON file
5. Configure connection references (see below)
6. Click **Import**

#### Method 2: Import via Solution (Recommended for Production)

1. Create a new Solution in Power Automate
2. Click **Add existing** > **Cloud flow**
3. Use the JSON definitions as reference to build each flow
4. This method provides better ALM and environment management

### Connection References

Each workflow uses generic connection references. After import, you must configure:

| Connection | Used By | Setup |
|---|---|---|
| SharePoint Online | All workflows | Connect to your M365 account |
| Approvals | Expense, Variation, Payment | Auto-provisioned in your environment |
| Microsoft Teams | All workflows | Connect to your M365 account |
| Office 365 Outlook | Most workflows | Connect to your M365 account |
| Microsoft Forms | PO Generator, Daily Report, Variation | Connect to your M365 account |
| Office 365 Users | Expense Claim | Connect to your M365 account |
| Word Online (Business) | PO Generator | Connect to your M365 account |
| Encodian | Daily Site Report | Requires Encodian subscription (or replace with alternative PDF connector) |

### Workflow Descriptions

#### 1. expense-claim-approval.json
**Trigger:** When a new item is created in the Expense Claims SharePoint list
**What it does:**
- Fetches claimant details from Office 365
- Starts an approval request with claim details
- Updates the SharePoint item with approval status
- Notifies the claimant via Teams
**Parameters to configure:** SharePointSiteUrl, ExpenseClaimsListId, AdminEmail

#### 2. purchase-order-generator.json
**Trigger:** When a new Microsoft Forms response is submitted
**What it does:**
- Generates a unique PO number
- Populates a Word template with form data
- Saves the PO document to SharePoint
- Emails the PO for approval with attachment
- Creates a tracking record in SharePoint
**Parameters to configure:** POFormId, POTemplatePath, SharePointSiteUrl, POListId, ApproverEmail

#### 3. daily-site-report.json
**Trigger:** Recurrence - Daily at 5:00 PM AEST
**What it does:**
- Collects form responses submitted that day
- Retrieves personnel log from SharePoint
- Generates an HTML report
- Converts to PDF (via Encodian connector)
- Saves to SharePoint and emails to Project Manager
**Parameters to configure:** DailyReportFormId, SharePointSiteUrl, PersonnelLogListId, ProjectName, ProjectManagerEmail

#### 4. timesheet-reminder.json
**Trigger:** Recurrence - Every Friday at 2:00 PM AEST
**What it does:**
- Gets all team members from a Teams group
- Checks which members have submitted timesheets
- Sends an Adaptive Card reminder to those who haven't
- Includes a direct link to the timesheet form
**Parameters to configure:** TeamGroupId, SharePointSiteUrl, TimesheetListId, TimesheetFormUrl

#### 5. safety-incident-reporter.json
**Trigger:** PowerApps trigger (called from a mobile app)
**What it does:**
- Creates a safety incident record in SharePoint
- Uploads incident photo if provided
- Routes notifications based on severity (Critical/High/Medium/Low)
- Critical incidents trigger Teams + email to Safety Officer AND Project Director
- Returns incident number to the PowerApp
**Parameters to configure:** SharePointSiteUrl, IncidentListId, SafetyOfficerEmail, ProjectDirectorEmail

#### 6. equipment-maintenance-tracker.json
**Trigger:** Recurrence - Daily at 7:00 AM AEST
**What it does:**
- Retrieves all active equipment from SharePoint
- Calculates days until next service for each item
- Posts OVERDUE alerts for past-due maintenance
- Posts UPCOMING alerts for maintenance due within 7 days
- Posts a daily summary to the maintenance Teams channel
**Parameters to configure:** SharePointSiteUrl, EquipmentListId, TeamGroupId, MaintenanceChannelId

#### 7. rfi-processor.json
**Trigger:** When a new email arrives with "RFI" in the subject
**What it does:**
- Parses the email to extract RFI details
- Determines discipline (Structural/Electrical/Mechanical/Architectural)
- Creates an RFI record in SharePoint
- Saves email attachments to a project folder
- Notifies the assigned discipline lead via Teams
**Parameters to configure:** SharePointSiteUrl, RFIListId, discipline lead emails

#### 8. variation-request-flow.json
**Trigger:** When a new Microsoft Forms response is submitted
**What it does:**
- Creates a variation record in SharePoint
- Stage 1: Project Manager approval
- Stage 2: Director approval (if PM approves)
- Updates SharePoint status at each stage
- Notifies the requestor of the final outcome
**Parameters to configure:** VariationFormId, SharePointSiteUrl, VariationListId, ProjectManagerEmail, DirectorEmail

#### 9. subcontractor-payment-tracker.json
**Trigger:** When a new payment claim is created in SharePoint
**What it does:**
- Retrieves contract details and previous claims
- Calculates retention, GST, and net payable amount
- Starts a dual-approval (PM + Finance Manager)
- Updates claim status and amounts
- Emails the subcontractor with the outcome
**Parameters to configure:** SharePointSiteUrl, PaymentClaimsListId, ContractsListId, ProjectManagerEmail, FinanceManagerEmail

#### 10. project-completion-checklist.json
**Trigger:** Manual button trigger (with Project Name and ID inputs)
**What it does:**
- Checks 5 registers in parallel: RFIs, Variations, Payment Claims, Defects, Safety Incidents
- Builds a pass/fail checklist for each category
- Generates an HTML completion report
- Saves to SharePoint and emails to PM + Director
**Parameters to configure:** SharePointSiteUrl, all list GUIDs, ProjectManagerEmail, DirectorEmail

### Customization Tips

1. **Change notification channels:** Update the Teams channel/chat IDs in each workflow
2. **Add approval stages:** Duplicate the approval actions and add conditions
3. **Modify triggers:** Change recurrence schedules or switch trigger types
4. **Add logging:** Insert "Create item" actions to log flow runs to a SharePoint list
5. **Environment variables:** When deploying via Solutions, replace hardcoded parameters with environment variables

### Troubleshooting

- **Connection errors:** Re-authenticate your connections in Power Automate > Connections
- **SharePoint list not found:** Verify the list GUID matches your environment
- **Approval not received:** Check the Approvals app in Teams; ensure the approver has a Power Automate license
- **Flow fails silently:** Check the error handling Scope blocks — they send notifications to the AdminEmail parameter

### Support

For questions or customization requests, contact Flowtech Advisory.
