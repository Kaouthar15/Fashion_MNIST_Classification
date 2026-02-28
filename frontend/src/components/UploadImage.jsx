import { useState } from "react";
import { predictImage } from "../services/api";

export default function UploadImage({ setResult, nSamples }) {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const res = await predictImage(formData, nSamples);
    setResult(res.data);
  };

  return (
    <div>
      <div className="section-title">Input</div>

      <input
        type="file"
        style={{
          marginBottom: 20,
          color: "#e6edf3"
        }}
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button className="button-primary" onClick={handleUpload}>
        Run Inference
      </button>
    </div>
  );
}