import React, { useState } from 'react';

const Login = ({ onLogin }) => {
  const [name, setName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (name.trim()) {
      onLogin(name.trim());
    }
  };

  return (
    <div className="login-container animate-fade-in">
      <div className="student-graphic">
        <div className="head"></div>
        <div className="body"></div>
        <div className="laptop">
          <div className="screen"></div>
          <div className="base"></div>
        </div>
      </div>
      
      <div className="glass-card login-card" style={{ maxWidth: '400px', width: '100%' }}>
        <h2>Welcome Student! 🎓</h2>
        <p className="subtitle">Enter your name to start learning and join the leaderboard.</p>
        
        <form onSubmit={handleSubmit} className="login-form">
          <input 
            type="text" 
            placeholder="Your Name..." 
            value={name} 
            onChange={(e) => setName(e.target.value)} 
            className="modern-input"
            required
            autoFocus
          />
          <button type="submit" className="btn login-btn">Let's Go! 🚀</button>
        </form>
      </div>
    </div>
  );
};

export default Login;
