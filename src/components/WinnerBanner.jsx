export default function WinnerBanner({ winner }) {
  if (!winner || winner === "tie") {
    return (
      <div className="bg-gray-100 text-gray-700 p-4 rounded-lg">
        Both companies show comparable financial strength.
      </div>
    );
  }

  return (
    <div className="bg-green-50 text-green-700 p-4 rounded-lg font-medium">
      ✅ {winner} appears financially stronger overall
    </div>
  );
}