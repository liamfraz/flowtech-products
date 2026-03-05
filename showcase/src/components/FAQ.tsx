import { useState } from "react";

const faqs = [
  {
    q: "What format are the Power Automate templates in?",
    a: "All workflows are standard JSON workflow definitions that can be imported directly into Power Automate via the portal or packaged into a Solution. They use generic connection references so they work in any Microsoft 365 environment.",
  },
  {
    q: "Do I need a premium Power Automate license?",
    a: "Most templates use standard connectors (SharePoint, Teams, Outlook, Forms) which are included with Microsoft 365. A few workflows use the Approvals connector which requires at least a Power Automate per-user plan. The guides cover licensing requirements in detail.",
  },
  {
    q: "Are the Excel templates compatible with Excel Online?",
    a: "Yes. All Excel files work in both Excel Desktop and Excel Online (via SharePoint or OneDrive). Charts, formulas, and conditional formatting are fully compatible.",
  },
  {
    q: "Can I customise the templates for my company?",
    a: "Absolutely. All templates are designed as starting points. The workflow JSON files include parameterised values (site URLs, list IDs, email addresses) that you replace with your own. The Excel templates have instructions for adding rows and modifying categories.",
  },
  {
    q: "What if I get stuck setting something up?",
    a: "Each product includes detailed setup instructions. The workflow pack has a comprehensive README, and both PDF guides walk through every step with explanations. If you need additional help, Flowtech Advisory offers consulting services.",
  },
  {
    q: "Do you offer refunds?",
    a: "Yes. If the product does not meet your expectations, contact us within 30 days for a full refund via Gumroad. No questions asked.",
  },
];

export function FAQ() {
  const [open, setOpen] = useState<number | null>(null);

  return (
    <section id="faq" className="py-20 px-4">
      <div className="max-w-3xl mx-auto">
        <h2 className="text-3xl md:text-4xl font-bold text-center mb-4">
          Frequently Asked <span className="text-orange-500">Questions</span>
        </h2>
        <p className="text-gray-400 text-center mb-12">
          Everything you need to know before purchasing.
        </p>

        <div className="space-y-3">
          {faqs.map((faq, i) => (
            <div
              key={i}
              className="border border-gray-800 rounded-lg overflow-hidden"
            >
              <button
                onClick={() => setOpen(open === i ? null : i)}
                className="w-full flex items-center justify-between px-6 py-4 text-left hover:bg-gray-900/50 transition-colors"
              >
                <span className="font-medium text-gray-200">{faq.q}</span>
                <svg
                  className={`w-5 h-5 text-orange-500 shrink-0 ml-4 transition-transform ${
                    open === i ? "rotate-180" : ""
                  }`}
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M19 9l-7 7-7-7"
                  />
                </svg>
              </button>
              {open === i && (
                <div className="px-6 pb-4 text-gray-400 text-sm">{faq.a}</div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
