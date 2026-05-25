/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",
  ],
  theme: {
    extend: {
      // 視覺基因：顏色定義
      colors: {
        'warm-white': '#fafaf9',  // 暖米白色背景
        'charcoal': '#1a1a1a',    // 深炭黑色文字
        'emerald-brand': {
          DEFAULT: '#064e3b',      // emerald-950 (品牌深綠)
          light: '#10b981',        // emerald-500
          soft: '#ecfdf5',         // emerald-50
        }
      },
      // 視覺基因：字體定義
      // Latin 字體放最前面（只含西文字形），中文交給 Noto 後備字體渲染，
      // 如此英文得到 Playfair / Inter 的精品感，中文得到思源宋體 / 黑體的工整氣質。
      fontFamily: {
        sans: ['Inter', 'Noto Sans TC', 'sans-serif'],
        serif: ['Playfair Display', 'Noto Serif TC', 'serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      letterSpacing: {
        // 中文專用字距：比預設稍微鬆開，呈現留白的呼吸感而不致鬆散
        'zh': '0.05em',
        'zh-wide': '0.12em',
      },
      // 高級感動畫：定義自定義貝茲曲線與時長
      transitionTimingFunction: {
        'elegant': 'cubic-bezier(0.16, 1, 0.3, 1)',
      },
      transitionDuration: {
        '1200': '1200ms',
      },
      // 全局頁面載入動畫
      keyframes: {
        'fade-in-up': {
          'from': {
            opacity: '0',
            transform: 'translateY(30px)'
          },
          'to': {
            opacity: '1',
            transform: 'translateY(0)'
          },
        }
      },
      animation: {
        'fade-in-up': 'fade-in-up 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards',
      }
    },
  },
  plugins: [],
}