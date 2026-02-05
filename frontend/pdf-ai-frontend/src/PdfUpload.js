import React, { useState } from "react";

function PdfUpload() {
  const [file, setFile] = useState(null);
  const [docId, setDocId] = useState("");

  const uploadPdf = async () => {
    if (!file) {
      alert("Select a PDF first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://3.6.39.190:8000/api/pdf/upload/", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    setDocId(data.doc_id);
    localStorage.setItem("doc_id", data.doc_id);
  };

  return (
    <div className="section">
      <h2>Upload PDF</h2>

      <label className="file-label">
        Choose File
        <input
          type="file"
          accept="application/pdf"
          className="file-input"
          onChange={(e) => setFile(e.target.files[0])}
        />
      </label>

      <button className="btn" onClick={uploadPdf}>
        Upload
      </button>

      {docId && (
        <p>
          <b>Doc ID:</b> {docId}
        </p>
      )}
    </div>
  );
}

export default PdfUpload;
