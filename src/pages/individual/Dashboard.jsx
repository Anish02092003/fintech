import KPICard from "../../components/KPICard";
import ChartCard from "../../components/ChartCard";
import InsightBox from "../../components/InsightBox";
import { useAppData } from "../../context/AppContext";

export default function IndividualDashboard() {
  const { individualData: data } = useAppData();

  if (!data) {
    return (
      <div className="text-center text-gray-500 mt-10">
        Upload a PDF to see your dashboard
      </div>
    );
  }

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-2xl font-semibold">Financial Overview</h1>

      {/* KPI Row */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <KPICard
          label="Overall Health"
          value={data.overall_health?.toUpperCase() || "N/A"}
          status={data.overall_health}
        />
        <KPICard
          label="Liquidity"
          value={data.scores?.liquidity || "N/A"}
          status={data.scores?.liquidity}
        />
        <KPICard
          label="Leverage Risk"
          value={data.scores?.leverage || "N/A"}
          status={data.scores?.leverage}
        />
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <ChartCard title="Income Breakdown">
          {/* Recharts goes here */}
        </ChartCard>

        <ChartCard title="Assets vs Liabilities">
          {/* Recharts goes here */}
        </ChartCard>
      </div>

      {/* Insights */}
      {data.insights?.length > 0 && (
        <InsightBox insights={data.insights} />
      )}
    </div>
  );
}