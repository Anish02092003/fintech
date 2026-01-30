export default function ComparisonTable({ companyA, companyB, metrics }) {
  return (
    <div className="overflow-x-auto bg-white rounded-xl shadow">
      <table className="w-full border-collapse">
        <thead>
          <tr className="bg-gray-100 text-sm text-gray-600">
            <th className="p-3 text-left">Metric</th>
            <th className="p-3 text-right">{companyA}</th>
            <th className="p-3 text-right">{companyB}</th>
          </tr>
        </thead>

        <tbody>
          {metrics.map((m) => (
            <tr key={m.key} className="border-t">
              <td className="p-3 text-sm font-medium">{m.label}</td>
              <td className="p-3 text-right">
                {m.a?.toLocaleString() ?? "—"}
              </td>
              <td className="p-3 text-right">
                {m.b?.toLocaleString() ?? "—"}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}