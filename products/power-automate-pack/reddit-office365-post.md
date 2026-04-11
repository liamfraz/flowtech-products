# Reddit Post — r/Office365

**Title:** I packaged 5 M365 Power Automate templates — onboarding, approvals, SharePoint alerts. Free to use, paid bundle if you want docs.

---

**Body:**

If your team is on Microsoft 365 and still doing approvals over email and onboarding via a 12-tab checklist, this post is for you.

I've been setting up Power Automate workflows for M365 environments for a few years. The same 5 automation use cases come up almost everywhere. Here they are, with enough detail to build them yourself.

---

**What these flows do and why they matter for M365 teams:**

**1. New Employee Onboarding Automation**

The problem: IT sends a welcome email manually, someone remembers to add them to Teams, someone else forgets the SharePoint groups, and the new hire spends day one waiting for access.

The flow: triggered by a new item in your onboarding SharePoint list. Sends welcome email with M365 quick-start links, posts intro to the team's Teams channel, adds user to relevant SharePoint groups via the Microsoft Graph API. Everything that used to require 3 people to coordinate, now requires none.

---

**2. Document Approval in SharePoint + Teams**

The problem: Someone uploads a policy or contract to SharePoint, sends an email asking for approval, the approver doesn't see it, the document sits in limbo for two weeks.

The flow: when a document is added to a SharePoint library, the flow sends an Adaptive Card to the approver directly in Teams — with Approve, Reject, and Comment buttons. The outcome writes back to the SharePoint item automatically. No email chains. No chasing.

---

**3. SharePoint List Change Alerts (That Actually Make Sense)**

The problem: SharePoint's built-in "Alert Me" emails everyone for everything. Nobody reads them. High-signal alerts get ignored alongside low-signal noise.

The flow: monitors your SharePoint list for meaningful changes — configurable by field value and change type. Notifies the right person (pulled from a lookup column, not a hardcoded email) via Teams or email, depending on urgency. The result is alerts people actually act on.

---

**4. Leave Request and Approval**

The problem: leave requests go into a shared inbox, managers forget to respond, HR has to chase, employees don't know the status.

The flow: employee submits a SharePoint form, the flow routes to their line manager via Teams, handles approve/reject, updates the HR SharePoint list, and creates the Outlook calendar block automatically. Manager gets a reminder after 48 hours if they haven't responded. End-to-end with no manual follow-up.

---

**5. Monday Morning Team Digest**

The problem: nobody knows what happened last week, what's overdue, or what's coming — unless they dig through SharePoint themselves.

The flow: every Monday at 8am, pulls last week's activity from a SharePoint list (new items, updated items, overdue items) and posts a structured summary to your Teams channel. The team starts Monday briefed, without a meeting.

---

**Getting started:**

All of these use standard M365 connectors — SharePoint, Teams, Outlook, and Office 365 Users. No premium connectors required for most of them (the Graph API call in onboarding needs HTTP with Azure AD, which is premium, but there's a workaround using the standard connector if you're on a basic licence).

If you want the importable JSON files with setup docs for each flow rather than building from my descriptions above, I packaged them: $49 at the link below.

https://flowtechadvisory.gumroad.com/l/m365-automation-starter-pack

Questions welcome — happy to go deeper on any of these, particularly the SharePoint trigger configuration and the Adaptive Cards approval pattern.
