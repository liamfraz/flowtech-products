const testimonials = [
  {
    quote:
      "The workflow templates saved us weeks of development time. We had our expense claim automation running within a day of purchase.",
    name: "Sarah Mitchell",
    role: "Project Manager, Apex Constructions",
  },
  {
    quote:
      "The Beginner's Blueprint was exactly what our team needed. Clear, practical, and focused on real construction use cases. Highly recommended.",
    name: "James Chen",
    role: "IT Coordinator, BuildRight Group",
  },
  {
    quote:
      "We use the daily runsheet template on every site now. It standardised our reporting and made handovers between site managers seamless.",
    name: "David Thompson",
    role: "Construction Director, Pacific Developments",
  },
];

export function Testimonials() {
  return (
    <section className="py-20 px-4 bg-gray-900/50">
      <div className="max-w-7xl mx-auto">
        <h2 className="text-3xl md:text-4xl font-bold text-center mb-4">
          What Our <span className="text-orange-500">Customers</span> Say
        </h2>
        <p className="text-gray-400 text-center mb-12 max-w-2xl mx-auto">
          Trusted by construction professionals across Australia.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {testimonials.map((t) => (
            <div
              key={t.name}
              className="bg-gray-900 border border-gray-800 rounded-xl p-6"
            >
              {/* Stars */}
              <div className="flex gap-1 mb-4">
                {[...Array(5)].map((_, i) => (
                  <svg
                    key={i}
                    className="w-5 h-5 text-orange-500"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                ))}
              </div>

              <p className="text-gray-300 mb-6 italic">"{t.quote}"</p>

              <div>
                <div className="font-semibold text-white">{t.name}</div>
                <div className="text-sm text-gray-500">{t.role}</div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
