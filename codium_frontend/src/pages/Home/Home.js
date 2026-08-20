import React from 'react';
import './Home.css';
import problemSolvingIcon from '../../icons/problem-solving.png';
import quizGameIcon from '../../icons/quiz-game.png';
import trophyIcon from '../../icons/trophy.png';

function Home({ userData, isLoggedIn, onLoginPrompt, onNavigate }) {
  const features = [
    {
      title: "Problem Solving",
      description: "Master coding challenges with our curated collection of problems. From beginner to advanced, practice algorithms, data structures, and problem-solving techniques.",
      image: "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&h=400&fit=crop",
      icon: problemSolvingIcon,
      link: "practice-dsa"
    },
    {
      title: "Quiz Challenges",
      description: "Test your knowledge with interactive quizzes covering various programming concepts. Track your progress and identify areas for improvement.",
      image: "https://images.unsplash.com/photo-1606326608606-aa0b62935f2b?w=600&h=400&fit=crop",
      icon: quizGameIcon,
      link: "take-quiz"
    }
  ];

  const practiceTopics = [
    { 
      title: "DSA Sheets", 
      desc: "Curated paths by experts", 
      img: "https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=600", 
      link: "dsa-sheets" 
    },
    { 
      title: "Practice DSA", 
      desc: "Topic-wise problems", 
      img: "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=600", 
      link: "practice-dsa" 
    },
    { 
      title: "SQL Sheets", 
      desc: "Database mastery guide", 
      img: "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600", 
      link: "sql-sheets" 
    }
  ];

  const handleAction = (link) => {
    if (!isLoggedIn) {
      onLoginPrompt();
    } else {
      onNavigate(link);
    }
  };

  return (
    <div className="home-container">
      {/* Welcome Section */}
      <div className="welcome-section">
        <h1>Welcome back, {userData?.username || 'Coder'}!</h1>
        <p className="welcome-subtitle">Ready to level up your coding skills?</p>
      </div>

      {/* Features Section */}
      <div className="features-section">
        <h2 className="features-heading">What We Offer</h2>
        
        {features.map((feature, index) => (
          <div 
            key={index} 
            className={`feature-card ${index % 2 === 1 ? 'reverse' : ''}`}
          >
            <div className="feature-content">
              {/* CHANGED: emoji string → <img> tag using imported icon */}
              <div className="feature-icon">
                <img src={feature.icon} alt={feature.title} className="sidebar-icon" />
              </div>
              <h3>{feature.title}</h3>
              <p>{feature.description}</p>
              <button className="feature-btn" onClick={() => handleAction(feature.link)}>
                Get Started →
              </button>
            </div>
            <div className="feature-image">
              <img src={feature.image} alt={feature.title} />
              <div className="image-overlay"></div>
            </div>
          </div>
        ))}

        {/* Practice Hub */}
        <h2 className="features-heading" style={{ marginTop: '80px' }}>Master Your Skills</h2>
        
        <div className="feature-card practice-main-card">
          <div className="practice-grid">
            {practiceTopics.map((topic, index) => (
              <div 
                key={index}
                className="practice-box"
                style={{ backgroundImage: `url(${topic.img})` }}
                onClick={() => handleAction(topic.link)}
              >
                <div className="box-overlay">
                  <h4>{topic.title}</h4>
                  <p>{topic.desc}</p>
                  {!isLoggedIn && <span className="lock-tag">🔒 Login to Unlock</span>}
                </div>
              </div>
            ))}
          </div>
        </div>

      </div>
    </div>
  );
}

export default Home;