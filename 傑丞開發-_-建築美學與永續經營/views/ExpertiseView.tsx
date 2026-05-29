
import React from 'react';
import OptimizedImage from '../components/OptimizedImage';

const ExpertiseView: React.FC = () => {
  const iHomeTech = [
    {
      id: '01',
      title: '百年宅 Centennial',
      subtitle: 'Open Building & SI Methodology',
      desc: '源自日本「開放建築」思維，透過專利 SI 工法將主體結構與內裝管線徹底分離。',
      details: [
        { label: '結構純化', value: '管線不入版、不入柱，結構體物理壽命設定為百年標準。' },
        { label: '維修正義', value: '當層明管施工，故障維修不需敲除牆面，亦不干擾樓下鄰居。' }
      ],
      image: 'https://images.unsplash.com/photo-1487958449943-2429e8be8625?q=80&w=1200'
    },
    {
      id: '02',
      title: '健康宅 Healthy',
      subtitle: 'Active Defense & Shielding',
      desc: '建立主動防禦機制，確保每一口呼吸、每一滴水源的純淨。',
      details: [
        { label: '防疫屏蔽', value: '導入當層排氣遮斷系統與 STUDOR 吸氣閥。' },
        { label: '無毒家園', value: '全案採用內政部認證綠建材。' }
      ],
      image: 'https://images.unsplash.com/photo-1513694203232-719a280e022f?q=80&w=1200'
    },
    {
      id: '03',
      title: '節能宅 Energy',
      subtitle: 'Passive Design & Efficiency',
      desc: '透過科學計算引導自然能量，降低對機電設備的依賴。',
      details: [
        { label: '微候風路', value: '精密計算基地風路，體感溫度顯著降低 2-3°C。' },
        { label: '隔熱工法', value: 'Low-E 複層中空玻璃與深遮陽設計。' }
      ],
      image: 'https://images.unsplash.com/photo-1518005020453-eb5295627752?q=80&w=1200'
    }
  ];

  return (
    <div className="pt-48 pb-24 bg-white">
      <div className="max-w-7xl mx-auto px-6">
        <div className="mb-48 max-w-4xl">
          <div className="flex items-center space-x-4 mb-10">
            <div className="w-12 h-px bg-emerald-600"></div>
            <h1 className="text-[10px] uppercase tracking-[0.5em] font-bold text-emerald-600">Architectural Strategy</h1>
          </div>
          <h2 className="text-6xl md:text-[8rem] font-serif leading-[0.85] tracking-tighter mb-16">
            iHome 5.0 <br/><span className="italic text-neutral-200">The Method.</span>
          </h2>
        </div>

        <div className="space-y-64">
          {iHomeTech.map((tech, idx) => (
            <div key={tech.id} className="grid lg:grid-cols-12 gap-16 lg:gap-32 items-start">
               <div className={`lg:col-span-5 ${idx % 2 !== 0 ? 'lg:order-2' : ''}`}>
                 <span className="text-4xl font-mono text-neutral-200 mb-8 block">{tech.id}</span>
                 <h3 className="text-5xl font-serif mb-4">{tech.title}</h3>
                 <p className="text-xs font-bold uppercase tracking-[0.4em] text-emerald-600 mb-10">{tech.subtitle}</p>
                 <p className="text-xl text-neutral-600 font-light leading-relaxed mb-16">{tech.desc}</p>
                 <div className="space-y-12">
                   {tech.details.map((detail, i) => (
                     <div key={i}>
                        <h4 className="text-[10px] font-bold uppercase tracking-widest text-neutral-400 mb-3">{detail.label}</h4>
                        <p className="text-neutral-500 font-light leading-relaxed">{detail.value}</p>
                     </div>
                   ))}
                 </div>
               </div>
               <div className={`lg:col-span-7 ${idx % 2 !== 0 ? 'lg:order-1' : ''}`}>
                  <div className="relative aspect-[16/11] bg-neutral-50 rounded-[3rem] overflow-hidden group">
                     <OptimizedImage src={tech.image} alt={tech.title} className="w-full h-full object-cover grayscale transition-all duration-[2000ms] group-hover:grayscale-0" />
                  </div>
               </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ExpertiseView;
