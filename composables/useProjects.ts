export interface Project {
  id: number
  title: string
  category: string
  description: string
  fullDescription: string
  image: string
  specs: Record<string, string>
}

/**
 * 全站作品資料的單一來源。
 * 新增作品：在此陣列加一筆物件，並把對應圖片放到 public/image/ 即可，
 * 首頁、作品集、作品詳情頁會自動同步。
 */
const projects: Project[] = [
  {
    id: 1,
    title: '開放建築',
    category: 'Residential',
    description: '利用自然採光與極簡線條，打造開放式居住空間。',
    fullDescription:
      '利用自然採光與極簡線條，打造開放式居住空間。本案重點在於打破傳統實牆的束縛，採用可變動的彈性隔間技術，讓住戶能隨著生命週期的變化，自由調整室內佈局。',
    image: 'image/project-1.jpg',
    specs: {
      Location: '台北市, 信義區',
      Year: '2024',
      Area: '120 sqm',
      System: 'Open Building Patent',
    },
  },
  {
    id: 2,
    title: '當層配管',
    category: 'Commercial',
    description: '結合工業風格與綠色植物，提升工作效率與舒適度。',
    fullDescription:
      '結合工業風格與綠色植物，提升工作效率與舒適度。引進「當層配管」專利技術，解決傳統建築漏水難以維修的痛點，實現管線與結構體徹底分離，大幅提升建物壽命。',
    image: 'image/project-2.jpg',
    specs: {
      Location: '新北市, 板橋區',
      Year: '2023',
      Area: '450 sqm',
      System: 'SI Separation',
    },
  },
  {
    id: 3,
    title: '複層樓板',
    category: 'Landscape',
    description: '強調人與自然互動，設計融入周圍環境的公共空間。',
    fullDescription:
      '強調人與自然互動，設計融入周圍環境的公共空間。透過複層樓板設計創造出極佳的隔音效果與微氣候調節空間，讓室內環境不受外界噪音干擾，維持恆溫舒適。',
    image: 'image/project-3.jpg',
    specs: {
      Location: '台中市, 西屯區',
      Year: '2024',
      Area: '800 sqm',
      System: 'Double-Layer Floor',
    },
  },
  {
    id: 4,
    title: '都市更新',
    category: 'Renovation',
    description: '保留歷史紋理，注入現代機能，賦予老建築新生命。',
    fullDescription:
      '保留歷史紋理，注入現代機能，賦予老建築新生命。在尊重原有結構與街區記憶的前提下，導入現代化的機能與安全規範，讓老屋在延續城市文化的同時，也能滿足當代的居住需求。',
    image: 'image/project-4.jpg',
    specs: {
      Location: '台北市, 大同區',
      Year: '2023',
      Area: '320 sqm',
      System: 'Urban Renewal',
    },
  },
]

export const useProjects = () => {
  // 動態綁定 (:src) 的圖片不會被 Nuxt 自動加上 baseURL，
  // 因此在這裡依 app.baseURL 補上前綴，子路徑部署 (GitHub Pages) 才能正確載入。
  const base = useRuntimeConfig().app.baseURL
  const withBase = (path: string) => `${base}${path}`.replace(/([^:]\/)\/+/g, '$1')

  const resolved = projects.map((p) => ({ ...p, image: withBase(p.image) }))

  const getProject = (id: string | number): Project | undefined =>
    resolved.find((p) => p.id === Number(id))

  return { projects: resolved, getProject }
}
