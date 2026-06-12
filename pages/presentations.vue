<template>
  <div class="bg-warm-white min-h-screen">
    <!-- 區塊1: 暗色 Hero -->
    <section class="grain-dark relative h-[45vh] flex items-center overflow-hidden bg-charcoal">
      <div class="absolute inset-0 z-0">
        <img
          src="/image/hero-background.jpg"
          alt="建築標章介紹"
          class="w-full h-full object-cover opacity-35 animate-slow-zoom"
          loading="eager" fetchpriority="high" decoding="async"
        >
        <div class="absolute inset-0 bg-gradient-to-r from-charcoal/90 via-charcoal/60 to-transparent"></div>
      </div>
      <div class="container-custom relative z-10">
        <div class="max-w-3xl">
          <div class="glass-dark rounded-full px-4 py-1.5 inline-block mb-4 animate-fade-in-up">
            <span class="font-mono text-emerald-brand-light text-[10px] tracking-[0.4em] uppercase">Certifications</span>
          </div>
          <div class="dim-line dim-line-light w-20 mb-5 animate-fade-in-up" style="animation-delay: 0.1s"></div>
          <h1 class="font-serif text-5xl md:text-7xl text-warm-white font-light mb-5 animate-fade-in-up" style="animation-delay: 0.15s">
            標章介紹
          </h1>
          <p class="font-sans text-lg text-warm-white/60 max-w-xl leading-relaxed animate-fade-in-up" style="animation-delay: 0.3s">
            台灣三大建築標章完整簡報——綠建築 EEWH、智慧建築、建築能效 BERS，點擊卡片即可全螢幕瀏覽。
          </p>
        </div>
      </div>
    </section>

    <!-- 區塊2: 簡報卡片 -->
    <section class="blueprint-grid pt-16 md:pt-24 pb-32 md:pb-48">
      <div class="container-custom">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <a
            v-for="(deck, index) in decks"
            :key="deck.file"
            :href="withBase(deck.file)"
            target="_blank"
            rel="noopener"
            class="glass-card glass-lift rounded-2xl group block animate-fade-in-up"
            :style="`animation-delay: ${0.2 + index * 0.12}s`"
          >
            <!-- 視覺色塊封面 -->
            <div
              class="relative aspect-[4/3] overflow-hidden rounded-t-2xl flex flex-col justify-between p-8 transition-transform duration-1200 elegant-transition group-hover:scale-[1.02]"
              :style="`background:${deck.bg}`"
            >
              <div class="flex justify-between items-start">
                <span class="font-mono text-[10px] tracking-[0.2em] uppercase text-white/70">
                  {{ deck.code }}
                </span>
                <span class="font-mono text-[10px] text-white/40 italic">0{{ index + 1 }}</span>
              </div>
              <div>
                <div class="text-5xl mb-3">{{ deck.icon }}</div>
                <h2 class="font-serif text-2xl font-light text-white leading-tight">
                  {{ deck.title }}
                </h2>
                <p class="font-mono text-[11px] text-white/60 mt-2">{{ deck.version }}</p>
              </div>
              <!-- 懸停開啟提示 -->
              <div class="absolute inset-0 bg-black/0 group-hover:bg-black/10 transition-colors duration-700 flex items-center justify-center">
                <span class="font-sans text-xs tracking-[0.2em] uppercase text-white opacity-0 group-hover:opacity-100 translate-y-2 group-hover:translate-y-0 transition-all duration-500 border border-white/60 px-5 py-2 backdrop-blur-sm">
                  開啟簡報 ↗
                </span>
              </div>
            </div>

            <!-- 資訊區 -->
            <div class="px-6 py-5">
              <p class="font-sans text-sm text-charcoal/60 leading-relaxed mb-3">
                {{ deck.description }}
              </p>
              <div class="flex flex-wrap gap-2">
                <span
                  v-for="tag in deck.tags"
                  :key="tag"
                  class="font-mono text-[10px] tracking-wider px-2 py-1 rounded-sm"
                  :style="`background:${deck.tagBg};color:${deck.tagColor}`"
                >
                  {{ tag }}
                </span>
              </div>
            </div>
          </a>
        </div>

        <!-- 使用提示 -->
        <div class="mt-20 text-center animate-fade-in-up" style="animation-delay: 0.6s">
          <p class="font-mono text-[11px] text-charcoal/30 tracking-wider">
            簡報以 Reveal.js 製作 · 支援全螢幕（F 鍵）· 總覽模式（Esc 鍵）
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
// 靜態 HTML 簡報置於 public/，需依 baseURL 補上子路徑前綴（GitHub Pages 子路徑部署用）。
const base = useRuntimeConfig().app.baseURL
const withBase = (path) => `${base}${path}`.replace(/([^:]\/)\/+/g, '$1')

const decks = [
  {
    file: 'presentation.html',
    code: 'EEWH',
    icon: '🌿',
    title: '綠建築標章',
    version: '2023 版 · 基本型 × 住宅型',
    description: '台灣綠建築 EEWH 制度解析，涵蓋九大指標、基本型與住宅型評估差異、五個認證等級，並串接傑丞建築機構代表專案。',
    tags: ['EEWH', '九大指標', '基本型', '住宅型'],
    bg: 'linear-gradient(135deg, #064e3b 0%, #065f46 60%, #047857 100%)',
    tagBg: '#d1fae5',
    tagColor: '#064e3b',
  },
  {
    file: 'presentation-ib.html',
    code: 'Intelligent Building',
    icon: '📡',
    title: '智慧建築標章',
    version: '2024 版 · 六大評估指標',
    description: '智慧建築標章六大指標深度解析：資訊通信、安全防災、健康舒適、節能管理、設備整合、貼心便利，含 2024 版 AI 與數位孿生更新。',
    tags: ['六大指標', 'AI 智慧化', '數位孿生', '5G'],
    bg: 'linear-gradient(135deg, #0f172a 0%, #1e3a8a 65%, #1d4ed8 100%)',
    tagBg: '#dbeafe',
    tagColor: '#1e40af',
  },
  {
    file: 'presentation-bers.html',
    code: 'BERS',
    icon: '⚡',
    title: '建築能效評估標示',
    version: '2024 版 · 八個能效等級',
    description: '建築能效評估標示 BERS 完整介紹：EUI 能源使用強度、八個能效等級、BERS 與 BERSh 差異，以及邁向 2050 淨零建築的路徑。',
    tags: ['EUI', '能效分級', '1+ 至 7 級', '淨零'],
    bg: 'linear-gradient(135deg, #1c1917 0%, #b45309 65%, #d97706 100%)',
    tagBg: '#fef3c7',
    tagColor: '#b45309',
  },
]
</script>
