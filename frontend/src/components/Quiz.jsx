import React, { useState, useEffect } from 'react';

const Quiz = ({ questions, category, onFinish }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [selectedOption, setSelectedOption] = useState(null);
  const [isAnswered, setIsAnswered] = useState(false);
  const [timeLeft, setTimeLeft] = useState(60); // 60 seconds per question or total? Let's do 60s per question for intensity
  
  useEffect(() => {
    // Timer logic
    if (isAnswered) return;
    
    if (timeLeft <= 0) {
       // Time's up! Auto-submit
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
      setTimeLeft(60); // Reset timer for next question
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

      <div className="options-container">
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

      {isAnswered && (
        <button className="btn animate-fade-in" onClick={nextQuestion}>
          {currentIndex === questions.length - 1 ? "Finish Quiz" : "Next Question"}
        </button>
      )}
    </div>
  );
};

export default Quiz;
