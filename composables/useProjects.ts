export interface Project {
  id: number
  title: string
  year: number
  category: 'residential' | 'renewal'  // 用於 portfolio 篩選
  categoryLabel: string
  location: string
  description: string
  fullDescription: string
  image: string
  highlights: string[]
  specs: Record<string, string>
  technologies: string[] // iHome 5.0 工法標籤（顯示於建案詳情頁）
}

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
  },
  {
    id: 3,
    title: '新店安和段都更案',
    year: 2026,
    category: 'renewal',
    categoryLabel: '都更案',
    location: '新北市新店區',
    description: '安和段都市更新重建計畫，整合多戶住戶共同推動，打造新北市永續都更示範標竿。',
    fullDescription:
      '新店安和段都市更新案以「整合共贏、永續宜居」為核心，在傑丞建築全案管理與整合協調下，成功整合區域住戶共同參與重建。本案規劃引入 iHome 5.0 工法，使舊屋換新宅、坪數大幅提升，並導入智慧設備與節能系統，為居住者創造現代化且符合百年耐用標準的生活品質，成為新北市都市更新示範標竿。',
    image: 'image/project-3.jpg',
    highlights: ['整合多戶都更共識', '原地重建坪數大幅提升', 'iHome 5.0 全套工法導入', '獲選新北市都更示範案'],
    specs: {
      案件類型: '都市更新重建',
      基地位置: '新北市新店區安和段',
      整合工法: 'iHome 5.0',
      預計完工: '2026'
    },
    technologies: ['centennial', 'energy', 'smart']
  }
]

export const useProjects = () => {
  const base = useRuntimeConfig().app.baseURL
  const withBase = (path: string) => `${base}${path}`.replace(/([^:]\/)\/+/g, '$1')

  const resolved = projects.map((p) => ({ ...p, image: withBase(p.image) }))

  const getProject = (id: string | number): Project | undefined =>
    resolved.find((p) => p.id === Number(id))

  // 依 iHome 工法篩選（建案詳情頁使用）
  const projectsByTech = (key: string) =>
    resolved.filter((p) => p.technologies.includes(key))

  // 依案件類型篩選（portfolio 頁使用）
  const projectsByCategory = (key: string) =>
    key === 'All' ? resolved : resolved.filter((p) => p.category === key)

  return { projects: resolved, getProject, projectsByTech, projectsByCategory }
}
