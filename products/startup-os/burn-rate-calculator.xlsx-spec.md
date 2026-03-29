# Burn Rate & Runway Calculator — Spreadsheet Spec

This document specifies the layout and formulas for a burn rate calculator spreadsheet. Build it in Excel or Google Sheets using the structure below.

---

## Overview

A simple, no-nonsense calculator that answers the two questions every founder loses sleep over:
1. **How fast are we spending money?** (Burn rate)
2. **When do we run out?** (Runway)

---

## Sheet 1: Monthly Inputs

### Section A: Cash Position

| Row | Field | Cell | Format | Notes |
|---|---|---|---|---|
| 1 | **Starting Cash Balance** | B2 | Currency ($) | Enter your current bank balance |
| 2 | **Date** | B3 | Date (MMM YYYY) | Month this calculation applies to |

### Section B: Monthly Revenue

| Row | Field | Cell | Format | Notes |
|---|---|---|---|---|
| 4 | **Recurring Revenue (MRR)** | B5 | Currency | Subscription / retainer income |
| 5 | **One-Time Revenue** | B6 | Currency | Project fees, consulting, etc. |
| 6 | **Other Income** | B7 | Currency | Grants, interest, affiliate income |
| 7 | **Total Monthly Revenue** | B8 | Currency | `=SUM(B5:B7)` |

### Section C: Monthly Expenses

| Row | Category | Cell | Format | Notes |
|---|---|---|---|---|
| 9 | **Salaries & Wages** | B10 | Currency | All team compensation incl. taxes |
| 10 | **Contractors & Freelancers** | B11 | Currency | Outsourced work |
| 11 | **Rent & Utilities** | B12 | Currency | Office, co-working, home office stipends |
| 12 | **Software & Tools** | B13 | Currency | SaaS subscriptions, hosting, APIs |
| 13 | **Marketing & Ads** | B14 | Currency | Paid acquisition, content, events |
| 14 | **Legal & Accounting** | B15 | Currency | Lawyers, bookkeeper, registered agent |
| 15 | **Insurance** | B16 | Currency | Liability, D&O, health (if company-paid) |
| 16 | **Travel & Meals** | B17 | Currency | Business travel, team meals |
| 17 | **Other Expenses** | B18 | Currency | Anything not covered above |
| 18 | **Total Monthly Expenses** | B19 | Currency | `=SUM(B10:B18)` |

### Section D: Calculated Metrics

| Row | Metric | Cell | Formula | Format |
|---|---|---|---|---|
| 20 | **Gross Burn** | B21 | `=B19` | Currency |
| 21 | **Net Burn** | B22 | `=B19-B8` | Currency |
| 22 | **Cash at End of Month** | B23 | `=B2-B22` | Currency |
| 23 | **Runway (Months)** | B24 | `=IF(B22<=0, "Profitable!", ROUND(B2/B22, 1))` | Number (1 decimal) |
| 24 | **Runway Date** | B25 | `=IF(B22<=0, "N/A", EDATE(B3, B24))` | Date (MMM YYYY) |

---

## Sheet 2: 12-Month Projection

### Layout

| Column | A | B | C | D | ... | M |
|---|---|---|---|---|---|---|
| Row 1 | **Category** | **Month 1** | **Month 2** | **Month 3** | ... | **Month 12** |
| Row 2 | Starting Cash | [From Sheet 1] | [=Previous End Cash] | [=Previous End Cash] | | |
| Row 3 | MRR | [Input] | [Input or growth %] | | | |
| Row 4 | One-Time Revenue | [Input] | [Input] | | | |
| Row 5 | Other Income | [Input] | [Input] | | | |
| Row 6 | **Total Revenue** | `=SUM(B3:B5)` | `=SUM(C3:C5)` | | | |
| Row 7 | | | | | | |
| Row 8 | Salaries & Wages | [Input] | [Input] | | | |
| Row 9 | Contractors | [Input] | [Input] | | | |
| Row 10 | Rent & Utilities | [Input] | [Input] | | | |
| Row 11 | Software & Tools | [Input] | [Input] | | | |
| Row 12 | Marketing & Ads | [Input] | [Input] | | | |
| Row 13 | Legal & Accounting | [Input] | [Input] | | | |
| Row 14 | Insurance | [Input] | [Input] | | | |
| Row 15 | Travel & Meals | [Input] | [Input] | | | |
| Row 16 | Other Expenses | [Input] | [Input] | | | |
| Row 17 | **Total Expenses** | `=SUM(B8:B16)` | `=SUM(C8:C16)` | | | |
| Row 18 | | | | | | |
| Row 19 | **Net Burn** | `=B17-B6` | `=C17-C6` | | | |
| Row 20 | **End Cash** | `=B2-B19` | `=C2-C19` | | | |
| Row 21 | **Cumulative Burn** | `=B19` | `=B21+C19` | | | |

### Conditional Formatting

- **End Cash row**: Green when > 6 months of burn. Yellow when 3–6 months. Red when < 3 months.
- **Net Burn row**: Green when negative (profitable). Red when positive (burning cash).

---

## Sheet 3: Scenario Planner

Three scenarios side-by-side to stress-test your assumptions.

| Metric | Conservative | Base Case | Optimistic |
|---|---|---|---|
| **MRR Growth Rate** | [e.g., 5%/mo] | [e.g., 10%/mo] | [e.g., 20%/mo] |
| **Monthly Expense Growth** | [e.g., 3%/mo] | [e.g., 2%/mo] | [e.g., 1%/mo] |
| **Starting Cash** | [Same] | [Same] | [Same] |
| **Month 6 Cash** | [Calculated] | [Calculated] | [Calculated] |
| **Month 12 Cash** | [Calculated] | [Calculated] | [Calculated] |
| **Runway (Months)** | [Calculated] | [Calculated] | [Calculated] |
| **Break-Even Month** | [Calculated] | [Calculated] | [Calculated] |

### Scenario Formulas

For each scenario column, project 12 months forward:
- `Revenue[n] = Revenue[n-1] * (1 + MRR_Growth_Rate)`
- `Expenses[n] = Expenses[n-1] * (1 + Expense_Growth_Rate)`
- `Cash[n] = Cash[n-1] - (Expenses[n] - Revenue[n])`
- `Runway = First month where Cash[n] <= 0`
- `Break-Even = First month where Revenue[n] >= Expenses[n]`

---

## Definitions

| Term | Definition |
|---|---|
| **Gross Burn** | Total monthly expenses, ignoring revenue. How much cash leaves the building each month. |
| **Net Burn** | Total expenses minus total revenue. The actual rate you're depleting cash. |
| **Runway** | Cash balance divided by net burn. How many months until you hit $0. |
| **MRR** | Monthly Recurring Revenue — predictable subscription income. |
| **Break-Even** | The month where revenue equals or exceeds expenses. Net burn drops to zero or below. |

---

## Tips for Founders

- **Update monthly.** A quarterly burn calculation is too slow — you need to see trends forming.
- **Use net burn for runway.** Gross burn overstates the problem if you have meaningful revenue.
- **Plan for the conservative scenario.** If your base case says 14 months of runway, plan as if you have 10.
- **Start fundraising at 6 months of runway.** Raising takes 3–6 months. Don't wait until you're desperate.
- **Watch expense creep.** $50/month tools add up fast. Review your software subscriptions quarterly.
- **Share with your co-founder.** Both founders should know the runway number at all times. No surprises.

---

*Part of the Startup Operating System — flowtechadvisory.gumroad.com*
