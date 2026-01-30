export default function MetricCard({ label, value, unit = "", trend }) {
  return (
    <div className="bg-white rounded-xl shadow p-4">
      <p className="text-sm text-gray-500">{label}</p>

      <div className="flex items-center justify-between mt-1">
        <h3 className="text-2xl font-semibold">
          {value?.toLocaleString() || "—"} {unit}
        </h3>

        {trend && (
          <span
            className={`text-sm font-medium ${
              trend === "up"
                ? "text-green-600"
                : trend === "down"
                ? "text-red-600"
                : "text-gray-500"
            }`}
          >
            {trend === "up" && "▲"}
            {trend === "down" && "▼"}
            {trend === "flat" && "•"}
          </span>
        )}
      </div>
    </div>
  );
}