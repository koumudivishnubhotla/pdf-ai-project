import React, { useState } from "react";

function AskPdf() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const askQuestion = async () => {
    const docId = localStorage.getItem("doc_id");

    if (!docId) {
      alert("Upload a PDF first");
      return;
    }

    const response = await fetch("http://3.6.39.190:8000/api/pdf/ask/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        doc_id: docId,
        question: question,
      }),
    });

    const data = await response.json();
    setAnswer(data.answer || data.error);
  };

  return (
    <div className="section">
      <h2>Ask PDF</h2>

      <textarea
        rows="4"
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <br /><br />

      <button className="btn" onClick={askQuestion}>
        Ask
      </button>

      {answer && (
        <div className="answer-box">
          <h3>Answer</h3>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default AskPdf;
