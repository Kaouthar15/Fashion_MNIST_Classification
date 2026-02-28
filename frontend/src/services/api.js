import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const predictImage = (formData, n_samples) =>
  API.post("/predict", formData, {
    params: { n_samples },
  });