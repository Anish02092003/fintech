import api from "./api";

export async function uploadIndividualPDF(
  name,
  file,
  pdfType = "summary",
  onProgress
) {
  const formData = new FormData();
  formData.append("name", name);
  formData.append("file", file);
  formData.append("pdf_type", pdfType);

  const response = await api.post(
    "/individual/upload",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
      onUploadProgress: (progressEvent) => {
        if (onProgress) {
          const percent = Math.round(
            (progressEvent.loaded * 100) / progressEvent.total
          );
          onProgress(percent);
        }
      },
    }
  );

  return response.data;
}