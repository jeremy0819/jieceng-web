
import React from 'react';
import OptimizedImage from './OptimizedImage';

const Hero: React.FC = () => {
  return (
    <section className="relative min-h-screen flex items-center justify-center bg-black overflow-hidden">
      <div className="absolute inset-0 z-0 opacity-60">
        <OptimizedImage src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=2000" alt="傑丞建築" className="w-full h-full object-cover scale-105" />
      </div>
      <div className="max-w-7xl mx-auto w-full px-6 z-10">
        <div className="animate-fade-in-up">
          <h1 className="text-7xl md:text-[10rem] font-serif leading-[1] tracking-tighter text-white mb-10">
            <span className="block text-neutral-400/80 mb-2">永續建築</span>
            <span className="italic">傳承百年</span>
          </h1>
          <p className="text-2xl text-neutral-300 font-light max-w-xl leading-relaxed">
            傑丞建築透過 <span className="text-emerald-400 font-medium">iHome 5.0</span> 專利技術，構築能與您共同成長的生命建築。
          </p>
        </div>
      </div>
    </section>
  );
};

export default Hero;
