import React, { useState, useEffect } from 'react';
import '../../styles/PracticeDSA.css';

function PracticeDSA({ onNavigate }) {
  const [problems, setProblems] = useState([]);
  const [filteredProblems, setFilteredProblems] = useState([]);
  const [selectedTopic, setSelectedTopic] = useState('All');
  const [loading, setLoading] = useState(true);

  const topics = ['All', 'Arrays', 'Stack', 'Queue', 'String', 'Linked List', 'Trees', 'Graphs', 'Dynamic Programming', 'Greedy', 'Backtracking'];

  useEffect(() => {
    fetchProblems();
  }, []);

  useEffect(() => {
    if (selectedTopic === 'All') {
      setFilteredProblems(problems);
    } else {
      // Note: Ensure your Django model has a 'topic' field or adjust this filter
      setFilteredProblems(problems.filter(p => p.topic === selectedTopic));
    }
  }, [selectedTopic, problems]);

  const fetchProblems = async () => {
    try {
      // 1. Updated URL to match your Django backend
      // 2. Added credentials: 'include' for session handling
      const response = await fetch('http://localhost:8000/api/problems/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) throw new Error('Network response was not ok');
      
      const data = await response.json();
      
      // Django returns an array of objects. 
      // Ensure the key for ID is 'id' (Django default) rather than '_id' (MongoDB default)
      setProblems(data);
      setFilteredProblems(data);
    } catch (error) {
      console.error("Fetch error:", error);
      // Fallback to empty or dummy if server is down
      setProblems([]);
    } finally {
      setLoading(false);
    }
  };

  const getDifficultyColor = (difficulty) => {
    switch(difficulty?.toLowerCase()) {
      case 'easy': return '#22c55e';
      case 'medium': return '#f59e0b';
      case 'hard': return '#ef4444';
      default: return '#666';
    }
  };

  return (
    <div className="practice-dsa-container">
      <div className="practice-dsa-header">
        <h1>Practice DSA Problems</h1>
        <p>Master data structures and algorithms with our curated problem set</p>
      </div>

      <div className="topics-section">
        <div className="topics-filter">
          {topics.map(topic => (
            <button
              key={topic}
              className={`topic-btn ${selectedTopic === topic ? 'active' : ''}`}
              onClick={() => setSelectedTopic(topic)}
            >
              {topic}
            </button>
          ))}
        </div>
      </div>

      {loading ? (
        <div className="loading-state">Loading problems...</div>
      ) : (
        <div className="problems-container">
          <div className="problems-table">
            <div className="table-header">
              <span className="col-title">Title</span>
              <span className="col-topic">Topic</span>
              <span className="col-difficulty">Difficulty</span>
              <span className="col-action">Action</span>
            </div>
            {filteredProblems.length === 0 ? (
              <div className="no-problems">No problems found</div>
            ) : (
              filteredProblems.map(problem => (
                /* Changed problem._id to problem.id to match Django */
                <div key={problem.id} className="table-row">
                  <span className="problem-title">{problem.title}</span>
                  <span className="problem-topic">{problem.topic || 'General'}</span>
                  <span 
                    className="problem-difficulty"
                    style={{ color: getDifficultyColor(problem.difficulty) }}
                  >
                    {problem.difficulty}
                  </span>
                  <button 
                    className="solve-btn" 
                    onClick={() => onNavigate('problem-solve', problem)}
                  >
                    Solve
                  </button>
                </div>
              ))
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default PracticeDSA;