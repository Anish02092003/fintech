export default function KPICard({ label, value, status }) {
  const colorMap = {
    good: "bg-green-50 text-green-700",
    moderate: "bg-yellow-50 text-yellow-700",
    weak: "bg-red-50 text-red-700",
  };

  return (
    <div className="p-4 rounded-lg border bg-white shadow-sm">
      <p className="text-sm text-gray-500">{label}</p>
      <p className="text-2xl font-semibold mt-1">{value}</p>
      {status && (
        <span
          className={`inline-block mt-2 px-2 py-1 text-xs rounded ${
            colorMap[status]
          }`}
        >
          {status.toUpperCase()}
        </span>
      )}
    </div>
  );
}