interface ProductCardProps {
  name: string;
  price: string;
  description: string;
  features: string[];
  badge: string | null;
}

export function ProductCard({
  name,
  price,
  description,
  features,
  badge,
}: ProductCardProps) {
  return (
    <div className="group relative bg-gray-900 border border-gray-800 rounded-xl p-6 hover:border-orange-500/50 transition-all duration-300 flex flex-col">
      {badge && (
        <span className="absolute -top-3 right-4 bg-orange-500 text-white text-xs font-bold px-3 py-1 rounded-full">
          {badge}
        </span>
      )}

      <div className="mb-4">
        <span className="text-3xl font-bold text-orange-500">{price}</span>
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
        href="https://gumroad.com"
        target="_blank"
        rel="noopener noreferrer"
        className="block w-full text-center py-3 bg-gray-800 hover:bg-orange-500 text-gray-200 hover:text-white font-semibold rounded-lg transition-colors"
      >
        Buy on Gumroad
      </a>
    </div>
  );
}
