import React from 'react';
import '../../styles/TakeQuiz.css';

function TakeQuiz({ onNavigate }) {
  const quizTopics = [
    { 
      title: "Arrays", 
      desc: "Test your array knowledge", 
      img: "https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=600"
    },
    { 
      title: "Strings", 
      desc: "Master string manipulation", 
      img: "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=600"
    },
    { 
      title: "Stack", 
      desc: "Challenge your stack skills", 
      img: "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600"
    },
    { 
      title: "Queue", 
      desc: "Queue concepts quiz", 
      img: "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600"
    },
    { 
      title: "Linked Lists", 
      desc: "Test linked list concepts", 
      img: "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600"
    },
    { 
      title: "Trees", 
      desc: "Tree traversal challenges", 
      img: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600"
    },
    { 
      title: "Graphs", 
      desc: "Graph algorithm quiz", 
      img: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600"
    },
        { 
      title: "Custom", 
      desc: "Custom quiz", 
      img: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600"
    }

  ];

  return (
    <div className="take-quiz-container">
      <div className="take-quiz-header">
        <h1>Choose Your Quiz Topic</h1>
        <p>Select a topic to test your knowledge and track your progress</p>
      </div>

      <div className="quiz-topics-grid">
        {quizTopics.map((topic, index) => (
          <div 
            key={index}
            className="quiz-topic-box"
            style={{ backgroundImage: `url(${topic.img})` }}
            onClick={() => {
              // ADD THIS LOGIC HERE
              if (topic.title === "Custom") {
                onNavigate('custom-quiz-upload'); // Go to upload page
              } else {
                onNavigate('quiz', topic.title); // Go to standard quiz
              }
            }}
          >
            <div className="quiz-box-overlay">
              <h3>{topic.title}</h3>
              <p>{topic.desc}</p>
              <button className="start-quiz-btn">
                {topic.title === "Custom" ? "Generate with AI →" : "Start Quiz →"}
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default TakeQuiz;
