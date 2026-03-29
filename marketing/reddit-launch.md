# Reddit Launch Posts — Flowtech Advisory

Post these on launch day, staggered 30-60 minutes apart. Lead with value. No hard sell.

---

## r/PowerAutomate

**Title:** Free tips from building 10 Power Automate workflows for construction — plus I'm sharing the templates

**Body:**

Been building Power Automate flows for construction projects for about 3 years. After rebuilding the same core workflows on every project, I finally cleaned them up and made them importable. Wanted to share some lessons first, because these cost me a lot of debugging time:

**Things I learned the hard way:**

1. **Scope blocks for error handling are non-negotiable.** The built-in "configure run after" approach gets messy on any flow with 4+ actions. Wrap your main logic in a Scope, add a parallel "Catch" scope that runs on Failed/Skipped/TimedOut. Centralized error notifications, one place to debug.

2. **Generic connection references make templates portable.** Hard-coded connections mean whoever imports your flow has to rebuild half of it. Generic refs prompt the user to map their own connections on import. Saves hours.

3. **Construction teams won't use anything that needs training.** Yellow cells for input, everything else locked. If someone has to read a manual to fill in a daily report, they'll go back to paper.

4. **The SharePoint 5000-item threshold will bite you.** If your flow queries a list that might grow past 5K items, add pagination or indexed columns now. Not later. Now.

5. **Approval flows need a fallback for when the approver is on leave.** Sounds obvious. I've seen three companies go a week without processing expense claims because the flow was waiting on someone in Bali.

---

**The templates I built:**

I packaged 10 production-ready workflows into a template pack. All Scope-based error handling, all generic connections, all construction-specific:

- Expense claim approval
- Purchase order generator
- Daily site reports
- Timesheet reminders
- Safety incident reporting
- Equipment maintenance tracking
- RFI processing
- Variation requests
- Subcontractor payment tracking
- Project completion checklists

$49 for the pack: https://flowtechadvisory.gumroad.com/l/pa-template-pack

I also wrote a Beginner's Blueprint ($39) — 45-page course covering triggers through to production deployment with ALM. Wrote it because most PA tutorials stop at "click the button" and never cover error handling or Solutions.

Full bundle with everything (including Excel templates for budgets and daily runsheets): $99 at https://flowtechadvisory.gumroad.com/l/complete-bundle

Happy to answer any questions about the flow architecture or share tips on specific patterns. Also genuinely want to know — what construction workflows are you struggling with? Might build templates for them next.

---

## r/passive_income

**Title:** Built a bundle of digital products for construction professionals — here's what I learned about the process

**Body:**

Not a "I made $50K in my first month" post. Just want to share the process honestly for anyone thinking about digital products in a niche industry.

**Background:** I'm a construction project manager in Australia. Over the past 3 years I've been building Microsoft Power Automate workflows and Excel templates for construction companies. Same problems on every project — manual expense claims, paper daily reports, budget spreadsheets nobody trusts.

**What I built:**

5 digital products, all sold on Gumroad:

1. **Power Automate Template Pack** ($49) — 10 importable workflow files for construction (expense claims, purchase orders, safety incidents, etc.)
2. **Power Automate Beginner's Blueprint** ($39) — 45-page PDF course on building automation workflows
3. **Construction Budget Dashboard** ($29) — Excel template with charts and variance tracking
4. **Expense Claim Automation Guide** ($19) — Step-by-step guide for building automated expense processing
5. **Site Daily Runsheet** ($15) — Excel template for daily site reporting

Complete bundle: $99 (save $52 vs individual).

**What I've learned so far:**

- **Niche > broad.** "Power Automate templates" is a crowded space. "Power Automate templates for construction" has almost no competition. Every product uses real construction terminology and handles industry-specific edge cases. That specificity is the moat.

- **Solve your own problems first.** Everything I'm selling started as something I built for my own projects. The daily runsheet was my actual daily runsheet. The expense flow was running on a real construction project before I turned it into a template. This means the product works in the real world, not just in a demo.

- **Bundle pricing works.** $151 individually vs $99 for all 5 makes the bundle feel like a no-brainer. People who would've bought 1-2 products end up grabbing the whole thing.

- **The product is 20% of the work.** The other 80% is Gumroad listings, screenshots, descriptions, landing pages, social media, email copy, Product Hunt prep. I underestimated this massively.

- **Price higher than you think.** I started thinking $9-15 for everything. But these save construction companies genuine money — a PM spending 10+ hrs/week on admin that a $49 template pack eliminates. The ROI math makes the price irrelevant.

No revenue numbers to share yet (just launched). Happy to answer questions about the process, the niche, or how I structured the products. Not here to sell — just want to give an honest account.

Store: https://flowtechadvisory.gumroad.com

---

## Posting Guidelines

| Subreddit | Tone | Key rule |
|-----------|------|----------|
| r/PowerAutomate | Technical, peer-to-peer | Lead with free technical tips. Products mentioned secondarily. |
| r/passive_income | Process-focused, honest | Share the journey. No income claims. No hype. |

**General rules for all Reddit posts:**
- Don't post and vanish — reply to every comment within 24 hours
- If someone asks a technical question, answer it fully even if it means they don't need to buy
- Never argue with negative comments — thank them for the feedback
- If a mod removes the post, don't repost. DM the mod and ask what to adjust
- Upvote other people's comments on your post to keep engagement visible
