import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar/Navbar';
import Sidebar from './components/Sidebar/Sidebar';
import Login from './pages/login/Login';
import Signup from './pages/Signup/Signup';
import Home from './pages/Home/Home';
import PracticeDSA from './pages/PracticeDSA/PracticeDSA';
import PracticeSQL from './pages/PracticeSQL/PracticeSQL';
import TakeQuiz from './pages/TakeQuiz/TakeQuiz';
import Quiz from './pages/Quiz/Quiz';
import DSASheets from './pages/DSASheets/DSASheets';
import SQLSheets from './pages/SQLSheets/SQLSheets';
import LearnTopic from './pages/LearnTopic/LearnTopic';
import Profile from './pages/Profile/Profile';
import ProblemSolve from './pages/ProblemSolve/ProblemSolve';
import AddProblem from './pages/Add_Ques/AddProblem'; 
import CustomQuizUpload from './pages/CustomQuizUpload';
import './App.css';

function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [currentPage, setCurrentPage] = useState('home');  
  const [userData, setUserData] = useState(null);
  
  const [scrollToSection, setScrollToSection] = useState(null);
  const [selectedQuizTopic, setSelectedQuizTopic] = useState(null);
  const [learnTopicData, setLearnTopicData] = useState(null);
  const [selectedProblem, setSelectedProblem] = useState(null);
  const [customQuizData, setCustomQuizData] = useState(null);

  useEffect(() => {
    const storedUserData = localStorage.getItem('userData');
    
    if (storedUserData) {
      setIsLoggedIn(true);
      setUserData(JSON.parse(storedUserData));
      
      // Clear warnings by handling redirect logic properly
      if (currentPage === 'login' || currentPage === 'signup') {
        setCurrentPage('home');
      }
    }
  }, [currentPage]); // Added dependency to satisfy ESLint

  const toggleSidebar = () => setIsSidebarOpen(!isSidebarOpen);
  const closeSidebar = () => setIsSidebarOpen(false);

  const handleLogin = (user) => {
    setIsLoggedIn(true);
    setUserData(user);
    setCurrentPage('home');
  };

  const handleSignup = (user) => {
    setIsLoggedIn(true);
    setUserData(user);
    setCurrentPage('home');
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
    setUserData(null);
    localStorage.removeItem('authToken');
    localStorage.removeItem('userData');
    setCurrentPage('home'); 
    closeSidebar();
  };

  const switchToLogin = () => { setCurrentPage('login'); closeSidebar(); };
  const switchToSignup = () => { setCurrentPage('signup'); closeSidebar(); };
  const switchToHome = () => { setCurrentPage('home'); closeSidebar(); };

  const handleNavigation = (page, section = null) => {
    setCurrentPage(page);
    closeSidebar();
    
    if (section) {
      if (page === 'quiz') {
        if (typeof section === 'object') {
          setSelectedQuizTopic('Custom'); 
          setCustomQuizData(section.questions); 
        } else {
          setSelectedQuizTopic(section);
          setCustomQuizData(null); // Clear custom data for standard quizzes
        }
      } else if (page === 'learn-topic') {
        setLearnTopicData(section);
      } else if (page === 'problem-solve') {
        setSelectedProblem(section);
      } else {
        setTimeout(() => setScrollToSection(section), 100);
      }
    } else {
      setScrollToSection(null);
      setSelectedQuizTopic(null);
      setLearnTopicData(null);
    }
  };

  return (
    <div className="App">
      <Navbar 
        toggleSidebar={toggleSidebar} 
        isLoggedIn={isLoggedIn}
        userData={userData}
        currentPage={currentPage}
        onLoginClick={switchToLogin}
        onRegisterClick={switchToSignup}
        onLogoClick={switchToHome} 
        onProfileClick={() => handleNavigation('profile')}
      />
      
      <Sidebar 
        isOpen={isSidebarOpen} 
        closeSidebar={closeSidebar}
        isLoggedIn={isLoggedIn}
        handleLogout={handleLogout}
        userData={userData}
        onNavigate={handleNavigation}
      />
      
      <div className={`main-content ${isSidebarOpen ? 'shifted' : ''}`}>
        {!isLoggedIn && currentPage === 'login' && (
          <Login onLogin={handleLogin} onSwitchToSignup={switchToSignup} />
        )}

        {!isLoggedIn && currentPage === 'signup' && (
          <Signup onSignup={handleSignup} onSwitchToLogin={switchToLogin} />
        )}

        {currentPage === 'home' && (
          <Home 
            userData={userData} 
            isLoggedIn={isLoggedIn} 
            onLoginPrompt={switchToLogin}
            onRegisterPrompt={switchToSignup}
            onNavigate={handleNavigation}
            scrollToSection={scrollToSection}
          />
        )}

        {isLoggedIn && currentPage === 'practice-dsa' && (
          <PracticeDSA onNavigate={handleNavigation} />
        )}

        {isLoggedIn && currentPage === 'problem-solve' && (
          <ProblemSolve problem={selectedProblem} onNavigate={handleNavigation} />
        )}

        {isLoggedIn && currentPage === 'practice-sql' && (
          <PracticeSQL onNavigate={handleNavigation} />
        )}

        {isLoggedIn && currentPage === 'AddProblem' && (
          <AddProblem />
        )}

        {isLoggedIn && currentPage === 'take-quiz' && (
          <TakeQuiz onNavigate={handleNavigation} />
        )}

        {isLoggedIn && currentPage === 'custom-quiz-upload' && (
          <CustomQuizUpload onNavigate={handleNavigation} />
        )}

        {isLoggedIn && currentPage === 'quiz' && selectedQuizTopic && (
        <Quiz 
          topic={selectedQuizTopic} 
          customQuestions={customQuizData}
          onNavigate={setCurrentPage} 
        />
      )}

        {isLoggedIn && currentPage === 'dsa-sheets' && (
          <DSASheets onNavigate={handleNavigation} />
        )}

        {isLoggedIn && currentPage === 'sql-sheets' && (
          <SQLSheets onNavigate={handleNavigation} />
        )}

        {isLoggedIn && currentPage === 'learn-topic' && learnTopicData && (
          <LearnTopic 
            topic={learnTopicData.topic} 
            category={learnTopicData.category} 
            onNavigate={setCurrentPage} 
          />
        )}

        {isLoggedIn && currentPage === 'profile' && (
          <Profile userData={userData} />
        )}
      </div>
    </div>
  );
}

export default App;