import React, { useState, useEffect } from 'react';
import '../../styles/Quiz.css';

// 1. Static data moved to a constant to avoid "not defined" errors
const ARRAYS_DUMMY_DATA = [
  {
    id: 1,
    question: "What is the time complexity of accessing an element in an array by index?",
    options: ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
    correct_answer: "O(1)"
  },
  {
    id: 2,
    question: "Which of the following is true about arrays?",
    options: [
      "Arrays can store elements of different data types",
      "Arrays have fixed size in most programming languages",
      "Arrays use O(n) space for n elements",
      "Both B and C"
    ],
    correct_answer: "Both B and C"
  },
  {
    id: 3,
    question: "What is the time complexity of inserting an element at the beginning of an array?",
    options: ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
    correct_answer: "O(n)"
  },
  {
    id: 4,
    question: "Which algorithm is best for searching in a sorted array?",
    options: ["Linear Search", "Binary Search", "Jump Search", "Interpolation Search"],
    correct_answer: "Binary Search"
  },
  {
    id: 5,
    question: "What is the space complexity of an array of size n?",
    options: ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
    correct_answer: "O(n)"
  }
];

function Quiz({ topic, customQuestions, onNavigate }) {
  const [questions, setQuestions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState({});
  const [loading, setLoading] = useState(true);
  const [showResults, setShowResults] = useState(false);
  const [score, setScore] = useState(0);

  const saveQuizResult = async (finalScore, totalQuestions) => {
    try {
      const response = await fetch('http://localhost:8000/api/quiz/submit/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: "include", // Required for session/cookie auth
        body: JSON.stringify({ 
          score: finalScore, 
          total: totalQuestions 
        }),
      });
      
      if (!response.ok) {
        console.error("Failed to save quiz results to the server.");
      }
    } catch (error) {
      console.error('Error saving quiz result:', error);
    }
  };

  useEffect(() => {
    const fetchQuestions = async () => {
      setLoading(true);
      try {
        // Priority 1: AI Generated Custom Questions
        if (topic === 'Custom' && customQuestions && customQuestions.length > 0) {
          setQuestions(customQuestions);
        } 
        // Priority 2: Hardcoded Arrays Topic
        else if (topic === 'Arrays') {
          setQuestions(ARRAYS_DUMMY_DATA);
        } 
        // Priority 3: Fetch from Django Backend for other topics
        else {
          const response = await fetch(`http://localhost:8000/api/quiz/questions/?topic=${topic}`);
          if (response.ok) {
            const data = await response.json();
            setQuestions(data);
          } else {
            setQuestions([]);
          }
        }
      } catch (error) {
        console.error('Error fetching questions:', error);
        setQuestions([]);
      } finally {
        setLoading(false);
      }
    };

    fetchQuestions();
  }, [topic, customQuestions]);

  const handleAnswerSelect = (answer) => {
    setSelectedAnswers({
      ...selectedAnswers,
      [currentQuestion]: answer
    });
  };

  const handleNext = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    }
  };

  const handlePrevious = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1);
    }
  };

const handleSubmit = () => {
    let correctCount = 0;
    questions.forEach((q, index) => {
      const actualCorrectAnswer = q.correct_answer || q.answer;
      if (selectedAnswers[index] === actualCorrectAnswer) {
        correctCount++;
      }
    });

    setScore(correctCount);
    setShowResults(true);

    // Trigger the API call here
    saveQuizResult(correctCount, questions.length);
  };

  if (loading) {
    return <div className="quiz-loading">Loading quiz...</div>;
  }

  if (questions.length === 0) {
    return (
      <div className="quiz-loading">
        <p>No questions available for this topic.</p>
        <button className="back-btn" onClick={() => onNavigate('take-quiz')}>
          Back to Topics
        </button>
      </div>
    );
  }

  if (showResults) {
    return (
      <div className="quiz-results-container">
        <div className="results-card">
          <h1>Quiz Completed!</h1>
          <div className="score-display">
            <div className="score-circle">
              <span className="score-text">{score}/{questions.length}</span>
            </div>
          </div>
          <p className="score-percentage">
            You scored {Math.round((score / questions.length) * 100)}%
          </p>
          <div className="results-actions">
            <button className="retry-btn" onClick={() => window.location.reload()}>
              Retry Quiz
            </button>
            <button className="back-btn" onClick={() => onNavigate('take-quiz')}>
              Back to Topics
            </button>
          </div>
        </div>
      </div>
    );
  }

  const question = questions[currentQuestion];

  return (
    <div className="quiz-container">
      <div className="quiz-header">
        <button className="quiz-back-btn" onClick={() => onNavigate('take-quiz')}>
          ← Back
        </button>
        <h2>{topic} Quiz</h2>
        <div className="progress-info">
          <div className="progress-bar">
            <div 
              className="progress-fill" 
              style={{ width: `${((currentQuestion + 1) / questions.length) * 100}%` }}
            ></div>
          </div>
          <p className="question-counter">
            Question {currentQuestion + 1} of {questions.length}
          </p>
        </div>
      </div>

      <div className="question-card">
        <h3 className="question-text">{question.question}</h3>
        <div className="options-container">
          {question.options.map((option, index) => (
            <button
              key={index}
              className={`option-btn ${selectedAnswers[currentQuestion] === option ? 'selected' : ''}`}
              onClick={() => handleAnswerSelect(option)}
            >
              <span className="option-label">{String.fromCharCode(65 + index)}</span>
              <span className="option-text">{option}</span>
            </button>
          ))}
        </div>
      </div>

      <div className="quiz-navigation">
        <button 
          className="nav-btn prev-btn" 
          onClick={handlePrevious}
          disabled={currentQuestion === 0}
        >
          Previous
        </button>
        {currentQuestion === questions.length - 1 ? (
          <button 
            className="nav-btn submit-btn" 
            onClick={handleSubmit}
            disabled={Object.keys(selectedAnswers).length !== questions.length}
          >
            Submit Quiz
          </button>
        ) : (
          <button 
            className="nav-btn next-btn" 
            onClick={handleNext}
          >
            Next
          </button>
        )}
      </div>
    </div>
  );
}

export default Quiz;