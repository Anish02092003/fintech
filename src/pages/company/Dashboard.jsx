import MetricCard from "../../components/MetricCard";
import StatusBadge from "../../components/StatusBadge";

export default function CompanyDashboard({ data }) {
  if (!data) {
    return (
      <div className="text-gray-500 text-center mt-10">
        Upload a PDF to see analysis
      </div>
    );
  }

  return (
    <div className="p-6 space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-semibold">
          {data.company_name} – Financial Overview
        </h1>

        <StatusBadge status={data.overall_health} />
      </div>

      {/* Metrics grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        <MetricCard label="Revenue" value={data.revenue} />
        <MetricCard label="Net Profit" value={data.net_profit} />
        <MetricCard label="Operating Profit" value={data.operating_profit} />
        <MetricCard label="Total Assets" value={data.total_assets} />
        <MetricCard label="Total Liabilities" value={data.total_liabilities} />
        <MetricCard label="Total Debt" value={data.total_debt} />
      </div>

      {/* Assumptions / Notes */}
      {data.assumptions && (
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