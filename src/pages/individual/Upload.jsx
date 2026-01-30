import UploadCard from "../../components/UploadCard";
import { uploadIndividualPDF } from "../../services/individual";
import { useNavigate } from "react-router-dom";

export default function IndividualUpload() {
  const navigate = useNavigate();

  const handleSubmit = async ({ name, files, pdfType }) => {
    const data = await uploadIndividualPDF({
      name,
      files,
      pdfType,
    });

    console.log("Individual result:", data);

    // later: store in state / context
    navigate("/individual/dashboard");
  };

  return (
    <UploadCard
      title="Individual Financial Analysis"
      description="Upload a financial PDF to analyze health, risks, and simulations"
      onSubmit={handleSubmit}
      multiple={false}
    />
  );
}