# Gumroad Upload Status

Last updated: 2026-04-13

## ZIP Files (Ready to Upload)

| # | Product | Price | ZIP File | ZIP Status | Gumroad Status |
|---|---------|-------|----------|------------|----------------|
| 1 | Power Automate Template Pack | $49 | `power-automate-template-pack-v1.zip` | ✅ Ready (11 files, 88KB) | ⏳ PENDING UPLOAD |
| 2 | Power Automate Beginner's Blueprint | $39 | `power-automate-beginners-blueprint-v1.zip` | ✅ Ready (PDF + README, 34KB) | ⏳ PENDING UPLOAD |
| 3 | Construction Budget Dashboard | $29 | `construction-budget-dashboard-v1.zip` | ✅ Ready (XLSX + README, 13KB) | ⏳ PENDING UPLOAD |

## Blocker: Gumroad Account Does Not Exist

**`flowtechadvisory.gumroad.com` returns 404.** No Gumroad account exists at this username.

To unblock uploads, Liam must:

1. Go to https://gumroad.com and create an account (or log in)
2. Set the profile username to `flowtechadvisory` (Settings → Profile)
3. Run the upload script below OR complete uploads manually

## Upload Script (run after logging in)

Once logged in with Playwright session available, run:

```bash
node showcase/scripts/gumroad-upload.js
```

## Manual Upload Steps (Gumroad dashboard)

For each product:
1. Go to https://app.gumroad.com/products → New Product → Digital Product
2. Set name, price, and upload the ZIP from `showcase/zips/`
3. Use the planned URL slugs (Settings → Permalink):
   - Template Pack → `pa-template-pack`
   - Blueprint → `pa-blueprint`
   - Budget Dashboard → `budget-dashboard`
4. Publish → copy URL → update `showcase/src/config/products.ts`

## Gumroad URLs (planned — update after publishing)

```
https://flowtechadvisory.gumroad.com/l/pa-template-pack     ($49)
https://flowtechadvisory.gumroad.com/l/pa-blueprint          ($39)
https://flowtechadvisory.gumroad.com/l/budget-dashboard      ($29)
```

## After Uploading

Update this file with status: `✅ UPLOADED` and run:

```bash
cd showcase && npm run build && npx vercel --prod
```
