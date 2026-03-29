import { ProductCard } from "./components/ProductCard";
import { Testimonials } from "./components/Testimonials";
import { FAQ } from "./components/FAQ";
import { Hero } from "./components/Hero";
import { Footer } from "./components/Footer";
import { products, bundleProduct } from "./config/products";

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
            <ProductCard key={product.id} {...product} />
          ))}
        </div>

        {/* Bundle CTA */}
        <div className="mt-16 relative bg-gradient-to-r from-orange-500/10 via-orange-500/5 to-orange-500/10 border border-orange-500/30 rounded-2xl p-8 md:p-12">
          <div className="absolute -top-4 left-1/2 -translate-x-1/2 bg-orange-500 text-white text-sm font-bold px-5 py-1.5 rounded-full">
            Save ${bundleProduct.originalPrice && bundleProduct.price ? parseInt(bundleProduct.originalPrice.replace('$', '')) - parseInt(bundleProduct.price.replace('$', '')) : 70}
          </div>
          <div className="grid md:grid-cols-2 gap-8 items-center">
            <div>
              <h3 className="text-2xl md:text-3xl font-bold text-white mb-3">
                {bundleProduct.name}
              </h3>
              <p className="text-gray-400 mb-4">{bundleProduct.description}</p>
              <ul className="space-y-2">
                {bundleProduct.features.map((feature) => (
                  <li key={feature} className="flex items-center gap-2 text-sm text-gray-300">
                    <svg className="w-4 h-4 text-orange-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                    {feature}
                  </li>
                ))}
              </ul>
            </div>
            <div className="text-center">
              {bundleProduct.originalPrice && (
                <div className="mb-2">
                  <span className="text-lg text-gray-500 line-through">{bundleProduct.originalPrice}</span>
                </div>
              )}
              <div className="text-5xl font-bold text-orange-500 mb-6">{bundleProduct.price}</div>
              <a
                href={bundleProduct.gumroadUrl}
                className="gumroad-button inline-flex items-center justify-center gap-2 px-10 py-4 bg-orange-500 hover:bg-orange-600 text-white font-bold text-lg rounded-lg transition-all duration-200 shadow-lg shadow-orange-500/20 hover:shadow-orange-500/40"
              >
                Get the Bundle
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 8l4 4m0 0l-4 4m4-4H3" />
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
