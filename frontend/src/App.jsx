import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Header from './components/Header';
import Home from './components/Home';
import Quiz from './components/Quiz';
import ScoreBoard from './components/ScoreBoard';
import './index.css';

const API_URL = 'http://127.0.0.1:8000';

function App() {
  const [categories, setCategories] = useState([]);
  const [currentCategory, setCurrentCategory] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [quizState, setQuizState] = useState('home'); // 'home', 'quiz', 'score'
  const [scoreData, setScoreData] = useState({ score: 0, total: 0 });

  useEffect(() => {
    fetchCategories();
  }, []);

  const fetchCategories = () => {
    axios.get(`${API_URL}/api/categories`)
      .then(res => setCategories(res.data))
      .catch(err => console.error("Error fetching categories:", err));
  };

  const handleSelectCategory = (categoryId) => {
    setCurrentCategory(categoryId);
    setQuizState('quiz');
    
    axios.get(`${API_URL}/api/questions/${categoryId}`)
      .then(res => {
        setQuestions(res.data.questions || []);
      })
      .catch(err => console.error("Error fetching questions:", err));
  };

  const handleFinishQuiz = (score, total) => {
    setScoreData({ score, total });
    setQuizState('score');
  };

  const handleRestart = () => {
    setQuizState('home');
    setCurrentCategory(null);
    setQuestions([]);
    // Refresh categories in case they were updated
    fetchCategories();
  };

  return (
    <>
      <Header onHomeClick={handleRestart} />
      
      <main>
        {quizState === 'home' && (
          <Home 
            categories={categories} 
            onSelectCategory={handleSelectCategory} 
          />
        )}
        {quizState === 'quiz' && (
          <Quiz 
            questions={questions} 
            category={currentCategory} 
            onFinish={handleFinishQuiz} 
          />
        )}
        {quizState === 'score' && (
          <ScoreBoard 
            score={scoreData.score} 
            total={scoreData.total} 
            onRestart={handleRestart} 
          />
        )}
      </main>
    </>
  );
}

export default App;
