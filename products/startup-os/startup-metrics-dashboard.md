# Startup Metrics Dashboard

The essential SaaS metrics every founder needs to track, explained in plain English with formulas and a tracking template. Stop guessing — measure what matters.

---

## Quick Reference: The 7 Metrics That Matter

| Metric | What It Tells You | Formula | Healthy Range |
|---|---|---|---|
| **MRR** | How much predictable revenue you earn monthly | Sum of all recurring subscription revenue | Growing 10–20%/month (early stage) |
| **Churn Rate** | How fast you're losing customers | Lost customers / Start-of-month customers | < 5% monthly (< 2% is great) |
| **CAC** | How much it costs to acquire one customer | Total sales + marketing spend / New customers | Depends on LTV (see LTV:CAC) |
| **LTV** | Total revenue a customer generates over their lifetime | ARPU / Monthly churn rate | LTV:CAC ratio > 3:1 |
| **NPS** | How likely customers are to recommend you | % Promoters - % Detractors | > 30 is good, > 50 is excellent |
| **ARPU** | Average revenue per user per month | MRR / Total active customers | Increasing over time |
| **MoM Growth** | Month-over-month revenue growth rate | (This month MRR - Last month MRR) / Last month MRR | 10–20% early stage, 5–10% at scale |

---

## Metric 1: MRR (Monthly Recurring Revenue)

### What It Is
The total predictable revenue you earn each month from subscriptions. This is the heartbeat of any SaaS business.

### How to Calculate

```
MRR = Sum of all active subscription amounts (normalised to monthly)
```

**Breakdown:**

| Component | Formula | Example |
|---|---|---|
| **New MRR** | Revenue from new customers this month | 12 new customers × $49 = $588 |
| **Expansion MRR** | Revenue from upgrades / add-ons | 5 customers upgraded, +$25 avg = $125 |
| **Churned MRR** | Revenue lost from cancellations | 3 customers cancelled, -$49 avg = -$147 |
| **Contraction MRR** | Revenue lost from downgrades | 2 customers downgraded, -$20 avg = -$40 |
| **Net New MRR** | New + Expansion - Churned - Contraction | $588 + $125 - $147 - $40 = **$526** |

### Tracking Template

| Month | Starting MRR | New MRR | Expansion | Churned | Contraction | Net New | Ending MRR |
|---|---|---|---|---|---|---|---|
| Jan 2025 | $8,200 | $588 | $125 | -$147 | -$40 | $526 | $8,726 |
| Feb 2025 | $8,726 | | | | | | |
| Mar 2025 | | | | | | | |
| Apr 2025 | | | | | | | |
| May 2025 | | | | | | | |
| Jun 2025 | | | | | | | |

---

## Metric 2: Churn Rate

### What It Is
The percentage of customers (or revenue) you lose each month. High churn is a leaky bucket — no amount of acquisition fixes it.

### How to Calculate

```
Customer Churn Rate = (Customers lost this month / Customers at start of month) × 100

Revenue Churn Rate = (MRR lost this month / MRR at start of month) × 100
```

**Track both.** You can lose 10 customers but if they were all on the cheapest plan, your revenue churn might be low. Conversely, losing 2 enterprise customers can devastate revenue churn.

### Benchmarks

| Churn Rate | Verdict |
|---|---|
| < 2% monthly | Excellent — strong product-market fit |
| 2–5% monthly | Acceptable — normal for early stage |
| 5–8% monthly | Concerning — investigate why customers leave |
| > 8% monthly | Critical — fix this before anything else |

### Tracking Template

| Month | Starting Customers | Lost Customers | Churn Rate | Starting MRR | Churned MRR | Revenue Churn |
|---|---|---|---|---|---|---|
| Jan 2025 | 168 | 5 | 2.98% | $8,200 | $195 | 2.38% |
| Feb 2025 | | | | | | |
| Mar 2025 | | | | | | |

---

## Metric 3: CAC (Customer Acquisition Cost)

### What It Is
How much you spend to acquire one new customer. Includes all sales and marketing costs.

### How to Calculate

```
CAC = (Total sales + marketing spend in period) / New customers acquired in period
```

**Include everything:** Ad spend, content creation costs, sales team salaries, tools (CRM, email marketing), event sponsorships, affiliate payouts.

### Example

| Line Item | Monthly Cost |
|---|---|
| Google Ads | $1,200 |
| Content writer (freelance) | $800 |
| Email marketing tool | $100 |
| Sales team (1 person, allocated) | $3,000 |
| **Total** | **$5,100** |
| New customers this month | 34 |
| **CAC** | **$150** |

### Tracking Template

| Month | Marketing Spend | Sales Spend | Total S&M | New Customers | CAC |
|---|---|---|---|---|---|
| Jan 2025 | $2,100 | $3,000 | $5,100 | 34 | $150 |
| Feb 2025 | | | | | |
| Mar 2025 | | | | | |

---

## Metric 4: LTV (Customer Lifetime Value)

### What It Is
The total revenue you can expect from a customer over their entire relationship with you.

### How to Calculate

```
LTV = ARPU / Monthly churn rate

-- or --

LTV = ARPU × Average customer lifespan (in months)
```

### The LTV:CAC Ratio

This is the most important ratio in SaaS.

| Ratio | Meaning |
|---|---|
| **< 1:1** | You're losing money on every customer. Stop spending on acquisition. |
| **1:1 – 3:1** | Unprofitable or barely breaking even. Improve retention or reduce CAC. |
| **3:1 – 5:1** | Healthy. You're generating good returns on acquisition spend. |
| **> 5:1** | You might be under-investing in growth. Spend more to grow faster. |

### Example

```
ARPU = $49/month
Monthly churn = 4%
LTV = $49 / 0.04 = $1,225

CAC = $150
LTV:CAC = $1,225 / $150 = 8.2:1 (excellent — could invest more in growth)
```

### Tracking Template

| Month | ARPU | Monthly Churn | LTV | CAC | LTV:CAC |
|---|---|---|---|---|---|
| Jan 2025 | $49 | 4.0% | $1,225 | $150 | 8.2:1 |
| Feb 2025 | | | | | |
| Mar 2025 | | | | | |

---

## Metric 5: NPS (Net Promoter Score)

### What It Is
A measure of customer satisfaction and loyalty. Based on one question: "How likely are you to recommend [Product] to a friend or colleague?" (0–10 scale).

### How to Calculate

```
Categorise responses:
  Promoters = 9–10
  Passives = 7–8
  Detractors = 0–6

NPS = (% Promoters) - (% Detractors)
```

NPS ranges from -100 to +100.

### Benchmarks

| NPS | Verdict |
|---|---|
| > 50 | Excellent — customers love you and refer others |
| 30–50 | Good — solid satisfaction, room to improve |
| 0–30 | Average — functional but not memorable |
| < 0 | Problem — more detractors than promoters |

### Survey Template

Send this quarterly or after key milestones (onboarding complete, 3 months active, etc.):

1. **On a scale of 0–10, how likely are you to recommend [Product] to a friend or colleague?**
2. **What's the primary reason for your score?** (Open text)
3. **What's one thing we could do to improve your experience?** (Open text)

### Tracking Template

| Survey Date | Responses | Promoters | Passives | Detractors | NPS |
|---|---|---|---|---|---|
| Jan 2025 | 84 | 42 (50%) | 28 (33%) | 14 (17%) | +33 |
| Apr 2025 | | | | | |
| Jul 2025 | | | | | |

---

## Metric 6: ARPU (Average Revenue Per User)

### How to Calculate

```
ARPU = MRR / Total active customers
```

### Why It Matters

ARPU tells you whether you're moving upmarket (higher ARPU = bigger customers, higher LTV) or downmarket. Track it alongside customer count — growing customers but shrinking ARPU means you're attracting lower-value segments.

---

## Metric 7: MoM Growth Rate

### How to Calculate

```
MoM Growth = (This month MRR - Last month MRR) / Last month MRR × 100
```

### Benchmarks (Early Stage)

| Growth Rate | Verdict |
|---|---|
| > 20%/month | Exceptional — you may be onto something big |
| 10–20%/month | Strong — typical of good early-stage SaaS |
| 5–10%/month | Moderate — fine at scale, slow for early stage |
| < 5%/month | Stalling — investigate product-market fit |

---

## Combined Monthly Dashboard

Use this single table to track all metrics in one place.

| Metric | Jan | Feb | Mar | Apr | May | Jun |
|---|---|---|---|---|---|---|
| **MRR** | | | | | | |
| **Net New MRR** | | | | | | |
| **MoM Growth** | | | | | | |
| **Total Customers** | | | | | | |
| **New Customers** | | | | | | |
| **Churned Customers** | | | | | | |
| **Customer Churn %** | | | | | | |
| **Revenue Churn %** | | | | | | |
| **ARPU** | | | | | | |
| **CAC** | | | | | | |
| **LTV** | | | | | | |
| **LTV:CAC** | | | | | | |
| **NPS** | — | — | — | | — | — |
| **Burn Rate** | | | | | | |
| **Runway (months)** | | | | | | |

---

## Tips for Founders

- **Start tracking MRR and churn from day one.** Even with 5 customers, the habit matters more than the numbers.
- **Don't cherry-pick metrics.** Report the ones that look bad alongside the ones that look good.
- **Cohort analysis > averages.** Your January cohort might churn at 2% while your March cohort churns at 12%. The average hides this.
- **Review weekly, report monthly.** Check your dashboard every Monday. Send a formal update to stakeholders monthly.
- **Automate collection.** Stripe, ChartMogul, Baremetrics, or even a simple spreadsheet with manual entry. Just make it easy to update.
- **LTV:CAC is your north star ratio.** If it's below 3:1, you either need to reduce churn, increase prices, or lower acquisition costs.

---

*Part of the Startup Operating System — flowtechadvisory.gumroad.com*
