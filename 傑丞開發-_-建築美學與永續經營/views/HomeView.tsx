
import React from 'react';
import Hero from '../components/Hero';
import OptimizedImage from '../components/OptimizedImage';

interface HomeViewProps {
  onNavigate: (page: any) => void;
}

const HomeView: React.FC<HomeViewProps> = ({ onNavigate }) => {
  return (
    <div className="bg-[#fafaf9]">
      <Hero />
      <section className="py-48 px-6 bg-white overflow-hidden">
        <div className="max-w-7xl mx-auto">
          <div className="grid lg:grid-cols-12 gap-24 items-start">
            <div className="lg:col-span-5">
              <h2 className="text-[10px] uppercase tracking-[0.6em] font-bold text-emerald-600 mb-10 flex items-center">
                <span className="w-8 h-px bg-emerald-600 mr-4"></span>
                Creative Strategy
              </h2>
              <p className="text-4xl md:text-5xl font-serif text-neutral-900 leading-tight mb-12">
                我們不只是建造物理結構，更是在策劃一種 <span className="italic">永續的生活藍圖。</span>
              </p>
              <div className="space-y-8 text-lg text-neutral-500 font-light leading-relaxed">
                <p>傑丞建築機構深耕桃園與雙北逾二十載，我們將「iHome 5.0」專利工法定義為品牌的技術脊樑。</p>
                <p>對我們而言，美學不應是奢侈的堆砌，而是基於物理性能的自然延伸。</p>
              </div>
            </div>
            <div className="lg:col-span-7 relative">
               <div className="aspect-[4/5] bg-neutral-100 rounded-3xl overflow-hidden shadow-2xl relative z-10 group">
                  <OptimizedImage 
                    src="https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=1200" 
                    className="w-full h-full object-cover transition-transform duration-[2000ms] group-hover:scale-110" 
                    alt="設計細節" 
                  />
               </div>
            </div>
          </div>
        </div>
      </section>
      
      <section className="py-32 px-6">
          <div className="max-w-7xl mx-auto">
            <div className="flex flex-col md:flex-row justify-between items-end mb-24 gap-8">
                <h3 className="text-6xl md:text-8xl font-serif leading-none tracking-tighter">精選 <br/><span className="italic text-neutral-300">建築誌。</span></h3>
                <button onClick={() => onNavigate('work')} className="px-10 py-4 border border-neutral-200 rounded-full text-[10px] font-bold uppercase tracking-widest hover:bg-black hover:text-white transition-all">探索所有案例</button>
            </div>
            <div className="grid md:grid-cols-2 gap-16 lg:gap-32">
                {[
                  { title: '傑丞。印象羅芙', year: '2020', img: 'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?q=80&w=1200' },
                  { title: '傑丞。印象天裔', year: '2022', img: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1200' }
                ].map((caseStudy, i) => (
                  <div key={i} className={`group cursor-pointer ${i % 2 !== 0 ? 'md:mt-32' : ''}`}>
                    <div className="aspect-[3/4] bg-neutral-100 rounded-2xl overflow-hidden mb-10 transition-shadow hover:shadow-2xl">
                      <OptimizedImage src={caseStudy.img} className="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-1000 group-hover:scale-105" alt={caseStudy.title} />
                    </div>
                    <div className="flex justify-between items-start border-t border-neutral-100 pt-8">
                       <div>
                         <span className="text-[10px] text-emerald-600 font-bold uppercase tracking-widest mb-2 block">Featured Case</span>
                         <h4 className="text-3xl font-serif">{caseStudy.title}</h4>
                       </div>
                       <span className="text-sm font-light text-neutral-400">{caseStudy.year}</span>
                    </div>
                  </div>
                ))}
            </div>
          </div>
      </section>
    </div>
  );
};

export default HomeView;
