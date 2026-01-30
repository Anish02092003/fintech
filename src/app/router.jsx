import { createBrowserRouter } from "react-router-dom";
import AppLayout from "./layout";

// Pages
import Home from "../pages/home/Home";

// Individual
import IndividualUpload from "../pages/individual/Upload";
import IndividualDashboard from "../pages/individual/Dashboard";
import IndividualSimulations from "../pages/individual/Simulations";
import IndividualExplain from "../pages/individual/Explain";

// Company
import CompanyUpload from "../pages/company/Upload";
import CompanyDashboard from "../pages/company/Dashboard";
import CompanyCompare from "../pages/company/Compare";
import CompanyTrends from "../pages/company/Trends";
import CompanyExplain from "../pages/company/Explain";

// System
import SystemHealth from "../pages/system/Health";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <AppLayout />,
    children: [
      { index: true, element: <Home /> },

      // Individual
      { path: "individual/upload", element: <IndividualUpload /> },
      { path: "individual/dashboard", element: <IndividualDashboard /> },
      { path: "individual/simulations", element: <IndividualSimulations /> },
      { path: "individual/explain", element: <IndividualExplain /> },

      // Company
      { path: "company/upload", element: <CompanyUpload /> },
      { path: "company/dashboard", element: <CompanyDashboard /> },
      { path: "company/compare", element: <CompanyCompare /> },
      { path: "company/trends", element: <CompanyTrends /> },
      { path: "company/explain", element: <CompanyExplain /> },

      // System
      { path: "system/health", element: <SystemHealth /> },
    ],
  },
]);