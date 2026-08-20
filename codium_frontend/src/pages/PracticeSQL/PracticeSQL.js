import React, { useState, useEffect } from 'react';
import '../../styles/PracticeSQL.css';

function PracticeSQL({ onNavigate }) { // Added onNavigate prop
  const [problems, setProblems] = useState([]);
  const [filteredProblems, setFilteredProblems] = useState([]);
  const [selectedDifficulty, setSelectedDifficulty] = useState('All');
  const [loading, setLoading] = useState(true);

  const difficulties = ['All', 'Easy', 'Medium', 'Hard'];

  useEffect(() => {
    fetchProblems();
  }, []);

  useEffect(() => {
    // We filter by difficulty AND ensure we are only showing SQL problems
    let result = problems;
    
    if (selectedDifficulty !== 'All') {
      result = result.filter(p => p.difficulty?.toLowerCase() === selectedDifficulty.toLowerCase());
    }
    
    setFilteredProblems(result);
  }, [selectedDifficulty, problems]);

  const fetchProblems = async () => {
    try {
      // Pointing to your Django API
      const response = await fetch('http://localhost:8000/api/problems/');
      const data = await response.json();
      
      // Filter the general problems to only show 'SQL' topic problems
      const sqlOnly = data.filter(p => p.topic?.toLowerCase() === 'sql');
      
      setProblems(sqlOnly);
      setFilteredProblems(sqlOnly);
    } catch (error) {
      console.error('Error fetching SQL problems:', error);
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
    <div className="practice-sql-container">
      <div className="practice-sql-header">
        <h1>Practice SQL Problems</h1>
        <p>Master database queries and SQL concepts with real-world problems</p>
      </div>

      <div className="topics-section">
        <div className="topics-filter">
          {difficulties.map(difficulty => (
            <button
              key={difficulty}
              className={`topic-btn ${selectedDifficulty === difficulty ? 'active' : ''}`}
              onClick={() => setSelectedDifficulty(difficulty)}
            >
              {difficulty}
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
              <div className="no-problems">No SQL problems found. Add some from the Creator Dashboard!</div>
            ) : (
              filteredProblems.map(problem => (
                // Changed _id to id to match Django
                <div key={problem.id} className="table-row">
                  <span className="problem-title">{problem.title}</span>
                  <span className="problem-topic">{problem.topic}</span>
                  <span 
                    className="problem-difficulty"
                    style={{ color: getDifficultyColor(problem.difficulty) }}
                  >
                    {problem.difficulty}
                  </span>
                  {/* Link to the Workspace */}
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

export default PracticeSQL;