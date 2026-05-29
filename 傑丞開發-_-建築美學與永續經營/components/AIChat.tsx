
import React, { useState, useRef, useEffect } from 'react';
import { geminiService } from '../services/geminiService';
import { ChatMessage } from '../types';

const AIChat: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<(ChatMessage & { grounding?: any[] })[]>([
    { role: 'assistant', text: "您好，歡迎來到傑丞開發。我是您的 AI 建築助理，今天有什麼我可以協助您的嗎？" }
  ]);
  const [isTyping, setIsTyping] = useState(false);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages, isTyping]);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMsg = input;
    setInput('');
    setMessages(prev => [...prev, { role: 'user', text: userMsg }]);
    setIsTyping(true);

    const history = messages.map(m => ({
      role: m.role === 'assistant' ? 'model' as const : 'user' as const,
      parts: [{ text: m.text }]
    }));

    const result = await geminiService.generateChatResponse(userMsg, history);
    
    setIsTyping(false);
    setMessages(prev => [...prev, { 
      role: 'assistant', 
      text: result.text || "抱歉，我暫時無法回覆。",
      grounding: result.grounding 
    }]);
  };

  return (
    <div className="fixed bottom-8 right-8 z-[100]">
      {isOpen ? (
        <div className="bg-white w-80 md:w-96 h-[500px] shadow-2xl rounded-2xl flex flex-col border border-neutral-100 animate-fade-in-up">
          <div className="p-6 border-b border-neutral-100 flex justify-between items-center bg-neutral-50 rounded-t-2xl">
            <div>
              <h3 className="text-sm font-bold uppercase tracking-wider">傑丞 AI 實驗室</h3>
              <p className="text-[10px] text-emerald-600 uppercase font-bold tracking-widest">連線中 / 智慧感應</p>
            </div>
            <button onClick={() => setIsOpen(false)} className="text-neutral-400 hover:text-black">
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
          </div>
          
          <div ref={scrollRef} className="flex-1 overflow-y-auto p-6 space-y-6">
            {messages.map((m, i) => (
              <div key={i} className={`flex flex-col ${m.role === 'user' ? 'items-end' : 'items-start'}`}>
                <div className={`max-w-[90%] px-4 py-3 rounded-2xl text-sm leading-relaxed ${
                  m.role === 'user' ? 'bg-black text-white rounded-br-none' : 'bg-neutral-100 text-neutral-800 rounded-bl-none'
                }`}>
                  {m.text}
                </div>
                {m.grounding && m.grounding.length > 0 && (
                  <div className="mt-2 flex flex-col space-y-1">
                    {m.grounding.map((chunk, idx) => (
                      chunk.maps && (
                        <a 
                          key={idx} 
                          href={chunk.maps.uri} 
                          target="_blank" 
                          rel="noopener noreferrer"
                          className="text-[10px] text-emerald-600 font-bold uppercase hover:underline flex items-center"
                        >
                          <svg className="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                          在地圖上查看: {chunk.maps.title}
                        </a>
                      )
                    ))}
                  </div>
                )}
              </div>
            ))}
            {isTyping && (
              <div className="flex justify-start">
                <div className="bg-neutral-100 px-4 py-3 rounded-2xl flex space-x-1 items-center">
                  <div className="w-1.5 h-1.5 bg-neutral-400 rounded-full animate-bounce"></div>
                  <div className="w-1.5 h-1.5 bg-neutral-400 rounded-full animate-bounce delay-100"></div>
                  <div className="w-1.5 h-1.5 bg-neutral-400 rounded-full animate-bounce delay-200"></div>
                </div>
              </div>
            )}
          </div>

          <div className="p-4 border-t border-neutral-100">
            <div className="relative">
              <input 
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && handleSend()}
                placeholder="詢問建案位置、設計理念..."
                className="w-full pl-4 pr-12 py-3 bg-neutral-50 rounded-xl text-sm border-none focus:ring-1 focus:ring-emerald-500 transition-all outline-none"
              />
              <button 
                onClick={handleSend}
                className="absolute right-2 top-1/2 -translate-y-1/2 p-2 text-emerald-600 hover:text-emerald-700"
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path></svg>
              </button>
            </div>
          </div>
        </div>
      ) : (
        <button 
          onClick={() => setIsOpen(true)}
          className="bg-black text-white w-14 h-14 rounded-full flex items-center justify-center shadow-xl hover:scale-105 transition-transform group"
        >
          <svg className="w-6 h-6 group-hover:rotate-12 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
        </button>
      )}
    </div>
  );
};

export default AIChat;
