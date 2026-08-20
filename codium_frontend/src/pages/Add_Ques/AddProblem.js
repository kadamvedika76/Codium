import React, { useState } from 'react';
import './AddProblem.css';

function AddProblem() {
  const [formData, setFormData] = useState({
    title: '',
    topic: 'Arrays', // Matches your Django model default
    description: '',
    difficulty: 'Easy',
    sample_input: '',
    sample_output: ''
  });

  const [testcases, setTestcases] = useState([{ input: '', output: '' }]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleTestChange = (index, field, value) => {
    const updated = [...testcases];
    updated[index][field] = value;
    setTestcases(updated);
  };

  const addTestCase = () => setTestcases([...testcases, { input: '', output: '' }]);

  const removeTestCase = (index) => {
    if (testcases.length > 1) {
      setTestcases(testcases.filter((_, i) => i !== index));
    }
  };

  const handleSubmit = async () => {
    const payload = { ...formData, testcases };
    try {
      const response = await fetch('http://localhost:8000/api/add-problem/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify(payload)
      });
      if (response.ok) {
        alert("Problem & Test Cases Uploaded Successfully!");
        setFormData({
          title: '',
          topic: 'Arrays',
          description: '',
          difficulty: 'Easy',
          sample_input: '',
          sample_output: ''
        });
        setTestcases([{ input: '', output: '' }]);
      }
    } catch (error) {
      alert("Error connecting to server.");
    }
  };

  

  return (
    <div className="admin-container">
      <header className="admin-header">
        <div className="logo small">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M7 8L3 11.6923L7 16M17 8L21 11.6923L17 16M14 4L10 20" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
          <h1>Codium Creator</h1>
        </div>
        <button className="login-btn save-btn" onClick={handleSubmit}>
          Publish Problem
        </button>
      </header>

      <main className="admin-content">
        <section className="info-panel">
          <label>Problem Title</label>
          <input 
            name="title" 
            placeholder="e.g. Two Sum" 
            value={formData.title} 
            onChange={handleChange} 
          />

          {/* Combined Topic and Difficulty for better space usage */}
          <div className="form-row" style={{ display: 'flex', gap: '20px', marginBottom: '20px' }}>
            <div style={{ flex: 1 }}>
              <label>Topic</label>
              <input 
                name="topic" 
                placeholder="e.g. Arrays, String, SQL" 
                value={formData.topic} 
                onChange={handleChange} 
              />
            </div>
            <div style={{ flex: 1 }}>
              <label>Difficulty</label>
              <select name="difficulty" value={formData.difficulty} onChange={handleChange} className="custom-select">
                <option value="Easy">Easy</option>
                <option value="Medium">Medium</option>
                <option value="Hard">Hard</option>
              </select>
            </div>
          </div>

          <label>Description</label>
          <textarea 
            name="description" 
            placeholder="Describe the problem, constraints, and edge cases..." 
            value={formData.description} 
            onChange={handleChange}
            rows="10"
          />

          <div className="sample-grid">
            <div>
              <label>Sample Input</label>
              <textarea name="sample_input" value={formData.sample_input} onChange={handleChange} rows="3" />
            </div>
            <div>
              <label>Sample Output</label>
              <textarea name="sample_output" value={formData.sample_output} onChange={handleChange} rows="3" />
            </div>
          </div>
        </section>

        <section className="testcase-panel">
          <div className="panel-header">
            <h3 className='hidden'>Hidden Test Cases</h3>
            <button className="add-tc-btn" onClick={addTestCase}>+ Add</button>
          </div>
          <div className="tc-list">
            {testcases.map((tc, index) => (
              <div key={index} className="tc-card">
                <div className="tc-header">
                  <span>Case #{index + 1}</span>
                  <button className="delete-tc" onClick={() => removeTestCase(index)}>×</button>
                </div>
                <textarea 
                  placeholder="Input" 
                  value={tc.input} 
                  onChange={(e) => handleTestChange(index, 'input', e.target.value)} 
                />
                <textarea 
                  placeholder="Expected Output" 
                  value={tc.output} 
                  onChange={(e) => handleTestChange(index, 'output', e.target.value)} 
                />
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}

export default AddProblem;