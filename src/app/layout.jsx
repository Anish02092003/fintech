import { NavLink, Outlet } from "react-router-dom";

export default function AppLayout() {
  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <aside className="w-64 bg-black text-white p-4 space-y-4">
        <h1 className="text-xl font-semibold mb-6">
          📊 Finance AI
        </h1>

        <nav className="space-y-2 text-sm">
          <NavItem to="/">Home</NavItem>

          <Section title="Individual">
            <NavItem to="/individual/upload">Upload</NavItem>
            <NavItem to="/individual/dashboard">Dashboard</NavItem>
            <NavItem to="/individual/simulations">Simulations</NavItem>
            <NavItem to="/individual/explain">Explain</NavItem>
          </Section>

          <Section title="Company">
            <NavItem to="/company/upload">Upload</NavItem>
            <NavItem to="/company/dashboard">Dashboard</NavItem>
            <NavItem to="/company/compare">Compare</NavItem>
            <NavItem to="/company/trends">Trends</NavItem>
            <NavItem to="/company/explain">Explain</NavItem>
          </Section>

          <NavItem to="/system/health">System Health</NavItem>
        </nav>
      </aside>

      {/* Main content */}
      <main className="flex-1 overflow-y-auto p-6">
        <Outlet />
      </main>
    </div>
  );
}

/* ------------------ helpers ------------------ */

function NavItem({ to, children }) {
  return (
    <NavLink
      to={to}
      className={({ isActive }) =>
        `block px-3 py-2 rounded ${
          isActive
            ? "bg-gray-800 text-white"
            : "text-gray-300 hover:bg-gray-800"
        }`
      }
    >
      {children}
    </NavLink>
  );
}

function Section({ title, children }) {
  return (
    <div className="mt-4">
      <div className="text-xs uppercase text-gray-400 mb-1">
        {title}
      </div>
      {children}
    </div>
  );
}