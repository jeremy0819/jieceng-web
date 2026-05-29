
import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import HomeView from './views/HomeView';
import WorkView from './views/WorkView';
import ExpertiseView from './views/ExpertiseView';
import EvaluationView from './views/EvaluationView';
import AboutView from './views/AboutView';
import SessionsView from './views/SessionsView';
import AIChat from './components/AIChat';
import Footer from './components/Footer';

const App: React.FC = () => {
  const [currentPage, setCurrentPage] = useState<'home' | 'work' | 'expertise' | 'evaluation' | 'about' | 'sessions'>('home');

  // 當頁面切換時，平滑滾動至頂端
  useEffect(() => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }, [currentPage]);

  const renderPage = () => {
    switch (currentPage) {
      case 'work': return <div key="work" className="view-transition"><WorkView /></div>;
      case 'expertise': return <div key="expertise" className="view-transition"><ExpertiseView /></div>;
      case 'evaluation': return <div key="evaluation" className="view-transition"><EvaluationView /></div>;
      case 'about': return <div key="about" className="view-transition"><AboutView /></div>;
      case 'sessions': return <div key="sessions" className="view-transition"><SessionsView /></div>;
      default: return <div key="home" className="view-transition"><HomeView onNavigate={setCurrentPage} /></div>;
    }
  };

  return (
    <div className="min-h-screen relative selection:bg-emerald-100 selection:text-emerald-900 flex flex-col">
      <Navbar onNavigate={setCurrentPage} currentPage={currentPage} />
      
      <main className="flex-grow">
        {renderPage()}
      </main>

      <Footer onNavigate={setCurrentPage} />
      <AIChat />

      <style>{`
        .view-transition {
          animation: fade-in-scale 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        @keyframes fade-in-scale {
          from { 
            opacity: 0; 
            transform: translateY(10px);
          }
          to { 
            opacity: 1; 
            transform: translateY(0);
          }
        }
      `}</style>
    </div>
  );
};

export default App;
