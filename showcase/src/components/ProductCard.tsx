import type { Product } from "../config/products";

export function ProductCard({
  name,
  price,
  originalPrice,
  description,
  features,
  badge,
  gumroadUrl,
}: Product) {
  return (
    <div className="group relative bg-gray-900 border border-gray-800 rounded-xl p-6 hover:border-orange-500/50 transition-all duration-300 flex flex-col">
      {badge && (
        <span className="absolute -top-3 right-4 bg-orange-500 text-white text-xs font-bold px-3 py-1 rounded-full">
          {badge}
        </span>
      )}

      <div className="mb-4 flex items-baseline gap-2">
        <span className="text-3xl font-bold text-orange-500">{price}</span>
        {originalPrice && (
          <span className="text-lg text-gray-500 line-through">{originalPrice}</span>
        )}
      </div>

      <h3 className="text-xl font-bold text-white mb-3">{name}</h3>

      <p className="text-gray-400 text-sm mb-6 flex-grow">{description}</p>

      <ul className="space-y-2 mb-6">
        {features.map((feature) => (
          <li key={feature} className="flex items-start gap-2 text-sm">
            <svg
              className="w-5 h-5 text-orange-500 shrink-0 mt-0.5"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M5 13l4 4L19 7"
              />
            </svg>
            <span className="text-gray-300">{feature}</span>
          </li>
        ))}
      </ul>

      <a
        href={gumroadUrl}
        className="gumroad-button group/btn flex items-center justify-center gap-2 w-full py-3 bg-orange-500 hover:bg-orange-600 text-white font-semibold rounded-lg transition-all duration-200 shadow-lg shadow-orange-500/20 hover:shadow-orange-500/40"
      >
        <svg
          className="w-5 h-5"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 100 4 2 2 0 000-4z"
          />
        </svg>
        Buy on Gumroad
        <svg
          className="w-4 h-4 transition-transform group-hover/btn:translate-x-0.5"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M9 5l7 7-7 7"
          />
        </svg>
      </a>
    </div>
  );
}
