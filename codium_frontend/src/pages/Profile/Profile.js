import React, { useState, useEffect, useCallback } from 'react';
import '../../styles/Profile.css';

function Profile({ userData }) {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

const fetchUserStats = useCallback(async () => {
  try {
    const response = await fetch('http://localhost:8000/api/user/stats/', {
      method: 'GET',
      // This allows the browser to send your login cookie to Django
      credentials: 'include', 
      headers: {
        'Content-Type': 'application/json'
      }
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Stats received:", data); // Check your console to see the points!
      setStats(data);
    }
  } catch (error) {
    console.error('Error fetching user stats:', error);
  } finally {
    setLoading(false);
  }
}, []);

  useEffect(() => {
    fetchUserStats();
  }, [fetchUserStats]);

  if (loading) {
    return <div className="profile-loading">Loading profile...</div>;
  }

  return (
    <div className="profile-container">
      <div className="profile-content">
        <div className="profile-sidebar">
          <div className="profile-card">
            <div className="profile-avatar">
              {userData?.username?.charAt(0).toUpperCase() || 'U'}
            </div>
            <h2>{userData?.username || 'User'}</h2>
            <p className="profile-email">{userData?.email || 'user@example.com'}</p>
            <div className="profile-points-badge">
              ⭐ {stats?.points || 0} Points
            </div>
          </div>
        </div>

        <div className="profile-main">
          <div className="stats-section">
            <h3>My Progress</h3>
            <div className="stats-grid">
              <div className="stat-item">
                <div className="stat-info">
                  <div className="stat-number">{stats?.solved_count || 0}</div>
                  <div className="stat-label">Problems Solved</div>
                </div>
              </div>
              <div className="stat-item">
                <div className="stat-info">
                  <div className="stat-number">{stats?.quiz_count || 0}</div>
                  <div className="stat-label">Quizzes Completed</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Profile;