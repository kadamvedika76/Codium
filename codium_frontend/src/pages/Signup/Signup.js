import React, { useState, useEffect } from 'react';
import './Signup.css';

function Signup({ onSignup, onSwitchToLogin }) {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: ''
  });
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  

  

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSignup = async () => {
    if (!formData.username || !formData.email || !formData.password || !formData.confirmPassword) {
      alert('Please fill in all fields');
      return;
    }

    if (formData.username.length < 5) {
      alert('Username must be at least 5 characters');
      return;
    }

    if (formData.password.length < 6) {
      alert('Password must be at least 6 characters');
      return;
    }

    if (formData.password !== formData.confirmPassword) {
      alert('Passwords do not match');
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(formData.email)) {
      alert('Please enter a valid email');
      return;
    }

    try {
      // 1. Updated URL to match our Django 'api/signup/'
      const response = await fetch('http://localhost:8000/api/signup/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include', // Crucial for session cookies
        body: JSON.stringify({
          username: formData.username,
          email: formData.email,
          password: formData.password
        })
      });

      const data = await response.json();

      if (response.ok) {
        // data is now { "message": "...", "username": "...", "email": "..." }
        // We save this to localStorage so App.js sees it on refresh
        localStorage.setItem('userData', JSON.stringify(data));
        
        // This triggers the redirection in App.js
        onSignup(data); 
        
        // Remove the alert for a smoother "App" feel, or keep it if you prefer
      } else {
        alert(data.error || 'Signup failed');
      }

    } catch (error) {
      console.error("Signup Error:", error);
      // Fallback for demo mode
      const newUser = { username: formData.username, email: formData.email };
      localStorage.setItem('userData', JSON.stringify(newUser));
      onSignup(newUser);
      alert('Account created successfully! (Demo mode)');
    }
  };

  const handleLoginClick = (e) => {
    e.preventDefault();
    onSwitchToLogin();
  };

  return (
    <>
      

      <div className="signup-container">
        <div className="signup-box">
          <div className="logo">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
              <path 
                d="M7 8L3 11.6923L7 16M17 8L21 11.6923L17 16M14 4L10 20" 
                stroke="currentColor" 
                strokeWidth="2" 
                strokeLinecap="round" 
                strokeLinejoin="round"
              />
            </svg>
            <h1>Codium</h1>
          </div>

          <p className="subtitle">Create your account</p>

          <label htmlFor="username">Username</label>
          <input
            type="text"
            id="username"
            name="username"
            placeholder="(min 5 characters)"
            value={formData.username}
            onChange={handleChange}
          />

          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            placeholder="Enter your email"
            value={formData.email}
            onChange={handleChange}
          />

          <label htmlFor="password"> Create Password</label>
          <div className="password-box">
            <input
              type={showPassword ? 'text' : 'password'}
              id="password"
              name="password"
              placeholder=" (min 6 characters)"
              value={formData.password}
              onChange={handleChange}
            />
            <span 
              className="toggle-btn" 
              onClick={() => setShowPassword(!showPassword)}
            >
              {showPassword ? 'Hide' : 'Show'}
            </span>
          </div>

          <label htmlFor="confirmPassword">Confirm Password</label>
          <div className="password-box">
            <input
              type={showConfirmPassword ? 'text' : 'password'}
              id="confirmPassword"
              name="confirmPassword"
              placeholder="Re-enter your password"
              value={formData.confirmPassword}
              onChange={handleChange}
            />
            <span 
              className="toggle-btn" 
              onClick={() => setShowConfirmPassword(!showConfirmPassword)}
            >
              {showConfirmPassword ? 'Hide' : 'Show'}
            </span>
          </div>

          <button className="signup-btn" onClick={handleSignup}>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
              <path 
                d="M16 21V19C16 17.9391 15.5786 16.9217 14.8284 16.1716C14.0783 15.4214 13.0609 15 12 15H5C3.93913 15 2.92172 15.4214 2.17157 16.1716C1.42143 16.9217 1 17.9391 1 19V21M12.5 7C12.5 9.20914 10.7091 11 8.5 11C6.29086 11 4.5 9.20914 4.5 7C4.5 4.79086 6.29086 3 8.5 3C10.7091 3 12.5 4.79086 12.5 7ZM20 8V14M23 11H17" 
                stroke="currentColor" 
                strokeWidth="2" 
                strokeLinecap="round" 
                strokeLinejoin="round"
              />
            </svg>
            <span>Sign Up</span>
          </button>

          <p className="login-text">
            Already have an account? <a href="#" onClick={handleLoginClick}>Login</a>
          </p>
        </div>
      </div>
    </>
  );
}

export default Signup;