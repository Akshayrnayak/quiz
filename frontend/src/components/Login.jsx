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
    <div className="login-split-container animate-fade-in">
      <div className="login-left-pane">
        <h1 className="hero-text">Master Web Development.<br />Compete Globally.</h1>
        <p className="hero-subtext">Join 10,000+ developers ranking up</p>
        <Player
          autoplay
          loop
          src="https://assets10.lottiefiles.com/packages/lf20_bhebjzpu.json"
          style={{ height: '350px', width: '350px', marginTop: '2rem' }}
        />
      </div>

      <div className="login-right-pane">
        <div className="glass-card login-card" style={{ maxWidth: '450px', width: '100%', padding: '3rem' }}>
          <h2 style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>Get Started 🚀</h2>
          <p className="subtitle" style={{ marginBottom: '2rem', fontSize: '1rem' }}>Sign in to track your mastery scores.</p>

          <div className="social-login">
            <button className="oauth-btn" type="button" onClick={() => alert("Just a demo button!")}>
              <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="Github" width={20} style={{ filter: 'invert(1)' }} />
              <span>Continue with GitHub</span>
            </button>
            <button className="oauth-btn" type="button" onClick={() => alert("Just a demo button!")}>
              <img src="https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg" alt="Google" width={20} />
              <span>Continue with Google</span>
            </button>
          </div>

          <div className="divider">
            <span>or continue with username</span>
          </div>

          <form onSubmit={handleSubmit} className="login-form">
            <label style={{ textAlign: 'left', marginBottom: '0.5rem', fontWeight: '600', color: 'var(--text-muted)' }}>Public Username</label>
            <input
              type="text"
              placeholder="e.g. CodeNinja99"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="modern-input"
              required
              autoFocus
            />
            <button type="submit" className="btn login-btn" style={{ padding: '1rem' }}>Join Leaderboard</button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Login;
