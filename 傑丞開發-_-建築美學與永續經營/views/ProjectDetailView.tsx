
import React, { useRef, useEffect } from 'react';
import { Project } from '../types';
import OptimizedImage from '../components/OptimizedImage';

interface ProjectDetailViewProps {
  project: Project;
  onBack: () => void;
}

const ProjectDetailView: React.FC<ProjectDetailViewProps> = ({ project, onBack }) => {
  const contentRef = useRef<HTMLDivElement>(null);

  // 禁止背後頁面滾動
  useEffect(() => {
    const originalStyle = window.getComputedStyle(document.body).overflow;
    document.body.style.overflow = 'hidden';
    return () => {
      document.body.style.overflow = originalStyle;
    };
  }, []);

  const scrollToSection = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  return (
    <div className="fixed inset-0 z-[100] flex items-center justify-center p-4 md:p-8">
      {/* 沉浸式遮罩 */}
      <div 
        className="absolute inset-0 bg-black/80 backdrop-blur-xl animate-fade-in cursor-pointer" 
        onClick={onBack}
      ></div>
      
      <div className="relative w-full max-w-7xl h-full max-h-[92vh] bg-white rounded-[3rem] shadow-2xl overflow-hidden flex flex-col md:flex-row animate-scale-up border border-white/20">
        
        {/* 關閉按鈕 */}
        <button 
          onClick={onBack}
          className="absolute top-8 right-8 z-[110] bg-white/10 backdrop-blur-md text-white md:text-black md:bg-white/80 p-4 rounded-full shadow-xl hover:bg-black hover:text-white transition-all border border-white/20 active:scale-95 group"
        >
          <svg className="w-5 h-5 group-hover:rotate-90 transition-transform duration-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>

        {/* 側邊欄導航 (桌面端) */}
        <div className="hidden lg:flex flex-col justify-between px-10 py-16 border-r border-neutral-100 bg-[#fafaf9] w-[280px]">
          <div className="space-y-12">
            <div className="space-y-4">
               <p className="text-[8px] font-bold uppercase tracking-[0.5em] text-emerald-600">Case Study</p>
               <h3 className="text-xl font-serif leading-tight">{project.title}</h3>
            </div>
            
            <nav className="flex flex-col space-y-8">
              {[
                { id: 'section-overview', label: '建案總覽' },
                { id: 'section-highlights', label: '核心亮點' },
                { id: 'section-tech', label: '技術參數' },
                { id: 'section-ihome', label: '工法導入' },
              ].map(section => (
                <button
                  key={section.id}
                  onClick={() => scrollToSection(section.id)}
                  className="group flex items-center space-x-6 text-left"
                >
                  <div className="w-1 h-1 bg-neutral-300 rounded-full group-hover:w-6 group-hover:bg-emerald-600 transition-all duration-300"></div>
                  <span className="text-[10px] font-bold uppercase tracking-widest text-neutral-400 group-hover:text-black transition-colors">{section.label}</span>
                </button>
              ))}
            </nav>
          </div>
          
          <div className="pt-10 border-t border-neutral-200">
             <div className="text-[8px] text-neutral-400 font-bold uppercase tracking-widest leading-relaxed">
                Jiecheng Development <br/>© 2024 Architectural Series
             </div>
          </div>
        </div>

        {/* 圖片區域 (左側/頂部) */}
        <div className="w-full lg:w-[45%] h-64 md:h-auto overflow-hidden relative group">
          <OptimizedImage src={project.imageUrl} alt={project.title} className="w-full h-full object-cover" />
          <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent opacity-100 md:opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-10">
             <p className="text-emerald-400 text-[10px] font-bold uppercase tracking-widest mb-2">Project Vision</p>
             <h4 className="text-white text-3xl font-serif">匠心。築夢</h4>
          </div>
        </div>

        {/* 內容滾動區 (右側) */}
        <div ref={contentRef} className="flex-1 overflow-y-auto p-10 md:p-24 bg-white scroll-smooth selection:bg-emerald-50">
          <div className="space-y-48">
            
            <section id="section-overview" className="space-y-12">
              <div className="flex items-center space-x-6">
                <span className="text-emerald-600 text-[10px] font-bold uppercase tracking-[0.4em] bg-emerald-50 px-5 py-2 rounded-full border border-emerald-100">{project.categoryLabel}</span>
                <div className="h-px flex-1 bg-neutral-100"></div>
                <span className="text-neutral-400 text-[10px] font-bold uppercase tracking-widest">{project.year} Selection</span>
              </div>
              
              <h2 className="text-5xl md:text-7xl font-serif text-neutral-900 leading-[1.1] tracking-tight">{project.title}</h2>
              
              <div className="flex flex-col md:flex-row gap-16">
                 <div className="flex-1">
                    <p className="text-xl text-neutral-500 font-light leading-relaxed first-letter:text-6xl first-letter:font-serif first-letter:mr-4 first-letter:float-left first-letter:text-emerald-700">
                      {project.details || project.description}
                    </p>
                 </div>
              </div>
            </section>

            {project.highlights && (
              <section id="section-highlights" className="space-y-16">
                <div className="flex items-center space-x-8">
                   <h3 className="text-xs font-bold uppercase tracking-[0.5em] text-neutral-300">Case Highlights</h3>
                   <div className="h-px flex-1 bg-neutral-100"></div>
                </div>
                
                <div className="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-16">
                  {project.highlights.map((h, i) => (
                    <div key={i} className="flex gap-8 items-start">
                      <span className="text-3xl font-serif italic text-neutral-100">0{i + 1}</span>
                      <p className="text-neutral-700 text-lg leading-relaxed font-light">{h}</p>
                    </div>
                  ))}
                </div>
              </section>
            )}

            {project.techSpecs && (
              <section id="section-tech" className="space-y-16">
                <div className="flex items-center space-x-8">
                   <h3 className="text-xs font-bold uppercase tracking-[0.5em] text-neutral-300">Technical Standards</h3>
                   <div className="h-px flex-1 bg-neutral-100"></div>
                </div>
                
                <div className="grid grid-cols-1 gap-12">
                  {project.techSpecs.map((s, i) => (
                    <div key={i} className="group border-b border-neutral-100 pb-10">
                      <p className="text-[10px] text-neutral-400 uppercase font-bold tracking-[0.3em] mb-4 group-hover:text-emerald-600 transition-colors">{s.label}</p>
                      <p className="text-2xl font-serif text-neutral-800">{s.value}</p>
                    </div>
                  ))}
                </div>
              </section>
            )}

            <section id="section-ihome" className="bg-[#0a2e26] rounded-[3.5rem] p-12 md:p-24 text-white relative overflow-hidden">
               <div className="absolute top-0 right-0 p-16 text-white/5 text-[15rem] font-serif pointer-events-none select-none">
                  iH
               </div>
               
               <div className="relative z-10 flex flex-col space-y-12">
                  <div className="w-12 h-12 bg-white/10 rounded-2xl flex items-center justify-center backdrop-blur-md">
                    <svg className="w-6 h-6 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
                    </svg>
                  </div>
                  
                  <div className="space-y-6 max-w-xl">
                    <span className="text-[10px] font-bold uppercase tracking-[0.5em] text-emerald-400">Methodology Integration</span>
                    <h4 className="text-4xl md:text-5xl font-serif italic text-emerald-50/90 leading-tight">
                      深植於建築基因中的 <br/>iHome 5.0 智慧工法。
                    </h4>
                  </div>
                  
                  <div className="flex flex-wrap gap-4 pt-12 border-t border-white/10">
                    {project.featuredTechnologies.map(t => (
                      <span key={t} className="px-6 py-2.5 bg-white/5 border border-white/10 rounded-full text-[10px] font-bold uppercase tracking-widest text-emerald-400 hover:bg-emerald-600 hover:text-white transition-all">
                        {t === 'centennial' ? '百年宅' : t === 'healthy' ? '健康宅' : t === 'energy' ? '節能宅' : t === 'smart' ? '智慧宅' : '履歷宅'}
                      </span>
                    ))}
                  </div>
               </div>
            </section>
            
            <div className="pt-24 pb-12 flex justify-center">
               <button 
                 onClick={onBack}
                 className="group flex flex-col items-center space-y-6"
               >
                 <span className="text-[10px] font-bold uppercase tracking-[0.5em] text-neutral-400 group-hover:text-black transition-colors">Back to Portfolio</span>
                 <div className="w-12 h-12 rounded-full border border-neutral-200 flex items-center justify-center group-hover:bg-black group-hover:text-white transition-all">
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path></svg>
                 </div>
               </button>
            </div>

          </div>
        </div>
      </div>
      
      <style>{`
        .animate-fade-in { animation: fadeIn 0.6s ease-out forwards; }
        .animate-scale-up { animation: scaleUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        @keyframes scaleUp { from { opacity: 0; transform: scale(0.92) translateY(30px); } to { opacity: 1; transform: scale(1) translateY(0); } }
      `}</style>
    </div>
  );
};

export default ProjectDetailView;
