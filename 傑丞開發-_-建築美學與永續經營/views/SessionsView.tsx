
import React from 'react';
import { SESSIONS } from '../constants';
import OptimizedImage from '../components/OptimizedImage';

const SessionsView: React.FC = () => {
  return (
    <div className="pt-32 pb-24 bg-[#fafaf9] animate-fade-in-up">
      <div className="max-w-7xl mx-auto px-6">
        <div className="mb-24">
          <h1 className="text-xs uppercase tracking-[0.4em] font-bold text-emerald-600 mb-6">Transparency</h1>
          <h2 className="text-6xl font-serif">說明會動態</h2>
          <p className="mt-8 text-xl text-neutral-500 font-light leading-relaxed max-w-2xl">
            傑丞相信「真相的重量」。我們記錄 PDF 中每一次與地主的交流，讓都更改建的每一步都誠實、透明。
          </p>
        </div>

        <div className="space-y-32">
          {SESSIONS.map((event) => (
            <div key={event.id} className="flex flex-col md:flex-row gap-12 items-center border-b border-neutral-200 pb-24 last:border-0 group">
              <div className="w-full md:w-1/2">
                <div className="aspect-video bg-neutral-200 rounded-2xl overflow-hidden shadow-sm group-hover:shadow-xl transition-all duration-700">
                   <OptimizedImage src={event.imageUrl} alt={event.title} className="w-full h-full" />
                </div>
              </div>
              <div className="w-full md:w-1/2 space-y-6">
                <div className="flex items-center space-x-4">
                  <span className="text-xs font-bold text-emerald-600 bg-emerald-50 px-4 py-2 rounded-full">{event.date}</span>
                  <span className="text-xs text-neutral-400 font-bold uppercase tracking-widest">{event.location}</span>
                </div>
                <h3 className="text-3xl font-serif group-hover:text-emerald-700 transition-colors">{event.title}</h3>
                <p className="text-lg text-neutral-600 font-light leading-relaxed">{event.desc}</p>
                <div className="pt-4 flex items-center space-x-2 text-[10px] font-bold uppercase tracking-widest text-emerald-600 cursor-pointer hover:underline underline-offset-4">
                   <span>查看現場紀實報導</span>
                   <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default SessionsView;
