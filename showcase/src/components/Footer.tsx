export function Footer() {
  return (
    <footer className="border-t border-gray-800 py-12 px-4">
      <div className="max-w-7xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
          {/* Brand */}
          <div>
            <div className="flex items-center gap-2 mb-4">
              <div className="w-8 h-8 bg-orange-500 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-sm">FT</span>
              </div>
              <span className="text-lg font-bold text-white">
                Flowtech Advisory
              </span>
            </div>
            <p className="text-gray-500 text-sm">
              Helping construction companies automate their operations with
              Microsoft Power Platform.
            </p>
          </div>

          {/* Products */}
          <div>
            <h4 className="font-semibold text-white mb-4">Products</h4>
            <ul className="space-y-2 text-sm text-gray-500">
              <li>
                <a href="#products" className="hover:text-orange-500 transition-colors">
                  Workflow Templates
                </a>
              </li>
              <li>
                <a href="#products" className="hover:text-orange-500 transition-colors">
                  Excel Templates
                </a>
              </li>
              <li>
                <a href="#products" className="hover:text-orange-500 transition-colors">
                  PDF Guides
                </a>
              </li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h4 className="font-semibold text-white mb-4">Contact</h4>
            <ul className="space-y-2 text-sm text-gray-500">
              <li>support@flowtechadvisory.com</li>
              <li>Melbourne, Australia</li>
            </ul>
          </div>
        </div>

        <div className="border-t border-gray-800 pt-8 text-center text-sm text-gray-600">
          &copy; {new Date().getFullYear()} Flowtech Advisory. All rights
          reserved.
        </div>
      </div>
    </footer>
  );
}
