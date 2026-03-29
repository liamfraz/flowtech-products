# Cross-Promotion Strategy: FlowGen <> Flowtech Products

## Overview

Two revenue streams that share the same target audience (construction professionals using Microsoft 365):
- **FlowGen** — AI-powered flow generation tool/service
- **Flowtech Products** — Digital templates, guides, and workflow packs on Gumroad

Cross-promotion turns each customer into a lead for the other product line.

---

## 1. FlowGen Users → Products Email List

### In-App Prompts
- After a user generates their first flow in FlowGen, show a banner:
  > "Need pre-built workflows? Get 10 production-ready Power Automate templates for construction — $49 on Gumroad."
- After a user generates an expense-related flow, surface the Expense Claim Automation Guide ($19)
- After any flow generation, offer the Beginner's Blueprint if the user's flow has common mistakes (missing error handling, no Scope blocks)

### Email Sequences
- **Welcome email** (Day 0): Mention the Products store in the footer — "Also available: ready-made templates on our Gumroad store"
- **Day 3 email**: "Getting started? Our Beginner's Blueprint covers everything from triggers to production deployment" — link to Gumroad
- **Day 7 email**: "Save time — import 10 pre-built construction workflows instead of building from scratch" — link to Template Pack
- **Monthly newsletter**: Feature one product per month with a use case story

### Discount Codes
- FlowGen users get a **15% discount code** for any Gumroad product (e.g., `FLOWGEN15`)
- Create this in Gumroad: Settings > Discount Codes > Create

---

## 2. Products Buyers → FlowGen Trial

### Gumroad Post-Purchase Emails
Configure Gumroad's post-purchase workflow email for each product:

| Product Purchased | FlowGen CTA in Email |
|---|---|
| Template Pack | "Want custom workflows beyond these 10? Try FlowGen — AI-generated Power Automate flows in minutes" |
| Beginner's Blueprint | "Ready to build your own? FlowGen generates production-ready flows from plain English descriptions" |
| Budget Dashboard | "Automate your budget data entry — FlowGen can build a Power Automate flow that populates this dashboard from SharePoint" |
| Expense Guide | "Skip the manual setup — FlowGen can generate the entire expense approval flow described in Chapter 3" |
| Daily Runsheet | "Auto-fill your runsheet from a mobile form — FlowGen builds the Power Automate connector in seconds" |

### PDF/Guide Inserts
Add a final page or section to each PDF/guide:
> **Build Custom Flows with AI**
> FlowGen by Flowtech Advisory generates production-ready Power Automate workflows from plain English.
> Try it free: [FlowGen URL]

### README Inserts (Template Pack)
Add to the workflows README.md:
```
## Need Custom Workflows?
These 10 templates cover common construction scenarios. For anything custom,
try FlowGen — describe what you need in plain English and get a ready-to-import
Power Automate flow in minutes.
→ [FlowGen URL]
```

---

## 3. Bundle Cross-Sell

### On the Showcase Landing Page
- Add a "Complete Bundle" card ($99, save $52) prominently — already added to products config
- Below the product grid, add a section: "Use FlowGen to customize any template"

### On the Gumroad Profile
- Pin the Complete Bundle as the featured product
- In the bundle description, mention FlowGen for customization

---

## 4. Content Marketing Flywheel

### LinkedIn Strategy (Weekly Posts)
- **Week 1**: Share a tip from the Beginner's Blueprint → link to Gumroad
- **Week 2**: Show a FlowGen demo (generate a flow in 30 seconds) → link to FlowGen
- **Week 3**: Share a budget dashboard screenshot with a construction use case → link to Gumroad
- **Week 4**: Customer story / case study combining FlowGen + templates

### YouTube / Video Content
- Demo videos (already scripted in `/marketing/video-scripts/`) each end with a Gumroad CTA
- Add FlowGen mentions to video descriptions: "Build custom versions of these workflows with FlowGen"
- Create a "FlowGen + Template Pack" combo video showing the full workflow

### SEO / Blog
- Write articles targeting "Power Automate construction templates" → links to Gumroad
- Write articles targeting "AI Power Automate generator" → links to FlowGen
- Internal cross-links between all content

---

## 5. Referral Program

### Products → Products
- Gumroad's built-in affiliate program: enable 20% commission for referrals
- Encourage buyers to share with colleagues

### FlowGen → Products
- FlowGen power users who refer 3+ colleagues get the Complete Bundle free (coupon code)

### Products → FlowGen
- Bundle buyers get 1 month FlowGen Pro free (if applicable)

---

## 6. Metrics to Track

| Metric | Source | Target |
|---|---|---|
| Gumroad sales from FlowGen referrals | UTM: `?utm_source=flowgen` | 10% of FlowGen users convert |
| FlowGen signups from Gumroad | UTM: `?utm_source=gumroad` | 5% of buyers try FlowGen |
| Bundle conversion rate | Gumroad analytics | 20% of product views → bundle purchase |
| Discount code redemptions | Gumroad: `FLOWGEN15` usage | Track monthly |
| Email click-through rates | Gumroad / email provider | >3% CTR on cross-sell links |

---

## Implementation Priority

1. **Now** (before Gumroad launch): Add FlowGen mention to showcase landing page footer
2. **At launch**: Configure Gumroad post-purchase emails with FlowGen CTAs
3. **Week 1**: Create FLOWGEN15 discount code, add to FlowGen welcome email
4. **Week 2**: Update PDF guides with FlowGen final page insert
5. **Month 1**: Start LinkedIn content flywheel
6. **Month 2**: Enable Gumroad affiliate program, launch referral incentives
