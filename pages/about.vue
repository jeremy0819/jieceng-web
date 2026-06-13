<template>
  <div class="bg-warm-white min-h-screen">
    <!-- 區塊1: 頁面標題區 (DARK Hero) -->
    <section class="grain-dark relative min-h-[55vh] flex items-center overflow-hidden bg-charcoal">
      <div class="absolute inset-0 z-0">
        <img
          src="/image/hero-background.jpg"
          alt="關於我們背景"
          class="w-full h-full object-cover opacity-45 animate-slow-zoom"
          loading="eager" fetchpriority="high" decoding="async"
        >
        <div class="absolute inset-0 bg-gradient-to-r from-charcoal/85 via-charcoal/50 to-transparent"></div>
      </div>

      <div class="container-custom relative z-10">
        <div class="max-w-3xl">
          <div class="glass-dark rounded-full px-4 py-1.5 inline-block mb-4 animate-fade-in-up">
            <span class="font-mono text-emerald-brand-light text-[10px] tracking-[0.4em] uppercase">
              Our Philosophy
            </span>
          </div>
          <div class="dim-line dim-line-light w-20 mb-6 animate-fade-in-up" style="animation-delay: 0.1s"></div>
          <h1 class="font-serif text-6xl md:text-8xl font-light text-warm-white leading-none animate-fade-in-up" style="animation-delay: 0.15s">
            關於
            <br />
            <span class="italic text-warm-white/40">傑丞。</span>
          </h1>
        </div>
      </div>

      <!-- 直書側註 -->
      <div class="hidden md:flex absolute right-10 bottom-16 z-10 flex-col items-center gap-5">
        <span class="text-vertical font-serif text-sm tracking-[0.5em] text-warm-white/35">以人為本 · 工藝至上</span>
        <div class="w-px h-14 bg-warm-white/20"></div>
      </div>
    </section>

    <!-- 區塊2: 數字亮點 (DARK, keep dark) -->
    <section class="grain-dark blueprint-grid-dark py-16 bg-charcoal border-t border-warm-white/5">
      <div class="container-custom relative z-10">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
          <div
            v-for="(stat, i) in stats"
            :key="stat.label"
            class="glass-dark rounded-xl p-5 text-center animate-fade-in-up"
            :style="`animation-delay: ${0.1 + i * 0.1}s`"
          >
            <div class="font-serif text-5xl text-warm-white font-light mb-3 tracking-tight" :data-counter="stat.num" :data-suffix="stat.suffix">{{ stat.value }}</div>
            <div class="font-mono text-[9px] tracking-[0.3em] uppercase text-warm-white/35">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊3: 品牌故事 + 企業核心 (LIGHT) -->
    <section class="section-spacing border-t border-stone-100 bg-warm-white blueprint-grid relative overflow-hidden">
      <span class="sheet-num top-12 -right-6" aria-hidden="true">01</span>
      <div class="container-custom relative z-10">
        <div class="grid lg:grid-cols-12 gap-16 items-start">
          <!-- 左：大圖 -->
          <div class="lg:col-span-5 space-y-12">
            <div class="relative corner-marks">
              <div class="img-reveal aspect-[3/4] rounded-3xl overflow-hidden bg-stone-100 shadow-xl ring-1 ring-black/[0.07] hover:ring-black/[0.12] transition-all duration-1200 elegant-transition group">
                <img
                  src="/image/project-4.jpg"
                  alt="傑丞團隊與作品"
                  class="w-full h-full object-cover grayscale group-hover:grayscale-0 group-hover:scale-105 transition-all duration-1200 elegant-transition"
                  loading="lazy" decoding="async"
                >
              </div>
            </div>
          </div>

          <!-- 右：文字 -->
          <div class="lg:col-span-7 lg:pl-12 space-y-16">
            <!-- 品牌故事 -->
            <div class="glass-card rounded-2xl p-8 space-y-8 animate-fade-in-up">
              <div class="flex items-center gap-4">
                <span class="font-mono text-[10px] tracking-[0.3em] uppercase text-emerald-brand">SEC. 01</span>
                <div class="dim-line w-12"></div>
                <span class="font-mono text-[10px] tracking-[0.3em] uppercase text-charcoal/40">Brand Story</span>
              </div>
              <p class="font-serif text-3xl font-light text-charcoal leading-tight tracking-zh">
                傑丞建築不僅是建築商，更是您生活夢想的構築者與守護者。
              </p>
              <div class="space-y-6 font-sans text-lg text-charcoal/55 font-light leading-relaxed max-w-2xl tracking-zh">
                <p>我們深信建築應該具有生命力。傑丞團隊由資深建築師、室內設計師與永續科技專家組成，共同追求「極簡、機能、永續」的核心價值。</p>
                <p>在過去的時光中，我們在多個城市核心區留下作品。每一個作品都象徵著我們對品質的挑剔，以及對居住者幸福感的重視。</p>
              </div>
            </div>

            <!-- 企業核心 -->
            <div class="glass-card rounded-2xl p-8 space-y-8 border-t border-stone-200 animate-fade-in-up" style="animation-delay: 0.1s">
              <div class="flex items-center gap-4">
                <span class="font-mono text-[10px] tracking-[0.3em] uppercase text-emerald-brand">SEC. 02</span>
                <div class="dim-line w-12"></div>
                <span class="font-mono text-[10px] tracking-[0.3em] uppercase text-charcoal/40">Core Values</span>
              </div>
              <div class="grid md:grid-cols-2 gap-12">
                <div class="animate-fade-in-up" style="animation-delay: 0.1s">
                  <h3 class="font-serif text-xl text-charcoal mb-5 tracking-zh">價值觀</h3>
                  <ul class="space-y-3">
                    <li v-for="v in values" :key="v" class="flex items-center gap-4 group">
                      <span class="w-1.5 h-1.5 rounded-full bg-emerald-brand shrink-0 transform group-hover:scale-150 transition-transform duration-500"></span>
                      <span class="font-sans text-charcoal/65 font-light tracking-zh">{{ v }}</span>
                    </li>
                  </ul>
                </div>
                <div class="animate-fade-in-up" style="animation-delay: 0.2s">
                  <h3 class="font-serif text-xl text-charcoal mb-5 tracking-zh">目標</h3>
                  <ul class="space-y-3">
                    <li v-for="g in goals" :key="g" class="flex items-center gap-4 group">
                      <span class="w-1.5 h-1.5 rounded-full bg-emerald-brand shrink-0 transform group-hover:scale-150 transition-transform duration-500"></span>
                      <span class="font-sans text-charcoal/65 font-light tracking-zh">{{ g }}</span>
                    </li>
                  </ul>
                </div>
              </div>
            </div>

            <!-- 聯絡連結 -->
            <div class="animate-fade-in-up" style="animation-delay: 0.3s">
              <NuxtLink
                to="/contact"
                class="group flex items-center text-charcoal font-serif italic text-lg hover:text-emerald-brand transition-colors duration-500"
              >
                與我們開始對話
                <svg class="ml-4 w-12 h-4 transform group-hover:translate-x-3 transition-transform duration-700 elegant-transition" fill="none" stroke="currentColor" viewBox="0 0 48 16">
                  <path d="M0 8H46M46 8L39 1M46 8L39 15" stroke-width="1" />
                </svg>
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 里程碑時間軸 (LIGHT) -->
    <section class="section-spacing bg-white border-t border-stone-100 relative overflow-hidden">
      <span class="sheet-num top-12 -left-6" aria-hidden="true">02</span>
      <div class="container-custom relative z-10">
        <div class="flex items-center gap-4 mb-16 animate-fade-in-up">
          <span class="font-mono text-[10px] tracking-[0.3em] uppercase text-emerald-brand">SEC. 03</span>
          <div class="dim-line w-12"></div>
          <span class="font-mono text-[10px] tracking-[0.3em] uppercase text-charcoal/40">Milestones</span>
        </div>
        <div class="max-w-3xl">
          <div
            v-for="(milestone, i) in milestones"
            :key="milestone.year"
            class="grid grid-cols-[72px_1px_1fr] md:grid-cols-[96px_1px_1fr] gap-0 items-stretch animate-fade-in-up"
            :style="`animation-delay: ${i * 0.08}s`"
          >
            <div class="py-6 pr-4 flex items-start justify-end">
              <span class="font-mono text-sm text-emerald-brand/70 tracking-wider">{{ milestone.year }}</span>
            </div>
            <div class="relative flex flex-col items-center">
              <div class="w-2 h-2 rounded-full bg-emerald-brand mt-7 shrink-0 z-10 ring-4 ring-white"></div>
              <div class="flex-1 w-px bg-stone-200"></div>
            </div>
            <div class="py-6 pl-6">
              <h3 class="font-serif text-xl text-charcoal mb-1.5 tracking-zh">{{ milestone.title }}</h3>
              <p class="font-sans text-sm text-charcoal/50 leading-relaxed tracking-zh">{{ milestone.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 品牌關鍵字帶 -->
    <BrandMarquee />
  </div>
</template>

<script setup>
const stats = [
  { value: '20+', num: 20, suffix: '+', label: 'Years of Heritage' },
  { value: '6', num: 6, suffix: '', label: 'Green Certifications' },
  { value: '5', num: 5, suffix: '', label: 'iHome Systems' },
  { value: '100%', num: 100, suffix: '%', label: 'Quality Traceability' }
]

const values = ['誠信開發', '工藝至上', '永續經營', '以人為本']
const goals = ['打造零碳建築', '提升居住品質', '活化都市空間', '引領建築潮流']

const milestones = [
  { year: '2004', title: '傑丞建築機構成立', desc: '於桃園創立，以「誠信開發、品質至上」為創業信念，深耕桃園建築市場。' },
  { year: '2013', title: '導入 SI 工法研發', desc: '引進日本「開放建築」概念，自主研發管線與結構分離之專利工法，成為 iHome 5.0 的技術起點。' },
  { year: '2019', title: 'iHome 5.0 系統完整化', desc: '五大宅系統正式定型，百年宅、健康宅、節能宅、智慧宅、履歷宅成為傑丞建築的核心技術品牌。' },
  { year: '2020', title: '印象羅芙完工', desc: '傑丞旗艦力作，台灣首座榮獲六大建築標章認證的頂級豪宅，創下桃園住宅標竿。' },
  { year: '2022', title: '印象天裔獲鑽石級綠建築', desc: '全台唯一住宅類「鑽石級」綠建築標章，以被動式降載設計樹立永續住宅新高度。' },
  { year: '2024', title: '啟動新店安和段都更整合', desc: '導入 iHome 5.0 全套工法協助都更重建，成為新北市都市更新示範案。' },
]

useSeoMeta({
  title: '關於我們 - 傑丞建築機構',
  description: '傑丞建築機構由資深建築師、室內設計師與永續科技專家組成，二十年深耕桃園與雙北，以誠信開發、工藝至上的精神為每位居住者構築百年住宅。',
  ogTitle: '關於傑丞建築機構',
  ogDescription: '二十年建築工藝與永續承諾，傑丞建築機構品牌故事。',
  ogImage: 'https://jeremy0819.github.io/jieceng-web/image/hero-background.jpg',
  ogType: 'website',
  twitterCard: 'summary_large_image',
})
</script>
