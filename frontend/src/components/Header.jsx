import React from 'react';

const Header = ({ onHomeClick }) => {
  return (
    <header className="header-container animate-fade-in">
      <div className="header-content" onClick={onHomeClick} style={{ cursor: 'pointer' }}>
        <div className="logo-icon">&lt;/&gt;</div>
        <span className="logo-text">W3Quiz Pro</span>
      </div>
      <nav>
        <button className="nav-btn" onClick={onHomeClick}>Home</button>
      </nav>
    </header>
  );
};

export default Header;
