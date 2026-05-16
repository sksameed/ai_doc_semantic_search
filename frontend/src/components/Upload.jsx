import { useState } from "react";
import axios from "axios";

const Upload = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a PDF file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData
      );

      setMessage(response.data.message);
    } catch (error) {
      setMessage("Upload failed");
    }
  };
return (
    <div
      style={{
        marginTop: "20px",
        padding: "20px",
        border: "1px solid #374151",
        borderRadius: "10px"
      }}
    >
      <h2>Upload PDF</h2>

      <input
        type="file"
        accept="application/pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br />
      <br />

      <button onClick={handleUpload}>Upload</button>

      <p>{message}</p>
    </div>
  );
};

export default Upload;