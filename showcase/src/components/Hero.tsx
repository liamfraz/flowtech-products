export function Hero() {
  return (
    <section className="relative overflow-hidden">
      {/* Background pattern */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-orange-900/20 via-gray-950 to-gray-950" />
      <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGRlZnM+PHBhdHRlcm4gaWQ9ImdyaWQiIHdpZHRoPSI2MCIgaGVpZ2h0PSI2MCIgcGF0dGVyblVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTSA2MCAwIEwgMCAwIDAgNjAiIGZpbGw9Im5vbmUiIHN0cm9rZT0icmdiYSgyNTUsMjU1LDI1NSwwLjAzKSIgc3Ryb2tlLXdpZHRoPSIxIi8+PC9wYXR0ZXJuPjwvZGVmcz48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSJ1cmwoI2dyaWQpIi8+PC9zdmc+')] opacity-50" />

      <div className="relative max-w-7xl mx-auto px-4 py-24 md:py-36 text-center">
        {/* Badge */}
        <div className="inline-flex items-center gap-2 bg-orange-500/10 border border-orange-500/20 rounded-full px-4 py-1.5 mb-8">
          <div className="w-2 h-2 rounded-full bg-orange-500 animate-pulse" />
          <span className="text-orange-400 text-sm font-medium">
            Built for Construction Professionals
          </span>
        </div>

        <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold mb-6 tracking-tight">
          Construction Automation
          <br />
          <span className="text-orange-500">Templates & Guides</span>
        </h1>

        <p className="text-lg md:text-xl text-gray-400 max-w-3xl mx-auto mb-10">
          Save hours every week with ready-to-use Power Automate workflows,
          professional Excel templates, and step-by-step automation guides built
          specifically for the construction industry.
        </p>

        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <a
            href="#products"
            className="inline-flex items-center justify-center px-8 py-3.5 bg-orange-500 hover:bg-orange-600 text-white font-semibold rounded-lg transition-colors"
          >
            Browse Products
          </a>
          <a
            href="#faq"
            className="inline-flex items-center justify-center px-8 py-3.5 border border-gray-700 hover:border-gray-500 text-gray-300 font-semibold rounded-lg transition-colors"
          >
            Learn More
          </a>
        </div>

        {/* Stats */}
        <div className="mt-16 grid grid-cols-2 md:grid-cols-4 gap-8 max-w-3xl mx-auto">
          {[
            { value: "10+", label: "Workflow Templates" },
            { value: "80+", label: "Pages of Guides" },
            { value: "100%", label: "Power Platform Native" },
            { value: "$0", label: "Extra Subscriptions" },
          ].map((stat) => (
            <div key={stat.label}>
              <div className="text-2xl md:text-3xl font-bold text-orange-500">
                {stat.value}
              </div>
              <div className="text-sm text-gray-500 mt-1">{stat.label}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
