import React from "react";
import PdfUpload from "./PdfUpload";
import AskPdf from "./AskPdf";

function App() {
  return (
    <div className="app-container">
      <h1>PDF AI App</h1>
      <PdfUpload />
      <AskPdf />
    </div>
  );
}

export default App;
