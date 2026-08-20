import React, { useState, useEffect } from 'react';
import './login.css';

function Login({ onLogin, onSwitchToSignup }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  

  
 

  const handleLogin = async () => {
  if (email === '' || password === '') {
    alert('Please fill in all fields');
    return;
  }

  try {
    const response = await fetch('http://localhost:8000/api/login/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include', // Important for Sessions!
      body: JSON.stringify({
        username: email, // Django expects 'username' (even if it's an email)
        password: password
      })
    });

    const data = await response.json();

    if (response.ok) {
      // We store the data returned from your Django view (message, username)
      localStorage.setItem('userData', JSON.stringify(data));
      onLogin(data); 
      alert('Login successful!');
    } else {
      alert(data.error || 'Invalid credentials');
    }
  } catch (error) {
    console.error("Login Error:", error);
    // Keep your catch block for demo mode if you want
  }
};

  const togglePassword = () => {
    setShowPassword(!showPassword);
  };

  const handleRegisterClick = (e) => {
    e.preventDefault();
    onSwitchToSignup();
  };

  return (
    <>
      
      <div className="login-container">
        <div className="login-box">
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

          <label htmlFor="email">Email or Username</label>
          <input
            type="text"
            id="email"
            placeholder="Enter your email or username"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <label htmlFor="password">Password</label>
          <div className="password-box">
            <input
              type={showPassword ? 'text' : 'password'}
              id="password"
              placeholder="Enter your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <span className="toggle-btn" onClick={togglePassword}>
              {showPassword ? 'Hide' : 'Show'}
            </span>
          </div>

          <button className="login-btn" onClick={handleLogin}>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
              <path 
                d="M14 8V6C14 4.89543 13.1046 4 12 4H5C3.89543 4 3 4.89543 3 6V18C3 19.1046 3.89543 20 5 20H12C13.1046 20 14 19.1046 14 18V16M10 12H21M21 12L18 9M21 12L18 15" 
                stroke="currentColor" 
                strokeWidth="2" 
                strokeLinecap="round" 
                strokeLinejoin="round"
              />
            </svg>
            <span>Login</span>
          </button>

          <p className="signup-text">
            Don't have an account? <a href="#" onClick={handleRegisterClick}>Register</a>
          </p>
        </div>
      </div>
    </>
  );
}

export default Login;