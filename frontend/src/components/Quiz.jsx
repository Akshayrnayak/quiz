import React, { useState, useEffect } from 'react';

const Quiz = ({ questions, category, onFinish }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [selectedOption, setSelectedOption] = useState(null);
  const [isAnswered, setIsAnswered] = useState(false);
  const [timeLeft, setTimeLeft] = useState(60);
  
  useEffect(() => {
    if (isAnswered) return;
    
    if (timeLeft <= 0) {
       setIsAnswered(true);
       return;
    }

    const timer = setInterval(() => {
      setTimeLeft(prev => prev - 1);
    }, 1000);

    return () => clearInterval(timer);
  }, [timeLeft, isAnswered]);

  if (!questions || questions.length === 0) {
    return (
      <div className="glass-card animate-fade-in">
        <div className="loader"></div>
        <p style={{marginTop: '1rem'}}>Loading questions...</p>
      </div>
    );
  }

  const question = questions[currentIndex];
  const progress = (currentIndex / questions.length) * 100;

  const handleOptionClick = (index) => {
    if (isAnswered) return;
    
    setSelectedOption(index);
    setIsAnswered(true);

    if (index === question.correct_answer) {
      setScore(prev => prev + 1);
    }
  };

  const nextQuestion = () => {
    if (currentIndex < questions.length - 1) {
      setCurrentIndex(prev => prev + 1);
      setSelectedOption(null);
      setIsAnswered(false);
      setTimeLeft(60);
    } else {
      onFinish(score, questions.length);
    }
  };

  return (
    <div className="glass-card animate-fade-in">
      <div className="flex-between">
        <span className="category-badge">{category ? category.toUpperCase() : ''}</span>
        
        <div className="timer-container timer-icon">
           ⏳ 00:{timeLeft.toString().padStart(2, '0')}
        </div>

        <span className="question-counter">Question {currentIndex + 1} of {questions.length}</span>
      </div>

      <div className="progress-bar-container">
        <div className="progress-bar" style={{ width: `${progress}%` }}></div>
      </div>

      <div className="question-text">
        {question.text}
      </div>

      <div className="options-container" style={{ marginBottom: isAnswered ? '1rem' : '0' }}>
        {question.options.map((option, index) => {
          let btnClass = "option-btn";
          if (isAnswered) {
             if (index === question.correct_answer) {
               btnClass += " correct";
             } else if (index === selectedOption) {
               btnClass += " incorrect";
             }
          }

          return (
            <button
              key={index}
              className={btnClass}
              onClick={() => handleOptionClick(index)}
              disabled={isAnswered}
            >
              <span>{option}</span>
            </button>
          );
        })}
      </div>

      {isAnswered && question.explanation && (
        <div className="explanation-card animate-slide-up" style={{
          background: 'rgba(251, 191, 36, 0.1)',
          borderLeft: '4px solid #fbbf24',
          padding: '1.2rem',
          borderRadius: '0 8px 8px 0',
          textAlign: 'left',
          marginBottom: '2rem'
        }}>
           <h4 style={{ margin: '0 0 0.5rem 0', color: '#fbbf24', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
             <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
             Instructor's Note
            </h4>
           <p style={{ margin: 0, fontSize: '1.05rem', color: 'var(--text-main)', lineHeight: '1.5' }}>
             {question.explanation}
           </p>
        </div>
      )}

      {isAnswered && (
        <button className="btn animate-fade-in" onClick={nextQuestion} style={{ width: '100%', fontSize: '1.2rem', padding: '1rem' }}>
          {currentIndex === questions.length - 1 ? "Finish Quiz 🏁" : "Next Question 👉"}
        </button>
      )}
    </div>
  );
};

export default Quiz;
