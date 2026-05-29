export interface Project {
  id: number
  title: string
  year: number
  category: string
  categoryLabel: string
  location: string
  description: string
  fullDescription: string
  image: string
  highlights: string[]
  specs: Record<string, string>
  technologies: string[] // 對應 useIHome 的 key：centennial / healthy / energy / smart / resume
}

/**
 * 全站建案資料的單一來源（真實案例）。
 * 新增建案：在此陣列加一筆物件，並把對應圖片放到 public/image/，
 * 首頁、作品集、案例詳情頁會自動同步。technologies 對應 iHome 5.0 五大宅。
 */
const projects: Project[] = [
  {
    id: 1,
    title: '傑丞。印象羅芙',
    year: 2020,
    category: 'residential',
    categoryLabel: '住宅建案',
    location: '桃園中路特區',
    description: '位於桃園中路特區，台灣首座榮獲六大建築標章認證之頂級豪宅。',
    fullDescription:
      '印象羅芙是傑丞建築的旗艦力作，坐落於萬坪風禾公園第一排。本案完美實踐 iHome 5.0 核心精神，透過 SI 工法實現結構與管線分離，並以全方位的標章認證，定義桃園頂級住宅的全新標準。',
    image: 'image/project-1.jpg',
    highlights: ['SI 結構純化工法', '複層高架式減音樓板', '風禾公園景觀第一排'],
    specs: {
      建築標章: '六大認證',
      節能潛力: '達 69%',
      完工年份: '2020',
      基地位置: '桃園中路特區'
    },
    technologies: ['centennial', 'healthy', 'energy', 'smart', 'resume']
  },
  {
    id: 2,
    title: '傑丞。印象天裔',
    year: 2022,
    category: 'residential',
    categoryLabel: '住宅建案',
    location: '桃園',
    description: '全台唯一住宅類「鑽石級」綠建築標章，被動式降載設計的永續典範。',
    fullDescription:
      '印象天裔以全台唯一住宅類「鑽石級」綠建築標章，樹立永續住宅的新高度。本案以被動式降載設計為核心，從建築外殼到空間配置，全面降低對機電的依賴，讓節能成為生活的自然狀態。',
    image: 'image/project-2.jpg',
    highlights: ['鑽石級綠建築標章', '被動式降載設計', '全齡友善生活空間'],
    specs: {
      建築標章: '鑽石級綠建築',
      設計核心: '被動式降載',
      完工年份: '2022',
      基地位置: '桃園'
    },
    technologies: ['energy', 'healthy', 'resume']
  }
]

export const useProjects = () => {
  // 動態綁定 (:src) 的圖片不會被 Nuxt 自動加上 baseURL，
  // 因此在這裡依 app.baseURL 補上前綴，子路徑部署 (GitHub Pages) 才能正確載入。
  const base = useRuntimeConfig().app.baseURL
  const withBase = (path: string) => `${base}${path}`.replace(/([^:]\/)\/+/g, '$1')

  const resolved = projects.map((p) => ({ ...p, image: withBase(p.image) }))

  const getProject = (id: string | number): Project | undefined =>
    resolved.find((p) => p.id === Number(id))

  const projectsByTech = (key: string) =>
    resolved.filter((p) => p.technologies.includes(key))

  return { projects: resolved, getProject, projectsByTech }
}
