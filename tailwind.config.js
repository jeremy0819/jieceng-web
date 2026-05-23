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
      fontFamily: {
        sans: ['Inter', 'Noto Sans TC', 'sans-serif'],
        serif: ['Playfair Display', 'serif'],
        mono: ['JetBrains Mono', 'monospace'],
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