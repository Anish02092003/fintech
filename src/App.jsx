// src/App.jsx
import { BrowserRouter } from "react-router-dom";
import AppLayout from "./app/layout";
import AppRouter from "./app/router";
import { RouterProvider } from "react-router-dom";
import { router } from "./app/router";

export default function App() {
  return <RouterProvider router={router} />;
}

export default function App() {
  return (
    <BrowserRouter>
      <AppLayout>
        <AppRouter />
      </AppLayout>
    </BrowserRouter>
  );
}

// src/app/layout.jsx
import { Link, useLocation } from "react-router-dom";

export default function AppLayout({ children }) {
  const location = useLocation();

  const nav = [
    { label: "Home", to: "/" },
    { label: "Individual", to: "/individual/upload" },
    { label: "Company", to: "/company/upload" },
    { label: "Simulations", to: "/individual/simulations" },
  ];

  return (
    <div className="flex min-h-screen bg-gray-50">
      {/* Sidebar */}
      <aside className="w-60 bg-white border-r p-4">
        <h1 className="text-xl font-bold mb-6">Finance AI</h1>
        <nav className="space-y-2">
          {nav.map(n => (
            <Link
              key={n.to}
              to={n.to}
              className={`block px-3 py-2 rounded-lg text-sm ${
                location.pathname.startsWith(n.to)
                  ? "bg-black text-white"
                  : "hover:bg-gray-100"
              }`}
            >
              {n.label}
            </Link>
          ))}
        </nav>
      </aside>

      {/* Main */}
      <main className="flex-1 p-6">{children}</main>
    </div>
  );
}

// src/app/router.jsx
import { Routes, Route } from "react-router-dom";

import Home from "../pages/home/Home";

import IndividualUpload from "../pages/individual/Upload";
import IndividualDashboard from "../pages/individual/Dashboard";
import IndividualSimulations from "../pages/individual/Simulations";
import IndividualExplain from "../pages/individual/Explain";

import CompanyUpload from "../pages/company/Upload";
import CompanyDashboard from "../pages/company/Dashboard";
import CompanyCompare from "../pages/company/Compare";
import CompanyTrends from "../pages/company/Trends";
import CompanyExplain from "../pages/company/Explain";

import SystemHealth from "../pages/system/Health";

export default function AppRouter() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />

      {/* Individual */}
      <Route path="/individual/upload" element={<IndividualUpload />} />
      <Route path="/individual/dashboard" element={<IndividualDashboard />} />
      <Route path="/individual/simulations" element={<IndividualSimulations />} />
      <Route path="/individual/explain" element={<IndividualExplain />} />

      {/* Company */}
      <Route path="/company/upload" element={<CompanyUpload />} />
      <Route path="/company/dashboard" element={<CompanyDashboard />} />
      <Route path="/company/compare" element={<CompanyCompare />} />
      <Route path="/company/trends" element={<CompanyTrends />} />
      <Route path="/company/explain" element={<CompanyExplain />} />

      {/* System */}
      <Route path="/system/health" element={<SystemHealth />} />
    </Routes>
  );
}

// Example placeholder page: src/pages/home/Home.jsx
export default function Home() {
  return (
    <div className="space-y-2">
      <h2 className="text-2xl font-semibold">Welcome</h2>
      <p className="text-gray-600">
        Finance Intelligence platform for individuals and companies.
      </p>
    </div>
  );
}
