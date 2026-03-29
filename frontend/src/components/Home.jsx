import React from 'react';

const Home = ({ categories, onSelectCategory }) => {
  return (
    <div className="glass-card animate-fade-in">
      <h1>Quiz App</h1>
      <p className="subtitle">Test your web development skills just like W3Schools!</p>
      
      {categories.length === 0 ? (
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
