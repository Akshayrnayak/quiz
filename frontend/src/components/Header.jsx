import React from 'react';

const Header = ({ onHomeClick, onLeaderboardClick, username, onLogout }) => {
  return (
    <header className="header-container animate-fade-in">
      <div className="header-content" onClick={username ? onHomeClick : undefined} style={{ cursor: username ? 'pointer' : 'default' }}>
        <div className="logo-icon">&lt;/&gt;</div>
        <span className="logo-text">W3Quiz Pro Max</span>
      </div>
      
      {username && (
        <nav className="header-nav">
          <span className="user-greeting">Hey, {username}! 👋</span>
          <button className="nav-btn" onClick={onHomeClick}>Topics</button>
          <button className="nav-btn" onClick={onLeaderboardClick}>🏅 Leaderboard</button>
          <button className="nav-btn logout-btn" onClick={onLogout}>Exit</button>
        </nav>
      )}
    </header>
  );
};

export default Header;
