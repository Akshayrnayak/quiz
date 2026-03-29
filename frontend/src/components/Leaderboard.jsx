import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Leaderboard = () => {
  const [board, setBoard] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/leaderboard')
      .then(res => {
        setBoard(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Leaderboard fetch error:", err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="glass-card animate-fade-in" style={{ maxWidth: '800px', margin: '0 auto', textAlign: 'left' }}>
      <h2 style={{ textAlign: 'center', marginBottom: '2rem' }}>🏆 Global Leaderboard</h2>
      
      {loading ? (
        <div className="loader"></div>
      ) : board.length === 0 ? (
        <p style={{ textAlign: 'center', color: 'var(--text-muted)' }}>No scores yet! Be the first to take a quiz.</p>
      ) : (
        <div className="table-responsive" style={{ overflowX: 'auto' }}>
          <table className="leaderboard-table">
            <thead>
              <tr>
                <th>Rank</th>
                <th>Student</th>
                <th>Topic</th>
                <th>Score</th>
                <th>Accuracy</th>
              </tr>
            </thead>
            <tbody>
              {board.map((entry, idx) => (
                <tr key={idx} className={idx < 3 ? `top-${idx + 1}` : ''}>
                  <td>#{idx + 1}</td>
                  <td><strong>{entry.username}</strong></td>
                  <td><span className="category-badge">{entry.topic.toUpperCase()}</span></td>
                  <td>{entry.score} / {entry.total}</td>
                  <td>{Math.round((entry.score / entry.total) * 100)}%</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default Leaderboard;
