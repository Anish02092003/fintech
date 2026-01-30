export default function StatusBadge({ status }) {
  const styles = {
    strong: "bg-green-100 text-green-700",
    stable: "bg-blue-100 text-blue-700",
    weak: "bg-yellow-100 text-yellow-700",
    risky: "bg-red-100 text-red-700",
  };

  return (
    <span
      className={`px-3 py-1 rounded-full text-sm font-medium ${
        styles[status] || "bg-gray-100 text-gray-600"
      }`}
    >
      {status?.toUpperCase() || "UNKNOWN"}
    </span>
  );
}