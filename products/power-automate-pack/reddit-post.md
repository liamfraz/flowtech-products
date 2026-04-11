# Reddit Post — r/PowerAutomate

**Title:** I packaged 5 M365 Power Automate templates — onboarding, approvals, SharePoint alerts. Free to use, paid bundle if you want docs.

---

**Body:**

Been building the same set of Power Automate flows across M365 client projects for the past few years. Every single engagement, I'd end up building variations of the same 5 workflows. After the fifth time, I stopped rebuilding them and started maintaining a set of clean, importable templates.

Sharing the core logic here. Use it however you want. There's a paid pack at the end if you want the full JSON files with setup docs — but the value is in the post regardless.

---

**The 5 flows and how they're built:**

**1. New Employee Onboarding**

Trigger: SharePoint list item created (your HR onboarding list)

Actions:
- Send welcome email via Outlook with M365 quick-start links
- Post intro message to the team's Teams channel
- Add user to relevant SharePoint groups via Graph API call

The Graph API step trips people up — you need a Service Principal or a licensed account with the right permissions. Worth setting up properly once.

---

**2. Document Approval Routing**

Trigger: SharePoint library — file added or modified

Actions:
- Get approver from a lookup column (or hardcode for simple setups)
- Send Adaptive Card to approver in Teams with Approve / Reject / Comment buttons
- Update SharePoint item with approval status and approver comments
- Send outcome notification to the submitter

The Adaptive Card approach beats the built-in Approvals connector for anything complex — you can include document metadata directly in the card.

---

**3. SharePoint List Change Alerts**

Trigger: SharePoint list item created or modified

Actions:
- Check field conditions (e.g. "Status changed to Overdue", "Priority = High")
- Route notification to the right person based on a lookup field (not a hardcoded email)
- Send Teams message or email depending on urgency condition

Key lesson: use a condition to check whether the field that matters actually changed. Otherwise you get notifications on every edit, which kills trust in the automation fast.

---

**4. Leave Request Approval**

Trigger: SharePoint list item created (leave request form)

Actions:
- Send approval to line manager (pulled from a People column on the SharePoint list)
- Handle Approve: update SharePoint item status, create Outlook calendar event for the employee
- Handle Reject: update status, send rejection email with manager comments
- Timeout handling: reminder to manager after 48 hours if no response

The calendar event step needs the employee's UPN from the SharePoint item — make sure your form captures that.

---

**5. Weekly Team Digest**

Trigger: Recurrence — Monday 8am

Actions:
- Get items from SharePoint list created in last 7 days
- Get items modified in last 7 days
- Get items where due date < today and status != "Complete" (overdue)
- Build HTML summary table using compose + string formatting
- Post to Teams channel or send via Outlook

The OData filter for "created in last 7 days" catches people out. You need: `Created ge '${addDays(utcNow(), -7)}'` formatted as a proper ISO datetime string, not just a date.

---

**General tips that apply to all of these:**

- Wrap your main logic in a Scope block. Add a parallel Catch scope that runs on Failed/Skipped/TimedOut. Centralised error notifications without duplicating logic everywhere.
- Use generic connection references if you're packaging flows to share or move between environments. Avoids the "rewire everything" problem on import.
- Test your trigger conditions before going live. A misconfigured SharePoint trigger that fires on every column update will burn through your run history fast.

---

**If you want the full package:**

I packaged all 5 as importable JSON files with a README covering import steps, connection configuration, and common gotchas for each flow. $49 at the link below if that's useful.

https://flowtechadvisory.gumroad.com/l/m365-automation-starter-pack

Happy to answer questions on any of the above — particularly the Graph API onboarding step and the Adaptive Cards approval pattern, both of which have a few non-obvious setup requirements.
