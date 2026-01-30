import UploadCard from "../../components/UploadCard";
import { uploadCompanyPDF } from "../../services/company";
import { useNavigate } from "react-router-dom";

export default function CompanyUpload() {
  const navigate = useNavigate();

  const handleSubmit = async ({ name, files, pdfType }) => {
    const data = await uploadCompanyPDF({
      name,
      files,
      pdfType,
    });

    console.log("Company result:", data);

    navigate("/company/dashboard");
  };

  return (
    <UploadCard
      title="Company Analysis"
      description="Upload annual report or financial summary PDF"
      onSubmit={handleSubmit}
      multiple={false}
    />
  );
}