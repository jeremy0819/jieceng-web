export interface IHomeDetail {
  label: string
  value: string
}

export interface IHomeTech {
  key: string
  num: string
  title: string
  en: string
  subtitle: string
  desc: string
  details: IHomeDetail[]
  image: string
}

/**
 * iHome 5.0 五大宅工法 — 傑丞建築機構的技術脊樑（單一資料來源）。
 * 內容萃取自品牌既有資料；圖片沿用 public/image/ 既有素材（離線可用）。
 */
const tech: Omit<IHomeTech, 'image'>[] = [
  {
    key: 'centennial',
    num: '01',
    title: '百年宅',
    en: 'Centennial',
    subtitle: 'Open Building & SI Methodology',
    desc: '源自日本「開放建築」思維，透過專利 SI 工法將主體結構與內裝管線徹底分離，讓建築的物理壽命設定為百年標準。',
    details: [
      { label: '結構純化', value: '管線不入版、不入柱，結構體物理壽命設定為百年標準。' },
      { label: '維修正義', value: '當層明管施工，故障維修不需敲除牆面，亦不干擾樓下鄰居。' }
    ]
  },
  {
    key: 'healthy',
    num: '02',
    title: '健康宅',
    en: 'Healthy',
    subtitle: 'Active Defense & Shielding',
    desc: '建立主動防禦機制，確保每一口呼吸、每一滴水源的純淨，從源頭守護居住者的健康。',
    details: [
      { label: '防疫屏蔽', value: '導入當層排氣遮斷系統與 STUDOR 吸氣閥，阻絕氣流交叉感染。' },
      { label: '無毒家園', value: '全案採用內政部認證綠建材，打造零負擔的呼吸環境。' }
    ]
  },
  {
    key: 'energy',
    num: '03',
    title: '節能宅',
    en: 'Energy',
    subtitle: 'Passive Design & Efficiency',
    desc: '透過科學計算引導自然能量，降低對機電設備的依賴，實踐能效一級的低碳生活。',
    details: [
      { label: '微候風路', value: '精密計算基地風路，體感溫度顯著降低 2-3°C，節能潛力達 69%。' },
      { label: '隔熱工法', value: 'Low-E 複層中空玻璃與深遮陽設計，從建築外殼阻絕熱負荷。' }
    ]
  },
  {
    key: 'smart',
    num: '04',
    title: '智慧宅',
    en: 'Smart',
    subtitle: 'Intelligent Energy & Living',
    desc: '以數位科技串聯建築的每一個環節，讓能源管理與生活服務在一指之間完成。',
    details: [
      { label: '能源管理', value: 'EMS 能源管理系統即時監控用電，讓節能成果可被量化與追蹤。' },
      { label: '智慧生活', value: '一鍵叫梯、AI 人臉辨識門禁，重新定義回家的儀式感與安全。' }
    ]
  },
  {
    key: 'resume',
    num: '05',
    title: '履歷宅',
    en: 'Resume',
    subtitle: 'Quality Traceability',
    desc: '讓每一道工序都被記錄、被驗證，把看不見的施工品質，化為可被檢視的生產履歷。',
    details: [
      { label: '施工透明', value: 'Jobdone APP 全程施工錄影存證，每一個隱蔽工程都有跡可循。' },
      { label: '品質驗證', value: 'SGS 第三方驗證，生產履歷完整交付，給居住者百分百的安心。' }
    ]
  }
]

// 五大宅對應的視覺素材（沿用既有圖庫）
const imageMap: Record<string, string> = {
  centennial: 'image/project-1.jpg',
  healthy: 'image/project-2.jpg',
  energy: 'image/project-3.jpg',
  smart: 'image/project-4.jpg',
  resume: 'image/hero-background.jpg'
}

export const useIHome = () => {
  const base = useRuntimeConfig().app.baseURL
  const withBase = (path: string) => `${base}${path}`.replace(/([^:]\/)\/+/g, '$1')

  const iHomeTech: IHomeTech[] = tech.map((t) => ({ ...t, image: withBase(imageMap[t.key]) }))

  // 標籤對照：把技術 key 轉成中文（供作品標籤、下拉選單使用）
  const labelOf = (key: string) => tech.find((t) => t.key === key)?.title ?? key

  return { iHomeTech, labelOf }
}
