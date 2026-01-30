import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const COLORS = ["#16a34a", "#dc2626", "#2563eb", "#ca8a04"];

export default function PieChartCard({ title, data }) {
  return (
    <div className="bg-white rounded-xl shadow-md p-4 h-72">
      <h3 className="text-sm font-medium mb-3">{title}</h3>

      <ResponsiveContainer width="100%" height="100%">
        <PieChart>
          <Pie
            data={data}
            dataKey="value"
            nameKey="label"
            outerRadius={90}
          >
            {data.map((_, i) => (
              <Cell key={i} fill={COLORS[i % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}