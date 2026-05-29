
import React from 'react';
import { ProjectFilters } from '../types';

interface ProjectFilterBarProps {
  filters: ProjectFilters;
  onChange: (filters: ProjectFilters) => void;
  resultCount: number;
}

const ProjectFilterBar: React.FC<ProjectFilterBarProps> = ({ filters, onChange, resultCount }) => {
  const categories = [
    { id: 'residential', label: '住宅建案' },
    { id: 'commercial', label: '商辦空間' },
    { id: 'public', label: '公共建設' },
  ];

  const technologies = [
    { id: 'centennial', label: '百年宅' },
    { id: 'healthy', label: '健康宅' },
    { id: 'energy', label: '節能宅' },
    { id: 'smart', label: '智慧宅' },
    { id: 'resume', label: '履歷宅' },
  ];

  const toggleCategory = (id: string) => {
    const newCats = filters.categories.includes(id)
      ? filters.categories.filter(c => c !== id)
      : [...filters.categories, id];
    onChange({ ...filters, categories: newCats });
  };

  const toggleTech = (id: string) => {
    const newTechs = filters.technologies.includes(id)
      ? filters.technologies.filter(t => t !== id)
      : [...filters.technologies, id];
    onChange({ ...filters, technologies: newTechs });
  };

  const clearFilters = () => onChange({ categories: [], technologies: [] });

  const isFiltered = filters.categories.length > 0 || filters.technologies.length > 0;

  return (
    <div className="bg-white border-b border-neutral-100 py-8 sticky top-[72px] z-40">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row md:items-center justify-between gap-8">
        
        <div className="flex flex-wrap items-center gap-4">
          <span className="text-[10px] font-bold uppercase tracking-widest text-neutral-400 mr-4">按類別篩選:</span>
          {categories.map(cat => (
            <button
              key={cat.id}
              onClick={() => toggleCategory(cat.id)}
              className={`px-6 py-2 rounded-full text-xs font-medium transition-all border ${
                filters.categories.includes(cat.id)
                  ? 'bg-black text-white border-black'
                  : 'bg-white text-neutral-500 border-neutral-200 hover:border-black hover:text-black'
              }`}
            >
              {cat.label}
            </button>
          ))}
        </div>

        <div className="flex flex-wrap items-center gap-4">
          <span className="text-[10px] font-bold uppercase tracking-widest text-neutral-400 mr-4">核心工法:</span>
          {technologies.map(tech => (
            <button
              key={tech.id}
              onClick={() => toggleTech(tech.id)}
              className={`px-4 py-1.5 rounded-lg text-[10px] font-bold uppercase tracking-widest transition-all ${
                filters.technologies.includes(tech.id)
                  ? 'bg-emerald-600 text-white shadow-lg shadow-emerald-100'
                  : 'bg-neutral-100 text-neutral-400 hover:bg-neutral-200'
              }`}
            >
              {tech.label}
            </button>
          ))}
        </div>

        <div className="flex items-center space-x-6">
          <div className="text-[10px] font-bold uppercase tracking-widest">
            共 <span className="text-emerald-600 text-sm">{resultCount}</span> 個結果
          </div>
          {isFiltered && (
            <button 
              onClick={clearFilters}
              className="text-[10px] font-bold uppercase tracking-widest text-neutral-400 hover:text-emerald-600 underline underline-offset-4"
            >
              重設所有條件
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

export default ProjectFilterBar;
