import React from 'react';

const Home = ({ categories, onSelectCategory, error }) => {
  return (
    <div className="glass-card animate-fade-in">
      <h1>Quiz App</h1>
      <p className="subtitle">Test your web development skills just like W3Schools!</p>
      
      {error ? (
        <div className="error-message">
          <p>{error}</p>
          <p style={{ fontSize: '0.8rem', marginTop: '10px', color: '#ffcccb' }}>
            Tip: If you've deployed this app, make sure your frontend environment variables (like VITE_API_URL) point to the deployed backend URL, not localhost.
          </p>
        </div>
      ) : categories.length === 0 ? (
        <div className="loader"></div>
      ) : (
        <>
          <h2>Select a Topic</h2>
          <div className="topics-grid">
            {categories.map((cat) => (
              <div 
                key={cat.id} 
                className="topic-card"
                onClick={() => onSelectCategory(cat.id)}
              >
                <h3>{cat.title}</h3>
                <p>{cat.description}</p>
              </div>
            ))}
          </div>
        </>
      )}
    </div>
  );
};

export default Home;
