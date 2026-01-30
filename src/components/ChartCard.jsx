export default function ChartCard({ title, children }) {
  return (
    <div className="bg-white border rounded-lg p-4 shadow-sm">
      <h3 className="text-sm font-medium mb-3">{title}</h3>
      <div className="h-64">{children}</div>
    </div>
  );
}