/**
 * 數字滾動（count-up）引擎 — 漸進增強。
 *
 * 用法：<span data-counter="20" data-suffix="+">20+</span>
 *  - SSR 直接輸出最終值（SEO / 無 JS 安全），
 *    元素滑入視窗後從 0 滾動至 data-counter 指定的數字。
 *  - data-suffix 為數字後綴（+、% 等），data-prefix 為前綴。
 *  - 與 reveal.client.ts 相同，等 hydration 完成後才接管 DOM。
 */
export default defineNuxtPlugin((nuxtApp) => {
  if (!process.client) return

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches

  const animate = (el: HTMLElement) => {
    const target = parseFloat(el.dataset.counter || '0')
    if (!Number.isFinite(target)) return
    const prefix = el.dataset.prefix || ''
    const suffix = el.dataset.suffix || ''
    if (reduceMotion) {
      el.textContent = `${prefix}${target}${suffix}`
      return
    }
    const duration = 1600
    const startTime = performance.now()
    const easeOut = (t: number) => 1 - Math.pow(1 - t, 3)
    const step = (now: number) => {
      const p = Math.min((now - startTime) / duration, 1)
      el.textContent = `${prefix}${Math.round(easeOut(p) * target)}${suffix}`
      if (p < 1) requestAnimationFrame(step)
    }
    requestAnimationFrame(step)
  }

  const io = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          animate(entry.target as HTMLElement)
          io.unobserve(entry.target)
        }
      }
    },
    { threshold: 0.4 }
  )

  const seen = new WeakSet<Element>()
  const observe = (el: Element) => {
    if (seen.has(el)) return
    seen.add(el)
    io.observe(el)
  }

  const scan = (node: any) => {
    if (!node || node.nodeType !== 1) return
    if (node.dataset?.counter !== undefined) observe(node)
    node.querySelectorAll?.('[data-counter]').forEach(observe)
  }

  const start = () => {
    scan(document.body)
    const mo = new MutationObserver((mutations) => {
      for (const m of mutations) m.addedNodes.forEach(scan)
    })
    mo.observe(document.body, { childList: true, subtree: true })
  }

  nuxtApp.hook('app:suspense:resolve', start)
})
