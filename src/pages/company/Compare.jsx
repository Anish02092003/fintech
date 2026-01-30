import ComparisonTable from "../../components/ComparisonTable";
import WinnerBanner from "../../components/WinnerBanner";
import StatusBadge from "../../components/StatusBadge";

export default function CompanyCompare({ data }) {
  if (!data) {
    return (
      <div className="text-gray-500 text-center mt-10">
        Upload two company PDFs to compare
      </div>
    );
  }

  const companies = Object.keys(data?.scores || {});
  if (companies.length < 2) {
    return (
      <div className="text-red-500 text-center mt-10">
        Comparison data incomplete
      </div>
    );
  }

  const [companyA, companyB] = companies;

  const metricConfig = [
    { label: "Revenue", key: "revenue" },
    { label: "Net Profit", key: "net_profit" },
    { label: "Operating Profit", key: "operating_profit" },
    { label: "Total Assets", key: "total_assets" },
    { label: "Total Liabilities", key: "total_liabilities" },
    { label: "Total Debt", key: "total_debt" },
  ];

  const metrics = metricConfig.map((m) => ({
    label: m.label,
    a: data.metrics?.[companyA]?.[m.key] ?? 0,
    b: data.metrics?.[companyB]?.[m.key] ?? 0,
  }));

  return (
    <div className="p-6 space-y-6">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
        <h1 className="text-2xl font-semibold">
          Company Comparison
        </h1>

        {/* Credit Ratings */}
        <div className="flex gap-4">
          <div className="flex items-center gap-2">
            <span className="text-sm font-medium">
              {companyA}
            </span>
            <StatusBadge
              status={data.credit_rating?.[companyA]}
            />
          </div>

          <div className="flex items-center gap-2">
            <span className="text-sm font-medium">
              {companyB}
            </span>
            <StatusBadge
              status={data.credit_rating?.[companyB]}
            />
          </div>
        </div>
      </div>

      {/* Winner */}
      <WinnerBanner
        winner={data.winner}
        isTie={data.winner === "tie"}
      />

      {/* Metrics Table */}
      <ComparisonTable
        companyA={companyA}
        companyB={companyB}
        metrics={metrics}
      />

      {/* Key Differences */}
      {Array.isArray(data.key_differences) &&
        data.key_differences.length > 0 && (
          <div className="bg-gray-50 p-4 rounded-lg">
            <h3 className="font-medium mb-2">
              Key Differences
            </h3>
            <ul className="list-disc pl-5 text-sm text-gray-600">
              {data.key_differences.map((d, i) => (
                <li key={i}>{d}</li>
              ))}
            </ul>
          </div>
        )}
    </div>
  );
}