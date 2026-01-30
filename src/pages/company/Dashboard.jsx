import MetricCard from "../../components/MetricCard";
import StatusBadge from "../../components/StatusBadge";
import BarChartCard from "../../components/charts/BarChartCard";
import PieChartCard from "../../components/charts/PieChartCard";
import { useAppData } from "../../context/AppContext";

export default function CompanyDashboard() {
  const { companyData :data } = useAppData();
  

  if (!data) {
    return (
      <div className="text-gray-500 text-center mt-10">
        Upload a PDF to see analysis
      </div>
    );
  }

  // -------------------------
  // Safe values
  // -------------------------
  const revenue = data.revenue ?? 0;
  const netProfit = data.net_profit ?? 0;
  const operatingProfit = data.operating_profit ?? 0;
  const assets = data.total_assets ?? 0;
  const liabilities = data.total_liabilities ?? 0;
  const debt = data.total_debt ?? 0;

  const barData = [
    { label: "Revenue", value: revenue },
    { label: "Net Profit", value: netProfit },
    { label: "Operating Profit", value: operatingProfit },
  ];

  const pieData = [
    { label: "Assets", value: assets },
    { label: "Liabilities", value: liabilities },
    { label: "Debt", value: debt },
  ];

  return (
    <div className="p-6 space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-semibold">
          {data.company_name} – Financial Overview
        </h1>

        <StatusBadge status={data.overall_health} />
      </div>

      {/* KPI ROW */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <MetricCard
          label="Overall Health"
          value={(data.overall_health || "N/A").toUpperCase()}
        />
        <MetricCard
          label="Liquidity Status"
          value={(data.scores?.liquidity || "N/A").toUpperCase()}
        />
        <MetricCard
          label="Leverage Risk"
          value={(data.scores?.leverage || "N/A").toUpperCase()}
        />
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        <BarChartCard
          title="Profitability Overview"
          data={barData}
        />

        <PieChartCard
          title="Balance Sheet Composition"
          data={pieData}
        />
      </div>

      {/* Financial Metrics */}
      <div>
        <h2 className="text-lg font-medium mb-3">
          Financial Metrics
        </h2>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <MetricCard label="Revenue" value={revenue} />
          <MetricCard label="Net Profit" value={netProfit} />
          <MetricCard label="Operating Profit" value={operatingProfit} />
          <MetricCard label="Total Assets" value={assets} />
          <MetricCard label="Total Liabilities" value={liabilities} />
          <MetricCard label="Total Debt" value={debt} />
        </div>
      </div>

      {/* Future charts */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="bg-white border rounded-lg p-4 text-gray-400 text-sm">
          📈 Revenue / Profit Trend (coming next)
        </div>

        <div className="bg-white border rounded-lg p-4 text-gray-400 text-sm">
          🧱 Assets vs Liabilities (coming next)
        </div>
      </div>

      {/* Assumptions */}
      {data.assumptions?.length > 0 && (
        <div className="bg-gray-50 rounded-lg p-4">
          <h3 className="font-medium mb-2">Assumptions</h3>
          <ul className="list-disc pl-5 text-sm text-gray-600">
            {data.assumptions.map((a, i) => (
              <li key={i}>{a}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}