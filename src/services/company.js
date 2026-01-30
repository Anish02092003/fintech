import api from "./api";

/**
 * Upload single company PDF
 */
export async function uploadCompanyPdf(
  companyName,
  file,
  pdfType = "summary",
  onProgress
) {
  try {
    const formData = new FormData();
    formData.append("company_name", companyName);
    formData.append("file", file);
    formData.append("pdf_type", pdfType);

    const response = await api.post(
      "/company/upload",
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
      "Failed to upload company PDF"
    );
  }
}

/**
 * Compare two companies
 */
export async function compareCompanies(
  companyA,
  fileA,
  companyB,
  fileB,
  pdfType = "summary",
  onProgress
) {
  try {
    const formData = new FormData();
    formData.append("company_a_name", companyA);
    formData.append("company_b_name", companyB);
    formData.append("file_a", fileA);
    formData.append("file_b", fileB);
    formData.append("pdf_type", pdfType);

    const response = await api.post(
      "/company/compare-upload",
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
      "Failed to compare companies"
    );
  }
}