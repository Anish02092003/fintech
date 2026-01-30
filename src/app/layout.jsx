import { NavLink, Outlet } from "react-router-dom";

export default function AppLayout() {
  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <aside className="w-64 bg-black text-white flex flex-col">
        {/* Logo */}
        <div className="p-4 border-b border-gray-800">
          <NavLink to="/" className="text-xl font-semibold block">
            📊 Finance AI
          </NavLink>
        </div>

        {/* Navigation */}
        <nav className="flex-1 overflow-y-auto p-4 space-y-3 text-sm">
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

          <Section title="System">
            <NavItem to="/system/health">Health</NavItem>
          </Section>
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
        `
        block px-3 py-2 rounded-md transition
        ${
          isActive
            ? "bg-gray-800 text-white font-medium"
            : "text-gray-300 hover:bg-gray-800 hover:text-white"
        }
        `
      }
    >
      {children}
    </NavLink>
  );
}

function Section({ title, children }) {
  return (
    <div className="mt-5">
      <div className="text-xs uppercase tracking-wide text-gray-400 mb-2">
        {title}
      </div>
      <div className="space-y-1">
        {children}
      </div>
    </div>
  );
}