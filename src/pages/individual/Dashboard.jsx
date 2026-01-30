import KPICard from "../../components/KPICard";
import ChartCard from "../../components/ChartCard";
import InsightBox from "../../components/InsightBox";
import { useAppData } from "../../context/AppContext";

export default function IndividualDashboard({ data }) {
  const { individualData: data } = useAppData();
  if (!data) {
    return (
      <div className="text-center text-gray-500 mt-10">
        Upload a PDF to see your dashboard
      </div>
    );
  }

  const overallHealth = data.overall_health || "unknown";
  const liquidity = data.scores?.liquidity || "n/a";
  const leverage = data.scores?.leverage || "n/a";

  return (
    <div className="p-6 space-y-6">
      {/* Header */}
      <h1 className="text-2xl font-semibold">
        Financial Overview
      </h1>

      {/* KPI Row */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <KPICard
          label="Overall Health"
          value={overallHealth.toUpperCase()}
          status={overallHealth}
        />

        <KPICard
          label="Liquidity"
          value={liquidity.toUpperCase()}
          status={liquidity}
        />

        <KPICard
          label="Leverage Risk"
          value={leverage.toUpperCase()}
          status={leverage}
        />
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <ChartCard title="Income Breakdown">
          <div className="text-sm text-gray-400">
            Chart coming next
          </div>
        </ChartCard>

        <ChartCard title="Assets vs Liabilities">
          <div className="text-sm text-gray-400">
            Chart coming next
          </div>
        </ChartCard>
      </div>

      {/* Insights */}
      <InsightBox insights={data.insights || []} />
    </div>
  );
}