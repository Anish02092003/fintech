import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api/v1", // change later for prod
  timeout: 60000, // PDFs take time
});

api.interceptors.response.use(
  (res) => res,
  (err) => {
    const message =
      err?.response?.data?.detail ||
      err?.message ||
      "API Error";
    return Promise.reject(new Error(message));
  }
);

export default api;