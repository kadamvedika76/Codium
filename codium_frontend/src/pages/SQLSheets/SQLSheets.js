import React from 'react';
import '../../styles/SQLSheets.css';
import basicsImg from '../../images/photo-1544383835-bda2bc66a55d.jpeg';
import queriesImg from '../../images/photo-1460925895917-afdab827c52f.jpeg';
import joinsImg from '../../images/photo-1504639725590-34d0984388bd.jpeg';
import aggregateImg from '../../images/photo-1606326608606-aa0b62935f2b.jpeg';

function SQLSheets({ onNavigate }) {
  const sqlTopics = [
    { 
      title: "Basics", 
      desc: "Learn SQL fundamentals and syntax", 
      img: basicsImg
    },
    { 
      title: "Queries and Operations", 
      desc: "Master SELECT, INSERT, UPDATE, DELETE", 
      img: queriesImg
    },
    { 
      title: "SQL Joins", 
      desc: "Understand different types of joins", 
      img: joinsImg
    },
    { 
      title: "Aggregate Functions", 
      desc: "Explore COUNT, SUM, AVG, MIN, MAX", 
      img: aggregateImg
    }
  ];

  return (
    <div className="sql-sheets-container">
      <div className="sql-sheets-header">
        <h1>SQL Learning Sheets</h1>
        <p>Select a topic to explore comprehensive SQL learning materials</p>
      </div>

      <div className="sql-topics-grid">
        {sqlTopics.map((topic, index) => (
          <div 
            key={index}
            className="sql-topic-box"
            style={{ backgroundImage: `url(${topic.img})` }}
            onClick={() => onNavigate('learn-topic', { topic: topic.title, category: 'sql' })}
          >
            <div className="sql-box-overlay">
              <h3>{topic.title}</h3>
              <p>{topic.desc}</p>
              <button className="learn-btn">Learn More →</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default SQLSheets;
