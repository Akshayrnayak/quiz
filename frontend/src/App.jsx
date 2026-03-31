import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Header from './components/Header';
import Home from './components/Home';
import Quiz from './components/Quiz';
import ScoreBoard from './components/ScoreBoard';
import Login from './components/Login';
import Leaderboard from './components/Leaderboard';
import './index.css';

const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';

function App() {
  const [username, setUsername] = useState(null);
  const [categories, setCategories] = useState([]);
  const [currentCategory, setCurrentCategory] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [quizState, setQuizState] = useState('login'); // 'login', 'home', 'quiz', 'score', 'leaderboard'
  const [scoreData, setScoreData] = useState({ score: 0, total: 0 });
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchCategories();
  }, []);

  const fetchCategories = () => {
    setError(null);
    axios.get(`${API_URL}/api/categories`)
      .then(res => setCategories(res.data))
      .catch(err => {
        console.error("Error fetching categories:", err);
        setError(`Failed to connect to the backend (${API_URL}). Please ensure the server is running.`);
      });
  };

  const handleLogin = (name) => {
    setUsername(name);
    setQuizState('home');
  };

  const handleLogout = () => {
    setUsername(null);
    setQuizState('login');
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

    axios.post(`${API_URL}/api/leaderboard`, {
      username: username,
      score: score,
      total: total,
      topic: currentCategory
    }).catch(err => console.error("Error posting score:", err));
  };

  const handleRestart = () => {
    if (!username) return;
    setQuizState('home');
    setCurrentCategory(null);
    setQuestions([]);
    fetchCategories();
  };

  const handleLeaderboardClick = () => {
    if (!username) return;
    setQuizState('leaderboard');
  };

  return (
    <>
      <Header 
        onHomeClick={handleRestart} 
        onLeaderboardClick={handleLeaderboardClick}
        username={username}
        onLogout={handleLogout}
      />
      
      <main>
        {quizState === 'login' && (
          <Login onLogin={handleLogin} />
        )}
        {quizState === 'home' && (
          <Home 
            categories={categories} 
            onSelectCategory={handleSelectCategory} 
            error={error}
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
            onViewLeaderboard={handleLeaderboardClick}
          />
        )}
        {quizState === 'leaderboard' && (
          <Leaderboard />
        )}
      </main>
    </>
  );
}

export default App;
