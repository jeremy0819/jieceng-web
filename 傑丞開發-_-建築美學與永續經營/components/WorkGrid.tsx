
import React from 'react';
import { PROJECTS } from '../constants';

const WorkGrid: React.FC = () => {
  return (
    <section id="work" className="py-24 px-6 bg-white">
      <div className="max-w-7xl mx-auto">
        <div className="flex justify-between items-end mb-16 border-b border-neutral-100 pb-8">
            <h2 className="text-3xl font-serif">Selected Works</h2>
            <p className="text-xs uppercase tracking-widest text-neutral-400">View All Projects</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-24">
          {PROJECTS.map((project, idx) => (
            <div key={project.id} className={`group cursor-pointer ${idx % 2 !== 0 ? 'md:mt-32' : ''}`}>
              <div className="overflow-hidden bg-neutral-100 aspect-[4/5] relative">
                <img 
                  src={project.imageUrl} 
                  alt={project.title}
                  className="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-105"
                />
                <div className="absolute inset-0 bg-black/0 group-hover:bg-black/10 transition-colors duration-500"></div>
              </div>
              <div className="mt-8 flex justify-between items-start">
                <div>
                  <p className="text-xs uppercase tracking-widest text-neutral-400 mb-2">{project.category}</p>
                  <h3 className="text-2xl font-medium tracking-tight group-hover:underline underline-offset-4 decoration-1">{project.title}</h3>
                </div>
                <span className="text-sm font-light text-neutral-400">{project.year}</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default WorkGrid;
