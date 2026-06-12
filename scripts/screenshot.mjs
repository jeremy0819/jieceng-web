/**
 * 視覺驗證腳本：對全站頁面截圖（桌機 + 手機），輸出至 /tmp/shots/。
 * 用法：node scripts/screenshot.mjs [baseURL]
 */
import { chromium } from 'playwright'
import { mkdirSync } from 'node:fs'

const BASE = process.argv[2] || 'http://localhost:3000'
const OUT = '/tmp/shots'
mkdirSync(OUT, { recursive: true })

const pages = [
  ['home', '/'],
  ['about', '/about'],
  ['pcm', '/pcm'],
  ['ihome', '/ihome'],
  ['portfolio', '/portfolio'],
  ['briefing', '/briefing'],
  ['presentations', '/presentations'],
  ['contact', '/contact'],
  ['project-1', '/project/1'],
]

const viewports = [
  ['desktop', { width: 1440, height: 900 }],
  ['mobile', { width: 390, height: 844 }],
]

const browser = await chromium.launch()
const errors = []

for (const [vpName, viewport] of viewports) {
  // reducedMotion: 捲動進場引擎會直接顯示所有元素，避免截圖與動畫賽跑
  const ctx = await browser.newContext({ viewport, reducedMotion: 'reduce' })
  const page = await ctx.newPage()
  page.on('console', (msg) => {
    if (msg.type() === 'error') errors.push(`[${vpName}] ${page.url()}: ${msg.text().slice(0, 200)}`)
  })
  page.on('pageerror', (err) => errors.push(`[${vpName}] ${page.url()}: PAGEERROR ${String(err).slice(0, 200)}`))

  for (const [name, path] of pages) {
    await page.goto(`${BASE}${path}`, { waitUntil: 'networkidle', timeout: 30000 }).catch((e) => {
      errors.push(`[${vpName}] ${path}: NAV FAIL ${e.message.slice(0, 120)}`)
    })
    // 等捲動進場觸發：捲到底再回頂，讓所有 reveal 元素顯示
    await page.evaluate(async () => {
      await new Promise((r) => {
        let y = 0
        const step = () => {
          y += 700
          window.scrollTo(0, y)
          if (y < document.body.scrollHeight) setTimeout(step, 120)
          else { window.scrollTo(0, 0); setTimeout(r, 400) }
        }
        step()
      })
    })
    await page.screenshot({ path: `${OUT}/${name}-${vpName}.png`, fullPage: true })
    // 檢查橫向溢出（手機跑版主因）
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth)
    if (overflow > 2) errors.push(`[${vpName}] ${path}: HORIZONTAL OVERFLOW ${overflow}px`)
  }
  await ctx.close()
}

await browser.close()
console.log(errors.length ? `ISSUES:\n${errors.join('\n')}` : 'ALL CLEAN')
