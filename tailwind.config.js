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
      colors: {
        // 暖象牙色底（主頁面背景）
        'warm-white': '#f5f3ee',
        // 深炭色（文字、暗色區塊）
        'charcoal': '#1c1a17',
        'emerald-brand': {
          DEFAULT: '#064e3b',
          light: '#10b981',
          soft: '#ecfdf5',
        }
      },
      fontFamily: {
        sans: ['Inter', 'Noto Sans TC', 'sans-serif'],
        serif: ['Playfair Display', 'Noto Serif TC', 'serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      letterSpacing: {
        'zh': '0.05em',
        'zh-wide': '0.12em',
      },
      transitionTimingFunction: {
        'elegant': 'cubic-bezier(0.16, 1, 0.3, 1)',
      },
      transitionDuration: {
        '1200': '1200ms',
      },
      keyframes: {
        'fade-in-up': {
          'from': { opacity: '0', transform: 'translateY(28px)' },
          'to': { opacity: '1', transform: 'translateY(0)' },
        },
        'float': {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-8px)' },
        },
        'glow-pulse': {
          '0%, 100%': { opacity: '0.5' },
          '50%': { opacity: '1' },
        },
        'slow-zoom': {
          'from': { transform: 'scale(1)' },
          'to': { transform: 'scale(1.1)' },
        },
        'scroll-bar': {
          '0%': { top: '-40%', opacity: '0' },
          '20%': { opacity: '1' },
          '80%': { opacity: '1' },
          '100%': { top: '140%', opacity: '0' },
        },
        'slide-in-right': {
          'from': { opacity: '0', transform: 'translateX(20px)' },
          'to': { opacity: '1', transform: 'translateX(0)' },
        },
        'scale-in': {
          'from': { opacity: '0', transform: 'scale(0.96)' },
          'to': { opacity: '1', transform: 'scale(1)' },
        },
      },
      animation: {
        'fade-in-up': 'fade-in-up 1.1s cubic-bezier(0.16, 1, 0.3, 1) forwards',
        'float': 'float 6s ease-in-out infinite',
        'glow-pulse': 'glow-pulse 3s ease-in-out infinite',
        'slow-zoom': 'slow-zoom 20s linear infinite alternate',
        'scroll-bar': 'scroll-bar 1.8s cubic-bezier(0.4, 0, 0.2, 1) infinite',
        'slide-in-right': 'slide-in-right 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards',
        'scale-in': 'scale-in 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards',
      }
    },
  },
  plugins: [],
}
