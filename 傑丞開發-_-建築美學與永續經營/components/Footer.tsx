
import React from 'react';

const Footer: React.FC<{onNavigate: (page: any)=>void}> = ({ onNavigate }) => {
  return (
    <footer className="py-24 px-6 bg-[#fafaf9] border-t border-neutral-200">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-start gap-16">
        <div>
          <h2 className="text-4xl font-serif mb-8">與我們聯繫，<br />共築美好家園。</h2>
          <a href="mailto:service@jiecheng-dev.com" className="text-xl font-light underline">service@jiecheng-dev.com</a>
        </div>
        <div className="flex gap-24">
          <ul className="text-xs uppercase font-bold tracking-widest space-y-4">
            <li><button onClick={()=>onNavigate('work')}>建案作品</button></li>
            <li><button onClick={()=>onNavigate('expertise')}>工法體系</button></li>
            <li><button onClick={()=>onNavigate('evaluation')}>開發評估</button></li>
          </ul>
        </div>
      </div>
      <div className="mt-32 pt-12 border-t text-[10px] text-neutral-400 font-bold uppercase tracking-widest">
        © 2024 傑丞開發。由 Gemini AI 驅動
      </div>
    </footer>
  );
};

export default Footer;
