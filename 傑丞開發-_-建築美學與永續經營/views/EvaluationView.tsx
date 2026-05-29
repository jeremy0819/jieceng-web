
import React, { useState, useEffect } from 'react';
import { GoogleGenAI } from "@google/genai";

const EvaluationView: React.FC = () => {
  const [landArea, setLandArea] = useState(605.6);
  const [baseFar, setBaseFar] = useState(345.5);
  const [bonusRate, setBonusRate] = useState(50);
  const [tdrRate, setTdrRate] = useState(30);
  const [sellPrice, setSellPrice] = useState(115);
  const [parkingPrice, setParkingPrice] = useState(280);
  const [parkingCount, setParkingCount] = useState(150);
  const [strategy, setStrategy] = useState<'joint' | 'manage'>('joint');
  const [jointRatio, setJointRatio] = useState(65);
  const [results, setResults] = useState({ totalRevenue: 0, devROI: 0, landownerProfit: 0 });
  const [aiReport, setAiReport] = useState<string | null>(null);
  const [isAiLoading, setIsAiLoading] = useState(false);

  useEffect(() => {
    const totalVolume = landArea * (baseFar/100) * (1 + bonusRate/100 + tdrRate/100);
    const totalSaleArea = totalVolume * 1.65;
    const totalRevenue = (totalSaleArea * sellPrice) + (parkingCount * parkingPrice);
    setResults({
      totalRevenue,
      devROI: strategy === 'joint' ? 18.5 : 8.0,
      landownerProfit: totalRevenue * (jointRatio / 100)
    });
  }, [landArea, baseFar, bonusRate, tdrRate, sellPrice, strategy, jointRatio]);

  const generateAIReport = async () => {
    setIsAiLoading(true);
    const ai = new GoogleGenAI({ apiKey: process.env.API_KEY || '' });
    try {
      const response = await ai.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: `分析都更開發數據：基地${landArea}坪，模式${strategy}，預估總銷${results.totalRevenue}萬。`,
      });
      setAiReport(response.text);
    } finally {
      setIsAiLoading(false);
    }
  };

  return (
    <div className="pt-48 pb-24 bg-[#fafaf9]">
      <div className="max-w-7xl mx-auto px-6">
        <h2 className="text-6xl font-serif mb-16">開發評估系統。</h2>
        <div className="grid lg:grid-cols-12 gap-12">
          <div className="lg:col-span-7 space-y-12">
            <div className="bg-white p-12 rounded-[3rem] shadow-sm border border-neutral-100 space-y-8">
              <div className="grid grid-cols-2 gap-8">
                <div><label className="text-[10px] uppercase font-bold text-neutral-400">基地面積 (坪)</label><input type="number" value={landArea} onChange={e => setLandArea(Number(e.target.value))} className="w-full text-4xl font-serif border-b outline-none py-2"/></div>
                <div><label className="text-[10px] uppercase font-bold text-neutral-400">容積獎勵 (%)</label><input type="number" value={bonusRate} onChange={e => setBonusRate(Number(e.target.value))} className="w-full text-4xl font-serif border-b outline-none py-2"/></div>
              </div>
            </div>
          </div>
          <div className="lg:col-span-5 space-y-8">
            <div className="bg-emerald-950 text-white rounded-[3.5rem] p-12 shadow-2xl">
               <div className="space-y-12">
                  <div className="flex bg-white/10 p-1 rounded-full"><button onClick={()=>setStrategy('joint')} className={`flex-1 py-3 text-[10px] uppercase font-bold rounded-full ${strategy==='joint'?'bg-white text-emerald-950':'text-white/40'}`}>合建分屋</button><button onClick={()=>setStrategy('manage')} className={`flex-1 py-3 text-[10px] uppercase font-bold rounded-full ${strategy==='manage'?'bg-white text-emerald-950':'text-white/40'}`}>全案管理</button></div>
                  <div><p className="text-[10px] uppercase text-emerald-400 mb-4">預估 ROI</p><p className="text-7xl font-serif">{results.devROI.toFixed(1)}%</p></div>
               </div>
            </div>
            <button onClick={generateAIReport} className="w-full py-8 bg-white border rounded-full text-[10px] uppercase font-bold text-emerald-600 shadow-xl">{isAiLoading?'演算中...':'啟動 AI 顧問分析'}</button>
            {aiReport && <div className="bg-white p-12 rounded-[3rem] text-sm text-neutral-600 font-light leading-relaxed">{aiReport}</div>}
          </div>
        </div>
      </div>
    </div>
  );
};

export default EvaluationView;
