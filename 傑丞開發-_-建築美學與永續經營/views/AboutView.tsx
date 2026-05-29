
import React from 'react';

const AboutView: React.FC = () => {
  return (
    <div className="pt-32 pb-24 px-6 bg-white animate-fade-in-up">
      <div className="max-w-7xl mx-auto">
        <div className="grid lg:grid-cols-12 gap-16 items-start">
            <div className="lg:col-span-5 space-y-12">
                <h1 className="text-6xl md:text-8xl font-serif leading-none">關於 <br/><span className="italic text-neutral-400">傑丞。</span></h1>
                <div className="aspect-[3/4] bg-neutral-100 overflow-hidden rounded-3xl grayscale hover:grayscale-0 transition-all duration-1000">
                    <img src="https://images.unsplash.com/photo-1577412647305-991150c7d163?q=80&w=800&h=1200&auto=format&fit=crop" className="w-full h-full object-cover" alt="團隊合作" />
                </div>
            </div>
            
            <div className="lg:col-span-7 lg:pl-12 space-y-16">
                <div className="space-y-8">
                    <h2 className="text-xs uppercase tracking-[0.3em] font-bold text-emerald-600">品牌故事</h2>
                    <p className="text-3xl font-light text-neutral-800 leading-tight">
                        傑丞開發不僅是建築商，更是您生活夢想的構築者與守護者。
                    </p>
                    <div className="space-y-6 text-lg text-neutral-500 font-light leading-relaxed max-w-2xl">
                        <p>我們深信建築應該具有生命力。傑丞團隊由資深建築師、室內設計師與永續科技專家組成，共同追求「極簡、機能、永續」的核心價值。</p>
                        <p>在過去的時光中，我們在多個城市核心區留下作品。每一個作品都象徵著我們對品質的挑剔，以及對居住者幸福感的重視。</p>
                    </div>
                </div>

                <div className="space-y-8 border-t border-neutral-100 pt-16">
                    <h2 className="text-xs uppercase tracking-[0.3em] font-bold text-emerald-600">企業核心</h2>
                    <div className="grid md:grid-cols-2 gap-12">
                        <div>
                            <h3 className="text-xl font-medium mb-4">價值觀</h3>
                            <ul className="space-y-2 text-neutral-500 font-light">
                                <li>— 誠信開發</li>
                                <li>— 工藝至上</li>
                                <li>— 永續經營</li>
                                <li>— 以人為本</li>
                            </ul>
                        </div>
                        <div>
                            <h3 className="text-xl font-medium mb-4">目標</h3>
                            <ul className="space-y-2 text-neutral-500 font-light">
                                <li>— 打造零碳建築</li>
                                <li>— 提升居住品質</li>
                                <li>— 活化都市空間</li>
                                <li>— 引領建築潮流</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      </div>
    </div>
  );
};

export default AboutView;
