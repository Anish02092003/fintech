import MetricCard from "../../components/MetricCard";
import StatusBadge from "../../components/StatusBadge";

export default function IndividualDashboard({ data }) {
  if (!data) {
    return (
      <div className="text-gray-500 text-center mt-10">
        Upload a PDF to see analysis
      </div>
    );
  }

  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-semibold">
          {data.name} – Financial Health
        </h1>

        <StatusBadge status={data.overall_health} />
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        <MetricCard label="Income" value={data.revenue} />
        <MetricCard label="Savings" value={data.net_profit} />
        <MetricCard label="Assets" value={data.total_assets} />
        <MetricCard label="Liabilities" value={data.total_liabilities} />
        <MetricCard label="Debt" value={data.total_debt} />
      </div>
    </div>
  );
}