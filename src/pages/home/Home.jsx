import { useNavigate } from "react-router-dom";

export default function Home() {
  const navigate = useNavigate();

  return (
    <div className="max-w-3xl mx-auto mt-20 space-y-6">
      <h1 className="text-3xl font-semibold text-center">
        Finance Intelligence AI
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card
          title="👤 Individual Analysis"
          onClick={() => navigate("/individual/upload")}
        />

        <Card
          title="🏢 Company Analysis"
          onClick={() => navigate("/company/upload")}
        />

        <Card
          title="🏢↔🏢 Company Comparison"
          onClick={() => navigate("/company/compare")}
        />
      </div>
    </div>
  );
}

function Card({ title, onClick }) {
  return (
    <button
      onClick={onClick}
      className="bg-white p-6 rounded-xl shadow hover:shadow-lg transition text-lg"
    >
      {title}
    </button>
  );
}