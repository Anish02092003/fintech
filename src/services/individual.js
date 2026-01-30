import api from "./api";

export async function uploadIndividualPdf(
  name,
  file,
  pdfType = "summary",
  onProgress
) {
  try {
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
          if (onProgress && progressEvent.total) {
            const percent = Math.round(
              (progressEvent.loaded * 100) / progressEvent.total
            );
            onProgress(percent);
          }
        },
      }
    );

    return response.data;
  } catch (err) {
    throw new Error(
      err?.response?.data?.detail ||
      err?.response?.data?.message ||
      "Failed to upload individual PDF"
    );
  }
}