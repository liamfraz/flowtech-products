# Purchase Flow Fix — All Links Broken

**Verified:** 2026-03-28 via Playwright automated testing
**Showcase site:** https://showcase-lemon-rho.vercel.app
**Status:** ALL purchase buttons return Gumroad 404 — no products can be purchased

---

## Root Cause

The Gumroad store **does not exist yet**. The profile page `https://flowtechadvisory.gumroad.com` itself returns 404, meaning:

1. No Gumroad account has been set up with the username `flowtechadvisory`, OR
2. The account exists but has no published products and no public profile

All URLs in the codebase are **planned slugs** with `// TODO: replace with actual Gumroad URL` comments. They were never replaced because the products were never listed.

---

## Broken Links (8 total)

### Showcase Site (React app — `showcase/src/config/products.ts`)

| # | Product | Price | Planned URL | Status |
|---|---------|-------|-------------|--------|
| 1 | Power Automate Template Pack | $49 | `flowtechadvisory.gumroad.com/l/pa-template-pack` | 404 |
| 2 | Power Automate Beginner's Blueprint | $39 | `flowtechadvisory.gumroad.com/l/pa-blueprint` | 404 |
| 3 | Construction Budget Dashboard | $29 | `flowtechadvisory.gumroad.com/l/budget-dashboard` | 404 |
| 4 | Expense Claim Automation Guide | $19 | `flowtechadvisory.gumroad.com/l/expense-automation` | 404 |
| 5 | Site Daily Runsheet Template | $15 | `flowtechadvisory.gumroad.com/l/daily-runsheet` | 404 |
| 6 | Freelancer Client Onboarding Kit | $19 | `flowtechadvisory.gumroad.com/l/freelancer-onboarding-kit` | 404 |
| 7 | Startup Operating System | $29 | `flowtechadvisory.gumroad.com/l/startup-os` | 404 |
| 8 | Complete Bundle | $129 | `flowtechadvisory.gumroad.com/l/complete-bundle` | 404 |

### Static Launch Page (`showcase/public/launch/index.html`)

Same 6 URLs hardcoded (products 1-5 + bundle). This page also 404s on Vercel — it was never deployed.

### Marketing Materials (not customer-facing, but will need updating)

Files referencing the same planned URLs:
- `marketing/social-posts.md`
- `marketing/twitter-launch.md`
- `marketing/reddit-launch.md`
- `marketing/product-hunt-final.md`
- `marketing/product-hunt/submission-draft.md`

---

## Additional Issue: Deployed vs Local Mismatch

The **live Vercel site** only shows 5 products (Template Pack, Blueprint, Budget Dashboard, Expense Guide, Runsheet) + the bundle. The **local codebase** has 7 products (adds Freelancer Onboarding Kit and Startup Operating System). The site needs a redeploy after fixing URLs.

---

## What Liam Needs to Do

### Step 1: Create the Gumroad Account & Products

1. Go to [gumroad.com](https://gumroad.com) and create an account (or log in)
2. Set your username/subdomain to `flowtechadvisory` (Settings → Profile)
3. Create each product using the detailed instructions in `UPLOAD-GUIDE.md`
4. For each product:
   - Upload the ZIP file from `zips/` directory
   - Set the price as listed above
   - Set a custom URL slug (Gumroad lets you choose — use the planned slugs if available)
   - Publish the product

### Step 2: Get the Actual Gumroad URLs

After creating each product, Gumroad assigns a URL. Two scenarios:

**If you can use custom slugs** (Gumroad allows this):
- The planned URLs should work as-is — just publish and verify

**If Gumroad assigns different slugs:**
- Copy each product's actual URL from the Gumroad dashboard
- URL format: `https://flowtechadvisory.gumroad.com/l/<SLUG>`

### Step 3: Update the Codebase

1. Edit `showcase/src/config/products.ts`:
   - Replace each `gumroadUrl` value with the real URL from Gumroad
   - Remove the `// TODO: replace with actual Gumroad URL` comments
2. Edit `showcase/public/launch/index.html`:
   - Update all 6 hardcoded `href` values
3. Update marketing files if the slugs differ from planned

### Step 4: Redeploy

```bash
cd showcase
npm run build
# Deploy to Vercel (or push to trigger auto-deploy)
```

### Step 5: Verify

After deploy, click every "Buy on Gumroad" button on the live site and confirm:
- Each link opens the correct Gumroad product page
- The product name and price match
- The Gumroad overlay checkout works (the site loads `gumroad.js` for in-page checkout)

---

## Gumroad URL Format Reference

```
https://<USERNAME>.gumroad.com/l/<PRODUCT_SLUG>
```

- `USERNAME`: Your Gumroad profile name (planned: `flowtechadvisory`)
- `PRODUCT_SLUG`: Either auto-generated or custom-set per product
- Gumroad also supports short URLs: `https://gumroad.com/l/<SLUG>` (but these don't include overlay checkout)

---

## Evidence

Screenshots saved during verification:
- `/tmp/showcase_full.png` — Showcase site renders correctly, all 5 product cards + bundle visible
- `/tmp/purchase_test_0.png` through `_5.png` — All 6 buy buttons lead to Gumroad "Page not found" 404
- `/tmp/gumroad_profile.png` — The `flowtechadvisory.gumroad.com` profile itself is 404
- `/tmp/launch_page.png` — Static launch page 404s on Vercel (not deployed)
