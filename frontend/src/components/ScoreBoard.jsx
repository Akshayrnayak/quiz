import React from 'react';

const ScoreBoard = ({ score, total, onRestart }) => {
  const percentage = Math.round((score / total) * 100);
  
  let message = "Good effort!";
  if (percentage === 100) message = "Perfect Score! Amazing!";
  else if (percentage >= 80) message = "Great job!";
  else if (percentage >= 50) message = "Not bad, keep learning!";

  return (
    <div className="glass-card animate-fade-in">
      <h2>Quiz Completed!</h2>
      <p className="subtitle">{message}</p>
      
      <div className="score-circle">
        {percentage}%
      </div>

      <div className="score-details">
        You scored <strong>{score}</strong> out of <strong>{total}</strong> correctly.
      </div>

      <button className="btn" onClick={onRestart}>
        Retake Quiz
      </button>
    </div>
  );
};

export default ScoreBoard;
