import React, { useState } from 'react';
import { Player } from '@lottiefiles/react-lottie-player';

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
      <Player
        autoplay
        loop
        src="https://assets10.lottiefiles.com/packages/lf20_bhebjzpu.json"
        style={{ height: '250px', width: '250px', margin: '-20px 0' }}
      >
      </Player>
      
      <div className="glass-card login-card" style={{ maxWidth: '400px', width: '100%', marginTop: '1rem' }}>
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
