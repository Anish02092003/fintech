export default function InsightBox({ insights = [] }) {
  if (!insights.length) return null;

  return (
    <div className="bg-blue-50 p-4 rounded-lg">
      <h3 className="font-medium mb-2">Key Insights</h3>
      <ul className="list-disc pl-5 text-sm text-blue-900">
        {insights.map((i, idx) => (
          <li key={idx}>{i}</li>
        ))}
      </ul>
    </div>
  );
}