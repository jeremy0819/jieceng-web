
import React, { useState, useEffect, useMemo } from 'react';
import { PROJECTS } from '../constants';
import ImageEditor from '../components/ImageEditor';
import ProjectDetailView from './ProjectDetailView';
import ProjectFilterBar from '../components/ProjectFilterBar';
import OptimizedImage from '../components/OptimizedImage';
import { Project, ProjectFilters } from '../types';

const WorkView: React.FC = () => {
  const [selectedProject, setSelectedProject] = useState<Project | null>(null);
  const [isLoadingData, setIsLoadingData] = useState(true);
  const [filters, setFilters] = useState<ProjectFilters>({ categories: [], technologies: [] });

  useEffect(() => {
    // 模擬載入動畫
    const timer = setTimeout(() => setIsLoadingData(false), 500);
    return () => clearTimeout(timer);
  }, []);

  const filteredProjects = useMemo(() => {
    return PROJECTS.filter(project => {
      const matchCat = filters.categories.length === 0 || filters.categories.includes(project.category);
      const matchTech = filters.technologies.length === 0 || 
        filters.technologies.some(t => project.featuredTechnologies.includes(t));
      return matchCat && matchTech;
    });
  }, [filters]);

  const scrollToAnchor = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      const offset = 160; 
      const bodyRect = document.body.getBoundingClientRect().top;
      const elementRect = el.getBoundingClientRect().top;
      const elementPosition = elementRect - bodyRect;
      const offsetPosition = elementPosition - offset;

      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
    }
  };

  return (
    <div className="pt-32 pb-24 bg-white animate-fade-in-up relative min-h-screen">
      <div className="max-w-7xl mx-auto px-6">
        {/* 標題區 */}
        <div className="mb-24 flex flex-col lg:flex-row lg:items-end justify-between border-b border-neutral-100 pb-16">
          <div className="max-w-2xl">
            <h1 className="text-6xl md:text-8xl font-serif mb-8 leading-tight">建築 <br/><span className="italic text-neutral-300">精選集。</span></h1>
            <p className="text-xl text-neutral-500 font-light leading-relaxed">
              傑丞建築機構將 iHome 5.0 永續工法落實於每一處細節，創造能傳承百年的資產，而不僅是消耗品。
            </p>
          </div>
          
          <div className="mt-12 lg:mt-0 flex flex-wrap gap-8">
            {['residential', 'public'].map(cat => (
              <button 
                key={cat}
                onClick={() => {
                  setFilters({ ...filters, categories: [cat as any] });
                  scrollToAnchor('project-grid');
                }}
                className="text-[10px] font-bold uppercase tracking-[0.4em] text-neutral-400 hover:text-emerald-600 border-b border-transparent hover:border-emerald-600 pb-2 transition-all"
              >
                {cat === 'residential' ? '住宅作品' : '都更/公共'}
              </button>
            ))}
          </div>
        </div>

        {/* 吸頂過濾列 */}
        <ProjectFilterBar 
          filters={filters} 
          onChange={setFilters} 
          resultCount={filteredProjects.length} 
        />

        {/* 建案列表 */}
        <div id="project-grid" className="mt-32">
          {isLoadingData ? (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-x-16 gap-y-32">
               {[1,2,3,4].map(i => (
                  <div key={i} className="aspect-[4/5] bg-neutral-50 rounded-[3rem] animate-pulse border border-neutral-100"></div>
               ))}
            </div>
          ) : filteredProjects.length > 0 ? (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-x-16 gap-y-32 lg:gap-x-32">
              {filteredProjects.map((project, idx) => (
                <div 
                  key={project.id} 
                  onClick={() => setSelectedProject(project)}
                  className={`group flex flex-col cursor-pointer transition-all duration-700 ${idx % 2 !== 0 ? 'md:mt-48' : ''}`}
                >
                  <div className="relative aspect-[4/5] bg-neutral-50 rounded-[3rem] overflow-hidden shadow-sm transition-all duration-700 group-hover:shadow-2xl border border-neutral-100">
                    <OptimizedImage 
                      src={project.imageUrl} 
                      alt={project.title}
                      className="w-full h-full grayscale group-hover:grayscale-0 transition-all duration-1000 group-hover:scale-110"
                    />
                    
                    <div className="absolute top-10 left-10 z-10 flex flex-col gap-3">
                       <span className="bg-white/90 backdrop-blur-md text-[10px] font-bold uppercase tracking-widest px-5 py-2.5 rounded-full border border-neutral-200 shadow-sm">
                          Est. {project.year}
                       </span>
                    </div>

                    <div className="absolute inset-0 bg-gradient-to-t from-emerald-950/90 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 flex flex-col justify-end p-12">
                       <p className="text-emerald-400 text-xs font-bold uppercase tracking-[0.3em] mb-3">Case Exploration</p>
                       <h4 className="text-white text-3xl font-serif mb-8">{project.title}</h4>
                       <div className="flex items-center space-x-4 text-white">
                          <span className="text-[10px] font-bold uppercase tracking-[0.4em]">探索細節</span>
                          <div className="w-12 h-[1px] bg-white group-hover:w-20 transition-all duration-700"></div>
                       </div>
                    </div>
                  </div>

                  <div className="mt-12 space-y-5 px-4">
                    <div className="flex flex-wrap gap-2">
                       {project.featuredTechnologies.slice(0, 3).map(t => (
                         <span key={t} className="text-[9px] font-bold uppercase tracking-widest text-emerald-700 bg-emerald-50 px-4 py-1.5 rounded-full border border-emerald-100">
                           {t === 'centennial' ? '百年宅' : t === 'healthy' ? '健康宅' : t === 'energy' ? '節能宅' : t === 'smart' ? '智慧宅' : '履歷宅'}
                         </span>
                       ))}
                    </div>
                    <h3 className="text-4xl font-serif tracking-tight leading-tight group-hover:text-emerald-800 transition-colors">
                      {project.title}
                    </h3>
                    <p className="text-neutral-500 font-light leading-relaxed max-w-sm line-clamp-2 italic">
                      {project.description}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="py-48 text-center animate-fade-in">
              <div className="w-20 h-20 bg-neutral-50 rounded-full flex items-center justify-center mx-auto mb-8 border border-neutral-100">
                 <svg className="w-8 h-8 text-neutral-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="1.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
              </div>
              <p className="text-neutral-400 font-serif italic text-2xl mb-4">尚未找到完全相符的作品</p>
              <button 
                onClick={() => setFilters({ categories: [], technologies: [] })}
                className="text-xs font-bold uppercase tracking-widest text-emerald-600 hover:text-emerald-800"
              >
                重置條件再試一次
              </button>
            </div>
          )}
        </div>

        {/* AI 實驗室區塊 */}
        <div className="mt-64 pt-32 border-t border-neutral-100">
            <div className="max-w-xl mb-20">
                <div className="flex items-center space-x-3 mb-6">
                   <div className="w-2 h-2 bg-emerald-600 rounded-full animate-pulse"></div>
                   <h2 className="text-xs uppercase tracking-[0.5em] font-bold text-emerald-600">AI Design Lab / 視覺實驗</h2>
                </div>
                <h3 className="text-5xl font-serif mb-6 leading-tight">預見您的 <br/><span className="italic text-neutral-300">未來居所。</span></h3>
                <p className="text-neutral-500 font-light text-lg leading-relaxed">
                   作為「履歷宅」數位化服務的延伸，我們提供 AI 影像修正技術。無論是空間草圖或實景照片，傑丞協助您即時視覺化各種設計可能。
                </p>
            </div>
            <ImageEditor />
        </div>
      </div>

      {/* 專案詳情彈出層 */}
      {selectedProject && (
        <ProjectDetailView project={selectedProject} onBack={() => setSelectedProject(null)} />
      )}
    </div>
  );
};

export default WorkView;
