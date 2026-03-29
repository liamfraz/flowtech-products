# Gumroad Product Setup Guide

Step-by-step instructions for creating each product on Gumroad, uploading the deliverable ZIP, setting the price, and linking it back to the showcase site.

## Prerequisites

- A Gumroad account (https://gumroad.com)
- Access to the `/zips/` directory in this repo

## Per-Product Setup

Repeat the following steps for each product listed below.

### 1. Power Automate Template Pack for Construction

| Field | Value |
|---|---|
| **Price** | $49 |
| **ZIP file** | `zips/power-automate-template-pack.zip` |
| **Config ID** | `power-automate-template-pack` |

### 2. Power Automate Beginner's Blueprint

| Field | Value |
|---|---|
| **Price** | $39 |
| **ZIP file** | `zips/power-automate-beginners-blueprint.zip` |
| **Config ID** | `power-automate-beginners-blueprint` |

### 3. Construction Budget Dashboard

| Field | Value |
|---|---|
| **Price** | $29 |
| **ZIP file** | `zips/construction-budget-dashboard.zip` |
| **Config ID** | `construction-budget-dashboard` |

### 4. Expense Claim Automation Guide

| Field | Value |
|---|---|
| **Price** | $19 |
| **ZIP file** | `zips/expense-claim-automation-guide.zip` |
| **Config ID** | `expense-claim-automation-guide` |

### 5. Site Daily Runsheet Template

| Field | Value |
|---|---|
| **Price** | $15 |
| **ZIP file** | `zips/site-daily-runsheet.zip` |
| **Config ID** | `site-daily-runsheet` |

## Steps for Each Product

1. **Create the product on Gumroad**
   - Go to https://app.gumroad.com/products and click **New Product**
   - Select **Digital product**
   - Enter the product name from the table above

2. **Upload the ZIP file**
   - In the product editor, click **Add content**
   - Upload the corresponding ZIP file from the `/zips/` directory
   - Add a brief description of what's included

3. **Set the price**
   - Under **Pricing**, set the price from the table above
   - Choose "Fixed price" (not "Pay what you want") unless you prefer flexible pricing

4. **Configure product details**
   - Add a cover image (use a screenshot from the showcase site or create one)
   - Write a product description (copy from `showcase/src/config/products.ts`)
   - Add relevant tags (e.g., "construction", "power automate", "templates")

5. **Publish the product**
   - Click **Publish** to make it live
   - Copy the product URL (e.g., `https://yourusername.gumroad.com/l/abc123`)

6. **Update the showcase config**
   - Open `showcase/src/config/products.ts`
   - Find the product by its `id` matching the **Config ID** in the table above
   - Replace `https://gumroad.com/l/REPLACE_ME` with the actual Gumroad URL
   - Example:
     ```ts
     gumroadUrl: "https://yourusername.gumroad.com/l/abc123",
     ```

7. **Rebuild and deploy**
   ```bash
   cd showcase
   npm run build
   ```
   Then deploy to your hosting provider (e.g., `vercel --prod`).

## Verification

After updating all 5 product URLs:

1. Run `npm run build` — should complete with zero errors
2. Run `npm run preview` — open the local URL and click each "Add to Cart" button
3. Confirm each button navigates to the correct Gumroad product page
