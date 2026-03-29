# Gumroad Upload Guide

Step-by-step instructions for listing all 5 digital products on Gumroad.

## Step 1: Create a Free Gumroad Account

1. Go to [gumroad.com](https://gumroad.com)
2. Click "Start Selling"
3. Sign up with your email or Google account
4. Complete your profile:
   - Display name: **Flowtech Advisory**
   - Bio: "Construction automation templates and guides built with Microsoft Power Platform"
   - Profile picture: Use the FT logo or a professional headshot

## Step 2: Set Up Your Payment

1. Go to Settings > Payments
2. Connect your bank account or PayPal
3. Set your payout schedule (weekly recommended)

## Step 3: Create Each Product Listing

### Product 1: Power Automate Template Pack for Construction — $49

1. Click "New Product"
2. **Name:** Power Automate Template Pack for Construction
3. **Price:** $49
4. **Description:**
   > 10 ready-to-import Power Automate workflow templates built for the construction industry.
   > Includes: expense claim approval, purchase order generator, daily site reports, timesheet reminders,
   > safety incident reporting, equipment maintenance tracking, RFI processing, variation requests,
   > subcontractor payment tracking, and project completion checklists.
   >
   > Every workflow includes error handling with Scope blocks and generic connection references that
   > work in any Microsoft 365 environment. Detailed README with import instructions included.
5. **File:** Create a ZIP of the entire `workflows/` directory (all 10 JSON files + README.md)
6. **Cover image:** Create a professional graphic (1280x720) showing workflow diagrams
7. **Tags:** power-automate, construction, workflow, automation, microsoft-365
8. **Category:** Software

### Product 2: Power Automate Beginner's Blueprint — $39

1. Click "New Product"
2. **Name:** Power Automate Beginner's Blueprint
3. **Price:** $39
4. **Description:**
   > From Zero to Automated — Master Power Automate in 8 Modules.
   > A comprehensive 45+ page PDF course covering everything from your first flow to
   > production deployment. Includes triggers, actions, connectors, expressions, variables,
   > conditions, loops, error handling, and ALM best practices.
   >
   > Each module includes learning objectives, practical examples, expression reference tables,
   > and hands-on exercises.
5. **File:** Upload `guides/power-automate-beginners-blueprint.pdf`
6. **Tags:** power-automate, course, beginners, tutorial, automation
7. **Category:** eBooks

### Product 3: Construction Budget Dashboard — $29

1. Click "New Product"
2. **Name:** Construction Budget Dashboard (Excel Template)
3. **Price:** $29
4. **Description:**
   > Professional Excel dashboard for tracking construction project budgets.
   > Includes a project summary dashboard with Budget vs Actual charts, monthly cost breakdown
   > by 6 categories (Labour, Materials, Equipment, Subcontractors, Overheads, Contingency),
   > conditional formatting, and auto-calculating variance formulas.
   >
   > Works in Excel Desktop and Excel Online. Print-ready with professional formatting.
5. **File:** Upload `templates/construction-budget-dashboard.xlsx`
6. **Tags:** excel, construction, budget, dashboard, template
7. **Category:** Templates

### Product 4: Expense Claim Automation Guide — $19

1. Click "New Product"
2. **Name:** Expense Claim Automation Guide
3. **Price:** $19
4. **Description:**
   > A step-by-step guide to automating expense claims with Power Automate and AI Builder.
   > Covers the full process: AI Builder receipt scanning, flow construction, approval routing
   > by amount thresholds, Office Scripts integration for Excel reporting, testing scenarios,
   > and deployment checklists.
   >
   > Includes expression reference tables and troubleshooting FAQ.
5. **File:** Upload `guides/expense-claim-automation-guide.pdf`
6. **Tags:** power-automate, expense, automation, ai-builder, construction
7. **Category:** eBooks

### Product 5: Site Daily Runsheet Template — $15

1. Click "New Product"
2. **Name:** Site Daily Runsheet Template (Excel)
3. **Price:** $15
4. **Description:**
   > Professional A4 landscape Excel template for capturing daily construction site activities.
   > 6 structured sections: Personnel On-Site, Plant & Equipment, Work Completed,
   > Safety Observations, Delays/Issues, and Materials Delivered.
   >
   > Includes auto-calculating hours and variance formulas, print-ready formatting,
   > yellow input cells for easy data entry, and sign-off section. Instructions sheet included.
5. **File:** Upload `templates/site-daily-runsheet.xlsx`
6. **Tags:** construction, daily-report, runsheet, site-management, excel
7. **Category:** Templates

## Step 4: Product Settings (All Products)

For each product, also configure:

- **Refund policy:** 30-day money-back guarantee
- **Content rating:** Everyone
- **Discover:** Enable (allows Gumroad to feature your product)
- **Workflow emails:** Enable post-purchase email with download instructions

## Step 5: Custom Domain (Optional)

1. Go to Settings > Custom Domain
2. Add a CNAME record pointing your subdomain to `gumroad.com`:
   - Type: CNAME
   - Name: `store` (or `shop`)
   - Value: `gumroad.com`
3. Enter your custom domain in Gumroad: `store.flowtechadvisory.com`
4. Wait for DNS propagation (up to 48 hours)

## Step 6: Promote Your Products

### Gumroad Profile
- Complete your profile with a professional bio and photo
- Pin your best-selling product to the top

### Landing Page
- Deploy the showcase site (`showcase/dist/`) to Vercel, Netlify, or your own hosting
- Update the "Buy on Gumroad" button hrefs with actual Gumroad product URLs

### Social Media
- Share product links on LinkedIn (target construction professionals)
- Post in Power Automate community forums and subreddits
- Create short demo videos showing the templates in action

### Email Marketing
- Set up a Gumroad email list
- Offer a free mini-template as a lead magnet
- Send monthly tips about Power Automate in construction

### Bundle Discounts
- Create a "Complete Bundle" product on Gumroad (see Product 6 below)
- Suggested bundle price: $99 (save $52)

### Product 6: Complete Construction Automation Bundle — $99

1. Click "New Product"
2. **Name:** Complete Construction Automation Bundle
3. **Price:** $99 (original value $151 — save $52)
4. **Description:**
   > Get everything you need to automate your construction operations in one package.
   >
   > Includes all 5 Flowtech Advisory products:
   > - Power Automate Template Pack (10 workflows) — worth $49
   > - Power Automate Beginner's Blueprint (45+ page course) — worth $39
   > - Construction Budget Dashboard (Excel) — worth $29
   > - Expense Claim Automation Guide (PDF) — worth $19
   > - Site Daily Runsheet Template (Excel) — worth $15
   >
   > Save $52 compared to buying individually. Perfect for teams getting started with
   > construction automation on Microsoft 365.
5. **File:** Upload `zips/complete-bundle.zip`
6. **Tags:** construction, automation, power-automate, bundle, microsoft-365
7. **Category:** Software

## Step 7: Update the Showcase Landing Page

After publishing all products on Gumroad, update the showcase config:

1. Open `showcase/src/config/products.ts`
2. Replace each `"https://gumroad.com/l/REPLACE_ME"` with the actual Gumroad URL
   - You'll find the URL on each product's Gumroad page (e.g., `https://yourusername.gumroad.com/l/abc123`)
3. Rebuild and deploy:
   ```bash
   cd showcase
   npm run build
   npx vercel --prod
   ```
4. Verify all "Buy on Gumroad" buttons on the live site link to the correct products

## File Checklist

Before uploading, verify all files exist and are non-empty:

| Product | Upload File | Source | Format |
|---|---|---|---|
| Workflow Templates | `zips/power-automate-template-pack.zip` | 10 JSON + README | .zip |
| Beginner's Blueprint | `zips/power-automate-beginners-blueprint.zip` | PDF guide | .zip |
| Budget Dashboard | `zips/construction-budget-dashboard.zip` | Excel template | .zip |
| Expense Guide | `zips/expense-claim-automation-guide.zip` | PDF guide | .zip |
| Daily Runsheet | `zips/site-daily-runsheet.zip` | Excel template | .zip |
| Complete Bundle | `zips/complete-bundle.zip` | All 5 products | .zip |

## Thumbnail Checklist

Each product needs a cover image (1280x720 recommended). Create these before uploading:

| Product | Suggested Thumbnail |
|---|---|
| Template Pack | Workflow diagram with connected nodes, "10 Workflows" text |
| Blueprint | Open book/PDF icon with "8 Modules" text |
| Budget Dashboard | Bar chart with green/red variance, "Budget vs Actual" text |
| Expense Guide | Receipt icon with AI scanning visual, "Automate Claims" text |
| Daily Runsheet | Clipboard/form icon with checkmarks, "Site Reporting" text |
| Complete Bundle | All 5 icons combined, "Save $52" badge |

Use Canva or Figma with the Flowtech brand colors (dark background, orange #F97316 accents, white text).
