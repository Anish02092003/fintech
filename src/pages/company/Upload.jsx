import UploadCard from "../../components/UploadCard";
import { uploadCompanyPdf } from "../../services/company";
import { useNavigate } from "react-router-dom";
import { useAppData } from "../../context/AppContext";

export default function CompanyUpload() {
  const navigate = useNavigate();
  const { setCompanyData } = useAppData();

  const handleSubmit = async ({ name, files, pdfType }) => {
    const data = await uploadCompanyPdf(
      name,
      files[0],
      pdfType
    );

    console.log("Company result:", data);

    // ✅ SAVE TO GLOBAL STATE
    setCompanyData(data);

    // ✅ MOVE TO DASHBOARD
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