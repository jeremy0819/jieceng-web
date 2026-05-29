
import React, { useState, useEffect } from 'react';

interface NavbarProps {
  onNavigate: (page: any) => void;
  currentPage: string;
}

const Navbar: React.FC<NavbarProps> = ({ onNavigate, currentPage }) => {
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => setIsScrolled(window.scrollY > 50);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const links = [
    { id: 'work', label: '建案作品' },
    { id: 'expertise', label: 'iHome 5.0 工法' },
    { id: 'evaluation', label: '開發評估' },
    { id: 'sessions', label: '說明會動態' },
    { id: 'about', label: '品牌故事' },
  ];

  return (
    <nav className={`fixed top-0 left-0 w-full z-50 transition-all duration-500 ${isScrolled ? 'bg-white/80 backdrop-blur-md py-4 shadow-sm' : 'bg-transparent py-8'}`}>
      <div className="max-w-7xl mx-auto px-6 flex justify-between items-center">
        <button onClick={() => onNavigate('home')} className="text-xl font-bold tracking-tighter uppercase group flex items-center space-x-2">
          <span className="bg-emerald-600 text-white w-8 h-8 flex items-center justify-center rounded-lg">傑</span>
          <span>傑丞<span className="text-emerald-600 transition-colors group-hover:text-black">建築</span></span>
        </button>
        <div className="hidden md:flex space-x-10 items-center">
          {links.map((item) => (
            <button 
              key={item.id} 
              onClick={() => onNavigate(item.id)}
              className={`text-[10px] uppercase tracking-[0.2em] font-bold transition-colors ${currentPage === item.id ? 'text-emerald-600' : 'text-neutral-500 hover:text-black'}`}
            >
              {item.label}
            </button>
          ))}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
