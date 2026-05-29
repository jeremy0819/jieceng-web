// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-02-17',

  // 開啟 SSG 模式
  ssr: true,
  nitro: {
    prerender: {
      crawlLinks: true,
      autoSubfolderIndex: false,
      // 明確列出所有路由，確保部署到子路徑 (GitHub Pages) 時每頁都會被預先產生。
      // 新增頁面時請一併加入；作品詳情頁對應 composables/useProjects.ts 的 id。
      routes: [
        '/',
        '/about',
        '/portfolio',
        '/pcm',
        '/presentations',
        '/contact',
        '/project/1',
        '/project/2',
        '/project/3',
        '/project/4'
      ]
    }
  },

  modules: ['@nuxtjs/tailwindcss'],

  app: {
    // GitHub Pages 專案站台會部署在 /<repo>/ 子路徑下。
    // 部署工作流程會在 build 時設定 DEPLOY_BASE（例如 /jieceng-web/）；本機開發時預設為 '/'。
    // 注意：不要用 NUXT_APP_BASE_URL，那會在 prerender 時被重複套用而導致整站變成轉址檔。
    baseURL: process.env.DEPLOY_BASE || '/',
    head: {
      htmlAttrs: { lang: 'zh-Hant' },
      title: '傑丞建築機構 | 構築永續未來，定義空間美學',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { hid: 'description', name: 'description', content: '傑丞建築機構，致力於永續未來與空間美學。' }
      ],
      // 在內容繪製前於 <html> 加上 reveal-ready，讓捲動進場不閃爍（見 plugins/reveal.client.ts）
      script: [
        { innerHTML: "document.documentElement.classList.add('reveal-ready')", tagPosition: 'head' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        // Latin 字體 (Playfair / Inter / JetBrains Mono) 負責英文與數字的高級感，
        // Noto Serif TC / Noto Sans TC 作為後備字體負責所有中文字形。
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Noto+Serif+TC:wght@300;400;500;600;700&family=Noto+Sans+TC:wght@300;400;500;700&family=JetBrains+Mono:wght@300&display=swap' }
      ]
    },
    pageTransition: { name: 'page', mode: 'out-in' }
  },

  tailwindcss: {
    cssPath: '~/assets/css/main.css',
    configPath: 'tailwind.config.js',
    exposeConfig: false,
    viewer: true,
  },

  experimental: {
    viewTransition: true
  },

  devtools: { enabled: true }
})
