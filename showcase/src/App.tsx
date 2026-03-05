import { ProductCard } from "./components/ProductCard";
import { Testimonials } from "./components/Testimonials";
import { FAQ } from "./components/FAQ";
import { Hero } from "./components/Hero";
import { Footer } from "./components/Footer";

export default function App() {
  return (
    <div className="min-h-screen bg-gray-950 text-gray-100">
      <Hero />
      <Products />
      <Testimonials />
      <FAQ />
      <Footer />
    </div>
  );
}

const products = [
  {
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
  },
  {
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
  },
  {
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
  },
  {
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
  },
  {
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
  },
];

function Products() {
  return (
    <section id="products" className="py-20 px-4">
      <div className="max-w-7xl mx-auto">
        <h2 className="text-3xl md:text-4xl font-bold text-center mb-4">
          Our <span className="text-orange-500">Products</span>
        </h2>
        <p className="text-gray-400 text-center mb-12 max-w-2xl mx-auto">
          Purpose-built templates and guides for construction professionals who
          want to automate their workflows and save hours every week.
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {products.map((product) => (
            <ProductCard key={product.name} {...product} />
          ))}
        </div>
      </div>
    </section>
  );
}
