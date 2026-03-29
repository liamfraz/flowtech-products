export interface Product {
  id: string;
  name: string;
  price: string;
  originalPrice?: string;
  description: string;
  features: string[];
  badge: string | null;
  gumroadUrl: string;
  zipFile: string;
}

// TODO: Replace each gumroadUrl with your actual Gumroad product URL
// Format: https://YOURUSERNAME.gumroad.com/l/PRODUCT_SHORT_CODE
// The Gumroad overlay script will auto-intercept these links for in-page checkout
export const products: Product[] = [
  {
    id: "power-automate-template-pack",
    name: "Power Automate Template Pack for Construction",
    price: "$49",
    description:
      "10 ready-to-import Power Automate workflow templates built specifically for construction companies. Covers expense claims, purchase orders, safety incidents, RFIs, and more.",
    features: [
      "10 fully configured workflow JSON files",
      "Error handling with Scope blocks on every flow",
      "Generic connection references (works in any environment)",
      "Detailed README with import instructions",
      "Covers: Approvals, Notifications, Reporting, Tracking",
    ],
    badge: "Best Seller",
    gumroadUrl: "https://flowtechadvisory.gumroad.com/l/pa-template-pack", // TODO: replace with actual Gumroad URL
    zipFile: "power-automate-template-pack.zip",
  },
  {
    id: "power-automate-beginners-blueprint",
    name: "Power Automate Beginner's Blueprint",
    price: "$39",
    description:
      "A comprehensive 45+ page PDF course that takes you from zero to building production-ready Power Automate flows in 8 structured modules.",
    features: [
      "8 modules covering triggers to production deployment",
      "Hands-on exercises in every module",
      "Expression reference tables",
      "Error handling patterns (try/catch with Scopes)",
      "ALM and Solutions best practices",
    ],
    badge: "New",
    gumroadUrl: "https://flowtechadvisory.gumroad.com/l/pa-blueprint", // TODO: replace with actual Gumroad URL
    zipFile: "power-automate-beginners-blueprint.zip",
  },
  {
    id: "construction-budget-dashboard",
    name: "Construction Budget Dashboard",
    price: "$29",
    description:
      "Professional Excel dashboard for tracking project budgets, cost breakdowns by category, and variance analysis. Pre-built with formulas and charts.",
    features: [
      "Dashboard with Budget vs Actual charts",
      "Monthly cost breakdown by 6 categories",
      "Conditional formatting (green/red variance)",
      "SUM formulas and percentage calculations",
      "Print-ready with professional formatting",
    ],
    badge: null,
    gumroadUrl: "https://flowtechadvisory.gumroad.com/l/budget-dashboard", // TODO: replace with actual Gumroad URL
    zipFile: "construction-budget-dashboard.zip",
  },
  {
    id: "expense-claim-automation-guide",
    name: "Expense Claim Automation Guide",
    price: "$19",
    description:
      "Step-by-step guide to building an automated expense claim system using Power Automate, AI Builder for receipt scanning, and Excel reporting.",
    features: [
      "AI Builder receipt processing setup",
      "Full flow construction walkthrough",
      "Office Scripts integration for Excel",
      "Approval routing by amount thresholds",
      "Testing scenarios and deployment checklist",
    ],
    badge: null,
    gumroadUrl: "https://flowtechadvisory.gumroad.com/l/expense-automation", // TODO: replace with actual Gumroad URL
    zipFile: "expense-claim-automation-guide.zip",
  },
  {
    id: "site-daily-runsheet",
    name: "Site Daily Runsheet Template",
    price: "$15",
    description:
      "Professional A4 landscape Excel template for capturing daily site activities. Covers personnel, equipment, work completed, safety, delays, and deliveries.",
    features: [
      "6 structured sections for complete daily reporting",
      "Print-ready A4 landscape format",
      "Yellow input cells for easy data entry",
      "Auto-calculating hours and variance formulas",
      "Sign-off section for site manager",
    ],
    badge: "Popular",
    gumroadUrl: "https://flowtechadvisory.gumroad.com/l/daily-runsheet", // TODO: replace with actual Gumroad URL
    zipFile: "site-daily-runsheet.zip",
  },
  {
    id: "freelancer-onboarding-kit",
    name: "Freelancer Client Onboarding Kit",
    price: "$19",
    description:
      "6-template bundle for freelancers who want a professional client intake process. Covers questionnaire, proposal, contract, welcome emails, project brief, and invoice.",
    features: [
      "25-question client intake questionnaire",
      "Professional proposal template with pricing table",
      "Freelance service agreement (contract)",
      "3 onboarding email templates for the first 48 hours",
      "Structured project brief + invoice template",
    ],
    badge: "New",
    gumroadUrl: "https://flowtechadvisory.gumroad.com/l/freelancer-onboarding-kit", // TODO: replace with actual Gumroad URL
    zipFile: "freelancer-onboarding-kit.zip",
  },
  {
    id: "startup-os",
    name: "Startup Operating System",
    price: "$29",
    description:
      "7-template operating system for early-stage founders. Covers weekly standups, OKRs, hiring pipeline, investor updates, product roadmaps, burn rate calculations, and SaaS metrics tracking.",
    features: [
      "Weekly standup template with facilitation rules",
      "Quarterly OKR tracking at company, team & individual levels",
      "Hiring pipeline: job description, scorecard & offer letter",
      "Monthly investor update with metrics dashboard",
      "Product roadmap with impact/effort scoring matrix",
      "Burn rate & runway calculator specification",
      "7 key SaaS metrics explained with tracking templates",
    ],
    badge: "New",
    gumroadUrl: "https://flowtechadvisory.gumroad.com/l/startup-os", // TODO: replace with actual Gumroad URL
    zipFile: "startup-os.zip",
  },
];

export const bundleProduct: Product = {
  id: "complete-bundle",
  name: "Complete Automation & Templates Bundle",
  price: "$129",
  originalPrice: "$199",
  description:
    "Get all 7 products in one package — 10 Power Automate workflows, the Beginner's Blueprint course, Budget Dashboard, Expense Guide, Daily Runsheet, the Freelancer Onboarding Kit, and the Startup Operating System. Save $70.",
  features: [
    "All 10 Power Automate workflow templates",
    "45+ page Beginner's Blueprint PDF course",
    "Construction Budget Dashboard (Excel)",
    "Expense Claim Automation Guide (PDF)",
    "Site Daily Runsheet Template (Excel)",
    "Freelancer Client Onboarding Kit (6 templates)",
    "Startup Operating System (7 templates)",
  ],
  badge: "Best Value",
  gumroadUrl: "https://flowtechadvisory.gumroad.com/l/complete-bundle", // TODO: replace with actual Gumroad URL
  zipFile: "complete-bundle.zip",
};
