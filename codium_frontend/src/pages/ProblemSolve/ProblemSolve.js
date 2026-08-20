import React, { useState, useEffect } from 'react';
import CodeMirror from '@uiw/react-codemirror';
import { python } from '@codemirror/lang-python';
import { java } from '@codemirror/lang-java';
import { cpp } from '@codemirror/lang-cpp';
// import { sql } from '@codemirror/lang-sql';
import { oneDark } from '@codemirror/theme-one-dark';
import '../../styles/ProblemSolve.css';

const STARTERS = {
  python: `# type your code here\n`,
  java: `// type your code here`,
  c: `/*type your code here*/`,
  // sql: `-- Write your SQL query here`,
};

function ProblemSolve({ problem, onNavigate }) {
  const [language, setLanguage] = useState('python');
  const [code, setCode] = useState(STARTERS.python);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [activeTab, setActiveTab] = useState('description');
  const [hint, setHint] = useState(null);
  const [isHintLoading, setIsHintLoading] = useState(false);
  const [showHint, setShowHint] = useState(false);

  const handleGetHint = async () => {
    setIsHintLoading(true);
    setShowHint(true);
    try {
      const response = await fetch('http://localhost:8000/api/problems/get-hint/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          problem_title: problem.title,
          problem_description: problem.description,
          user_code: code,
          language: language
        }),
      });
      const data = await response.json();
      setHint(data.hints);
    } catch (error) {
      setHint("Failed to fetch hint. Please try again.");
    } finally {
      setIsHintLoading(false);
    }
  };

  useEffect(() => {
    if (problem?.topic?.toLowerCase() === 'sql') {
      setLanguage('sql');
      setCode(STARTERS.sql || '');
    } else {
      setLanguage('python');
      setCode(STARTERS.python);
    }
  }, [problem]);

  const getExtensions = () => {
    if (language === 'java') return [java()];
    if (language === 'python') return [python()];
    if (language === 'c') return [cpp()];
    // if (language === 'sql') return [sql()];
    return [];
  };

  const handleLanguageChange = (lang) => {
    setLanguage(lang);
    setCode(STARTERS[lang] || '');
    setResult(null);
  };

  const handleSubmit = async () => {
    setLoading(true);
    setResult(null);
    try {
      const response = await fetch('http://localhost:8000/api/code/submit/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: "include",
        body: JSON.stringify({ 
          code, 
          language, 
          problem_id: problem?.id || problem?._id 
        }),
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      setResult({ 
        status: 'error', 
        message: 'Server connection failed. Please try again later.' 
      });
    } finally {
      setLoading(false);
    }
  };

  const getDifficultyColor = (d) => {
    switch (d?.toLowerCase()) {
      case 'easy': return '#22c55e';
      case 'medium': return '#f59e0b';
      case 'hard': return '#ef4444';
      default: return '#666';
    }
  };

  if (!problem) {
    return (
      <div className="ps-error">
        <h3>No problem selected</h3>
        <button onClick={() => onNavigate('home')}>Go Home</button>
      </div>
    );
  }

  return (
    <div className="ps-container">
      <div className="ps-left">
        <div className="ps-tabs">
          {['description', 'examples'].map(tab => (
            <button
              key={tab}
              className={`ps-tab ${activeTab === tab ? 'active' : ''}`}
              onClick={() => setActiveTab(tab)}
            >
              {tab.charAt(0).toUpperCase() + tab.slice(1)}
            </button>
          ))}
        </div>

        <div className="ps-left-content">

          {activeTab === 'description' && (
            <>
              <div className="ps-problem-header">
                <h2>{problem.title}</h2>
                <span className="ps-difficulty" style={{ color: getDifficultyColor(problem.difficulty) }}>
                  {problem.difficulty}
                </span>
              </div>
              <span className="ps-topic-tag">{problem.topic}</span>
              <p className="ps-description">{problem.description}</p>

                        {showHint && (
          <div className="ps-hint-box">
            <div className="ps-hint-header">
              <span>AI Mentor 💡</span>
              <button onClick={() => setShowHint(false)}>×</button>
            </div>
            <div className="ps-hint-content">
              {isHintLoading ? (
                <div className="ps-hint-loader">Thinking...</div>
              ) : (
                <p>{hint}</p>
              )}
            </div>
          </div>
        )}
            </>
          )}

          {activeTab === 'examples' && (
            <div className="ps-examples">
              <div className="ps-example">
                <p className="ps-example-label">Sample Input</p>
                <pre className="ps-example-block">{problem.sample_input}</pre>
                <p className="ps-example-label">Expected Output</p>
                <pre className="ps-example-block">{problem.sample_output}</pre>
              </div>
            </div>
          )}
        </div>

        {(loading || result) && (
          <div className={`ps-result ${result?.status || result?.verdict?.toLowerCase() || ''}`}>
            {loading ? (
              <span className="ps-result-loading">⏳ Running test cases...</span>
            ) : (
              <>
                <div className="ps-result-header">
                  <span className={`ps-result-status ${result?.status || result?.verdict?.toLowerCase() || ''}`}>
                    {result?.status === 'accepted' || result?.verdict === 'AC' ? '✓ Accepted' :
                     result?.status === 'wrong' || result?.verdict === 'WA' ? '✗ Wrong Answer' :
                     '✗ Execution Error'}
                  </span>
                  {result?.passed != null && (
                    <span className="ps-result-cases">{result.passed}/{result.total} passed</span>
                  )}
                </div>
                {result?.message && <p className="ps-result-msg">{result.message}</p>}
                {(result?.output || result?.error) && (
                  <pre className="ps-console-log">
                    {result.output || result.error}
                  </pre>
                )}
              </>
            )}
          </div>
        )}
      </div>

      <div className="ps-right">
        <div className="ps-editor-toolbar">
          <select
            className="ps-lang-select"
            value={language}
            onChange={e => handleLanguageChange(e.target.value)}
          >
            <option value="python">Python</option>
            <option value="java">Java</option>
            <option value="c">C</option>
          </select>
          <button 
            className="ps-btn-hint" 
            onClick={handleGetHint} 
            disabled={isHintLoading}
          >
            {isHintLoading ? '...' : 'Get Hint'}
          </button>

          <button className="ps-btn-submit" onClick={handleSubmit} disabled={loading}>
            {loading ? 'Submitting...' : 'Submit'}
          </button>
        </div>


        <div className="ps-editor-wrapper">
          <CodeMirror
            value={code}
            height="100%"
            theme={oneDark}
            extensions={getExtensions()}
            onChange={(value) => setCode(value)}
            basicSetup={{ lineNumbers: true, foldGutter: true, autocompletion: true }}
          />
        </div>
      </div>
    </div>
  );
}

export default ProblemSolve;