
import React, { useState } from 'react';
import { geminiService } from '../services/geminiService';

const ImageEditor: React.FC = () => {
  const [originalImage, setOriginalImage] = useState<string | null>(null);
  const [editedImage, setEditedImage] = useState<string | null>(null);
  const [prompt, setPrompt] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setOriginalImage(reader.result as string);
        setEditedImage(null);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleEdit = async () => {
    if (!originalImage || !prompt) return;
    setIsLoading(true);
    try {
      const base64 = originalImage.split(',')[1];
      const mimeType = originalImage.split(';')[0].split(':')[1];
      const result = await geminiService.editImage(prompt, base64, mimeType);
      if (result) setEditedImage(result);
    } catch (error) {
      alert("編輯失敗，請稍後再試。");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-3xl p-8 border border-neutral-100 shadow-sm max-w-4xl mx-auto my-12">
      <div className="flex flex-col md:flex-row gap-8">
        <div className="flex-1 space-y-6">
          <h3 className="text-2xl font-serif">AI 建築視覺實驗室</h3>
          <p className="text-neutral-500 text-sm">上傳您的室內照片或建案草圖，使用文字指令進行即時修改（如：「加入復古濾鏡」、「更換牆面顏色」）。</p>
          
          <div className="space-y-4">
            <input 
              type="file" 
              accept="image/*" 
              onChange={handleFileChange}
              className="text-xs text-neutral-400 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-xs file:font-semibold file:bg-emerald-50 file:text-emerald-700 hover:file:bg-emerald-100 cursor-pointer"
            />
            
            <textarea 
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="輸入修改指令，例如：『將這張圖調成懷舊風格』..."
              className="w-full p-4 bg-neutral-50 rounded-2xl text-sm h-32 outline-none focus:ring-1 focus:ring-emerald-500 transition-all border-none resize-none"
            />
            
            <button 
              onClick={handleEdit}
              disabled={isLoading || !originalImage || !prompt}
              className={`w-full py-4 rounded-full font-bold uppercase tracking-widest text-[10px] transition-all ${
                isLoading || !originalImage || !prompt 
                ? 'bg-neutral-100 text-neutral-400 cursor-not-allowed' 
                : 'bg-black text-white hover:bg-neutral-800'
              }`}
            >
              {isLoading ? '處理中...' : '生成設計變更'}
            </button>
          </div>
        </div>

        <div className="flex-1 flex flex-col items-center justify-center border-2 border-dashed border-neutral-100 rounded-3xl p-4 bg-neutral-50 min-h-[400px]">
          {editedImage ? (
            <img src={editedImage} alt="Edited" className="w-full h-full object-contain rounded-2xl shadow-xl animate-fade-in-up" />
          ) : originalImage ? (
            <img src={originalImage} alt="Original" className="w-full h-full object-contain rounded-2xl opacity-50" />
          ) : (
            <div className="text-center space-y-2">
              <svg className="w-12 h-12 text-neutral-200 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="1" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              <p className="text-xs text-neutral-300 font-bold uppercase tracking-widest">等待影像上傳</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default ImageEditor;
