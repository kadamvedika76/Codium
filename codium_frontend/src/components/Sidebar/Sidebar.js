import React from 'react';
import '../../styles/Sidebar.css';
import homeIcon from '../../icons/home.png';
import problemSolvingIcon from '../../icons/problem-solving.png';
import quizGameIcon from '../../icons/quiz-game.png';
import trophyIcon from '../../icons/trophy.png';
import userIcon from '../../icons/user.png';
import PracticeDSA from '../../pages/PracticeDSA/PracticeDSA';

function Sidebar({ isOpen, closeSidebar, isLoggedIn, handleLogout, userData, onNavigate }) {
  const handleNavigation = (page, section = null) => {
    closeSidebar();
    onNavigate(page, section);
  };

  const isAdmin = userData && userData.username === 'Vedika';

  return (
    <>
      {isOpen && <div className="overlay" onClick={closeSidebar}></div>}
      
      <div className={`sidebar ${isOpen ? 'open' : ''}`}>
        <div className="sidebar-header">
          <h2>Menu</h2>
          <button className="close-btn" onClick={closeSidebar}>×</button>
        </div>

        <nav className="sidebar-nav">
          <button className="sidebar-link" onClick={(e) => { e.preventDefault(); handleNavigation('home'); }}>
            <img src={homeIcon} alt="Home" className="sidebar-icon" /> Home
          </button>
          <button className="sidebar-link" onClick={(e) => { e.preventDefault(); handleNavigation('practice-dsa'); }}>
            <img src={problemSolvingIcon} alt="Problems" className="sidebar-icon" /> Problems
          </button>
          <button className="sidebar-link" onClick={(e) => { e.preventDefault(); handleNavigation('take-quiz'); }}>
            <img src={quizGameIcon} alt="Quiz" className="sidebar-icon" /> Quiz
          </button>

          {isLoggedIn && isAdmin && (
            <button className="sidebar-link" onClick={(e) => { e.preventDefault(); handleNavigation('AddProblem'); }}>
              <img src={problemSolvingIcon} alt="Add Problem" className="sidebar-icon" style={{ filter: 'hue-rotate(90deg)' }} /> 
              Create Problem
            </button>
          )}
          
          {isLoggedIn && (
            <>
              <button className="sidebar-link" onClick={(e) => { e.preventDefault(); handleNavigation('profile'); }}>
                <img src={userIcon} alt="Profile" className="sidebar-icon" /> Profile
              </button>
            </>
          )}
        </nav>

        {isLoggedIn && (
          <div className="sidebar-footer">
            <button className="logout-btn" onClick={handleLogout}>
              Logout
            </button>
          </div>
        )}
      </div>
    </>
  );
}

export default Sidebar;