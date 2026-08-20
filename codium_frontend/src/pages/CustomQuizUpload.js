import React, { useState } from 'react';
import '../styles/CustomQuizUpload.css';

function CustomQuizUpload({ onNavigate }) {
  const [file, setFile] = useState(null);
  const [numQuestions, setNumQuestions] = useState(5);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!file) return alert("Please upload a PDF!");
    
    setLoading(true);
    const formData = new FormData();
    formData.append('pdf', file);
    formData.append('count', numQuestions);

    try {
      const response = await fetch('http://localhost:8000/api/generate-quiz/', {
        method: 'POST',
        body: formData,
        credentials: 'include'
      });
      
      const data = await response.json();
      if (response.ok) {
        // Pass the generated questions back to App.js
        onNavigate('quiz', { questions: data.questions });
      }
    } catch (err) {
      alert("AI Generation failed. Check your API key or PDF size.");
    } finally {
      setLoading(false);
    }
  };

  return (
  <div className="custom-upload-container">
    <div className="upload-card">
      <h2>Custom PDF Quiz</h2>
      <p>Upload your notes (PDF) and We'll generate a custom quiz for you.</p>
      
      <div className="file-upload-section">
        <label className="custom-file-label">
          <input 
            type="file" 
            onChange={(e) => setFile(e.target.files[0])} 
            accept=".pdf" 
            style={{ display: 'none' }} // Hide the ugly default button
          />
          {file ? "Change PDF File" : "Choose PDF File"}
        </label>
        {file && <span className="file-name-display">Selected: {file.name}</span>}
      </div>

      <div className="range-control">
        <label>Number of Questions: {numQuestions}</label>
        <input 
          type="range" 
          min="3" 
          max="100" 
          value={numQuestions} 
          onChange={(e) => setNumQuestions(e.target.value)} 
          className="custom-slider"
        />
      </div>

      <button className="generate-btn" onClick={handleGenerate} disabled={loading}>
        {loading ? "We're generating the quiz..." : "Start Custom Quiz →"}
      </button>
    </div>
  </div>
);
}

export default CustomQuizUpload;