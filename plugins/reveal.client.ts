/**
 * 捲動進場（scroll reveal）引擎 — 漸進增強。
 *
 * 作法：
 *  - 全站既有的 `.animate-fade-in-up` 元素，原本是「載入即播放」的 CSS 動畫。
 *  - 本外掛在 client 端接管：把這些元素改為「滑入視窗才揭露」（加上 .is-visible）。
 *  - 搭配 main.css 中 `.reveal-ready` 的閘門：只有 JS 啟用時才改變行為，
 *    JS 關閉時自動退回原本的載入動畫，內容永遠看得到（SEO / 無障礙安全）。
 *  - 原本以 inline style 設定的 animation-delay 會自動轉成 transition-delay，
 *    讓交錯（stagger）節奏完整保留，無需改任何模板。
 */
export default defineNuxtPlugin(() => {
  if (!process.client) return

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches

  const io = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible')
          io.unobserve(entry.target)
        }
      }
    },
    { threshold: 0.12, rootMargin: '0px 0px -6% 0px' }
  )

  const prep = (el) => {
    if (el.__revealed) return
    el.__revealed = true

    // 尊重「減少動態效果」系統偏好：直接顯示，不做動畫
    if (reduceMotion) {
      el.classList.add('is-visible')
      return
    }

    // 把 inline 的 animation-delay 轉為 transition-delay，保留交錯節奏
    const delay = el.style.animationDelay || getComputedStyle(el).animationDelay
    if (delay && delay !== '0s') {
      el.style.transitionDelay = delay
    }

    io.observe(el)
  }

  const scan = (node) => {
    if (!node || node.nodeType !== 1) return
    if (node.classList?.contains('animate-fade-in-up')) prep(node)
    node.querySelectorAll?.('.animate-fade-in-up').forEach(prep)
  }

  const start = () => {
    scan(document.body)
    // 路由切換後 Nuxt 會換入新頁面 DOM，用 MutationObserver 接住新元素
    const mo = new MutationObserver((mutations) => {
      for (const m of mutations) m.addedNodes.forEach(scan)
    })
    mo.observe(document.body, { childList: true, subtree: true })
  }

  if (document.body) start()
  else window.addEventListener('DOMContentLoaded', start)
})
