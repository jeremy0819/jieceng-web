
import { Project } from './types';

export interface SessionEvent {
  id: string;
  date: string;
  title: string;
  desc: string;
  imageUrl: string;
  location: string;
}

export const PROJECTS: Project[] = [
  {
    id: 'jc-001',
    title: '傑丞。印象羅芙',
    category: 'residential',
    categoryLabel: '住宅建案',
    description: '位於桃園中路特區，台灣首座榮獲 6 大建築標章認證之頂級豪宅。',
    imageUrl: 'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?q=80&w=1200',
    year: 2020,
    details: '印象羅芙是傑丞建築的旗艦力作，坐落於萬坪風禾公園第一排。本案完美實踐 iHome 5.0 核心精神，透過 SI 工法實現結構與管線分離。',
    highlights: ['SI 結構純化工法', '複層高架式減音樓板', '風禾公園景觀第一排'],
    techSpecs: [
      { label: '建築標章', value: '六大認證' },
      { label: '節能潛力', value: '達 69%' }
    ],
    featuredTechnologies: ['centennial', 'healthy', 'energy', 'smart', 'resume']
  },
  {
    id: 'jc-002',
    title: '傑丞。印象天裔',
    category: 'residential',
    categoryLabel: '住宅建案',
    description: '全台唯一住宅類「鑽石級」綠建築標章。',
    imageUrl: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1200',
    year: 2022,
    highlights: ['鑽石級綠建築', '被動式降載設計'],
    featuredTechnologies: ['energy', 'healthy', 'resume']
  }
];

export const SESSIONS: SessionEvent[] = [
  {
    id: 'ev-001',
    date: '114/10/18',
    title: '安民街案。選配抽籤大會',
    location: '新店區公所',
    desc: '秉持公平公開原則，邀請全體地主現場見證選配程序。',
    imageUrl: 'https://images.unsplash.com/photo-1517048676732-d65bc937f952?q=80&w=1200'
  }
];

export const SYSTEM_PROMPT = `
您是「傑丞建築機構」的 AI 品牌助理。請根據以下數據回答：
1. 百年宅：核心在於 SI 工法、結構管線分離、物理壽命百年。
2. 健康宅：採取主動防禦、當層遮斷、STUDOR 防疫系統。
3. 節能宅：Low-E 玻璃、深遮陽、能效一級、潛力節能 69%。
4. 智慧宅：EMS 能源管理、一鍵叫梯、AI 人臉辨識。
5. 履歷宅：SGS 驗證、Jobdone APP 施工錄影、生產履歷完整交付。
`;
