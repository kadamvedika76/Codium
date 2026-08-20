import React from 'react';
import '../../styles/DSASheets.css';
import arraysImg from '../../images/photo-1516116216624-53e697fedbea.jpeg';
import stringsImg from '../../images/photo-1504639725590-34d0984388bd.jpeg';
import stackImg from '../../images/photo-1555066931-4365d14bab8c.jpeg';
import queueImg from '../../images/photo-1544383835-bda2bc66a55d.jpeg';
import linkedListsImg from '../../images/photo-1460925895917-afdab827c52f.jpeg';
import treesImg from '../../images/photo-1552664730-d307ca884978.jpeg';
import graphsImg from '../../images/photo-1606326608606-aa0b62935f2b.jpeg';

function DSASheets({ onNavigate }) {
  const dsaTopics = [
    { 
      title: "Arrays", 
      desc: "Learn array operations and algorithms", 
      img: arraysImg
    },
    { 
      title: "Strings", 
      desc: "Master string manipulation techniques", 
      img: stringsImg
    },
    { 
      title: "Stack", 
      desc: "Understand stack data structure", 
      img: stackImg
    },
    { 
      title: "Queue", 
      desc: "Explore queue operations", 
      img: queueImg
    },
    { 
      title: "Linked Lists", 
      desc: "Deep dive into linked lists", 
      img: linkedListsImg
    },
    { 
      title: "Trees", 
      desc: "Learn tree traversals and operations", 
      img: treesImg
    },
    { 
      title: "Graphs", 
      desc: "Master graph algorithms", 
      img: graphsImg
    }
  ];

  return (
    <div className="dsa-sheets-container">
      <div className="dsa-sheets-header">
        <h1>DSA Learning Sheets</h1>
        <p>Select a topic to explore comprehensive learning materials and concepts</p>
      </div>

      <div className="dsa-topics-grid">
        {dsaTopics.map((topic, index) => (
          <div 
            key={index}
            className="dsa-topic-box"
            style={{ backgroundImage: `url(${topic.img})` }}
            onClick={() => onNavigate('learn-topic', { topic: topic.title, category: 'dsa' })}
          >
            <div className="dsa-box-overlay">
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

export default DSASheets;
