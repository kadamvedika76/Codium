import React, { useState, useEffect } from 'react';
import './Navbar.css';

function Navbar({ 
  toggleSidebar, 
  isLoggedIn, 
  userData, 
  currentPage, // Added this prop from App.js
  onLoginClick, 
  onRegisterClick ,
  onLogoClick,     // Add this
  onProfileClick
}) {
  const [theme, setTheme] = useState('light');

  useEffect(() => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    setTheme(savedTheme);
    document.body.className = savedTheme;
  }, []);

  const toggleTheme = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    document.body.className = newTheme;
    localStorage.setItem('theme', newTheme);
  };

  // Logic: Hide buttons if logged in OR if currently on login/signup pages
  const shouldShowAuth = !isLoggedIn && currentPage !== 'login' && currentPage !== 'signup';

  return (
    <nav className="navbar">
      <div className="navbar-content">
        {/* Left: Hamburger */}
        <button className="hamburger" onClick={toggleSidebar}>
          <span></span>
          <span></span>
          <span></span>
        </button>

        {/* Center: Logo */}
        <div className="navbar-logo" style={{ cursor: 'pointer' }} onClick={onLogoClick}>
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M7 8L3 11.6923L7 16M17 8L21 11.6923L17 16M14 4L10 20" 
                  stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
          <span>Codium</span>
        </div>

        {/* Right Section */}
        <div className="navbar-right">
          
          {/* 1. Auth Buttons (Conditional) */}
          {shouldShowAuth && (
            <div className="auth-buttons">
              <button className="nav-btn login" onClick={onLoginClick}>
                Login
              </button>
              <button className="nav-btn register" onClick={onRegisterClick}>
                Register
              </button>
            </div>
          )}

          {/* 2. User Profile (Only if logged in) */}
          {isLoggedIn && (
            <div className="user-profile" style={{ cursor: 'pointer' }} onClick={onProfileClick}>
              <span className="nav-username">{userData?.username}</span>
              <div className="user-icon-circle">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
              </div>
            </div>
          )}

          {/* 3. Theme Toggle (Always visible) */}
          <button className="theme-toggle-btn" onClick={toggleTheme} aria-label="Toggle theme">
            {theme === 'light' ? (
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" 
                      stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
            ) : (
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                <circle cx="12" cy="12" r="5" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <line x1="12" y1="1" x2="12" y2="3" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <line x1="12" y1="21" x2="12" y2="23" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <line x1="4.22" y1="4.22" x2="5.64" y2="5.64" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <line x1="18.36" y1="18.36" x2="19.78" y2="19.78" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <line x1="1" y1="12" x2="3" y2="12" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <line x1="21" y1="12" x2="23" y2="12" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <line x1="4.22" y1="19.78" x2="5.64" y2="18.36" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <line x1="18.36" y1="5.64" x2="19.78" y2="4.22" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
            )}
          </button>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;