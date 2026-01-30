import { useState } from "react";

export default function UploadCard({
  title,
  description,
  onSubmit,
  multiple = false,
  showPdfType = true,
}) {
  const [name, setName] = useState("");
  const [files, setFiles] = useState([]);
  const [pdfType, setPdfType] = useState("summary");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    setError(null);
    setFiles(Array.from(e.target.files));
  };

  const handleSubmit = async () => {
    if (!name || files.length === 0) {
      setError("Please enter name and upload PDF");
      return;
    }

    try {
      setLoading(true);
      setError(null);

      await onSubmit({
        name,
        files,
        pdfType,
      });
    } catch (err) {
      setError(
        err?.message || "Failed to process PDF. Please try another file."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-md p-6 w-full max-w-xl">
      <h2 className="text-xl font-semibold mb-1">{title}</h2>
      <p className="text-gray-500 mb-4">{description}</p>

      {/* Name input */}
      <div className="mb-4">
        <label className="block text-sm font-medium mb-1">
          Company / Person Name
        </label>
        <input
          type="text"
          className="w-full border rounded-md p-2"
          placeholder="Enter name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          disabled={loading}
        />
      </div>

      {/* File input */}
      <div className="mb-4">
        <label className="block text-sm font-medium mb-1">
          Upload PDF
        </label>
        <input
          type="file"
          accept=".pdf"
          multiple={multiple}
          onChange={handleFileChange}
          disabled={loading}
        />
        {files.length > 0 && (
          <p className="text-sm text-gray-600 mt-1">
            {files.map((f) => f.name).join(", ")}
          </p>
        )}
      </div>

      {/* PDF type */}
      {showPdfType && (
        <div className="mb-4">
          <label className="block text-sm font-medium mb-1">
            PDF Type
          </label>
          <select
            className="w-full border rounded-md p-2"
            value={pdfType}
            onChange={(e) => setPdfType(e.target.value)}
            disabled={loading}
          >
            <option value="summary">Summary PDF</option>
            <option value="annual_report">Annual Report (300+ pages)</option>
          </select>
        </div>
      )}

      {/* Error */}
      {error && (
        <div className="mb-3 text-sm text-red-600 bg-red-50 p-2 rounded">
          {error}
        </div>
      )}

      {/* Submit */}
      <button
        onClick={handleSubmit}
        disabled={loading}
        className="w-full bg-black text-white py-2 rounded-md hover:bg-gray-800 disabled:opacity-50"
      >
        {loading ? "Processing..." : "Analyze"}
      </button>
    </div>
  );
}