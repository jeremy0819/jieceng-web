<template>
  <div class="bg-[#050505] min-h-screen">
    <!-- 區塊1: 頁面標題區 -->
    <section class="grain-dark relative min-h-[60vh] flex items-center overflow-hidden bg-[#050505]">
      <div class="absolute inset-0 z-0">
        <img
          src="/image/hero-background.jpg"
          alt="關於我們背景"
          class="w-full h-full object-cover opacity-45 animate-slow-zoom"
          loading="eager" fetchpriority="high" decoding="async"
        >
        <div class="absolute inset-0 bg-gradient-to-r from-[#050505]/90 via-[#050505]/50 to-transparent"></div>
      </div>

      <div class="container-custom relative z-10">
        <div class="max-w-3xl">
          <div class="glass rounded-full px-4 py-1.5 inline-block mb-6 animate-fade-in-up">
            <span class="font-mono text-[#10b981] text-[10px] tracking-[0.4em] uppercase">
              Our Philosophy
            </span>
          </div>
          <h1 class="font-serif text-6xl md:text-8xl font-light text-white leading-none animate-fade-in-up" style="animation-delay: 0.15s">
            關於
            <br />
            <span class="italic text-white/40">傑丞。</span>
          </h1>
        </div>
      </div>
    </section>

    <!-- 區塊2: 數字亮點 -->
    <section class="grain-dark py-20 md:py-24 bg-[#050505] border-t border-white/[0.08]">
      <div class="container-custom relative z-10">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
          <div
            v-for="(stat, i) in stats"
            :key="stat.label"
            class="glass rounded-2xl p-6 text-center animate-fade-in-up"
            :style="`animation-delay: ${0.1 + i * 0.1}s`"
          >
            <div class="font-serif text-5xl md:text-6xl text-white font-light mb-3 tracking-tight">{{ stat.value }}</div>
            <div class="font-mono text-[9px] tracking-[0.3em] uppercase text-white/40">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊3: 品牌故事 + 企業核心 -->
    <section class="section-spacing border-t border-white/[0.08] bg-[#050505]">
      <div class="container-custom">
        <div class="grid lg:grid-cols-12 gap-16 items-start">
          <!-- 左：大圖 -->
          <div class="lg:col-span-5 space-y-12">
            <div class="aspect-[3/4] rounded-3xl overflow-hidden bg-white/[0.06] ring-1 ring-white/10 hover:ring-white/20 transition-all duration-1200 elegant-transition group animate-fade-in-up">
              <img
                src="/image/project-4.jpg"
                alt="傑丞團隊與作品"
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-1200 elegant-transition"
                loading="lazy" decoding="async"
              >
            </div>
          </div>

          <!-- 右：文字 -->
          <div class="lg:col-span-7 lg:pl-12 space-y-16">
            <!-- 品牌故事 -->
            <div class="glass-card rounded-2xl p-8 space-y-8 animate-fade-in-up">
              <h2 class="font-mono text-xs uppercase tracking-[0.3em] font-bold text-[#10b981]">品牌故事</h2>
              <p class="font-serif text-3xl font-light text-white leading-tight tracking-zh">
                傑丞建築不僅是建築商，更是您生活夢想的構築者與守護者。
              </p>
              <div class="space-y-6 font-sans text-lg text-white/55 font-light leading-relaxed max-w-2xl tracking-zh">
                <p>我們深信建築應該具有生命力。傑丞團隊由資深建築師、室內設計師與永續科技專家組成，共同追求「極簡、機能、永續」的核心價值。</p>
                <p>在過去的時光中，我們在多個城市核心區留下作品。每一個作品都象徵著我們對品質的挑剔，以及對居住者幸福感的重視。</p>
              </div>
            </div>

            <!-- 企業核心 -->
            <div class="glass-card rounded-2xl p-8 space-y-8 border-t border-white/[0.10] animate-fade-in-up" style="animation-delay: 0.1s">
              <h2 class="font-mono text-xs uppercase tracking-[0.3em] font-bold text-[#10b981]">企業核心</h2>
              <div class="grid md:grid-cols-2 gap-12">
                <div class="animate-fade-in-up" style="animation-delay: 0.1s">
                  <h3 class="font-serif text-xl text-white mb-5 tracking-zh">價值觀</h3>
                  <ul class="space-y-3">
                    <li v-for="v in values" :key="v" class="flex items-center gap-4 group">
                      <span class="w-1.5 h-1.5 rounded-full bg-[#10b981] shrink-0 transform group-hover:scale-150 transition-transform duration-500"></span>
                      <span class="font-sans text-white/65 font-light tracking-zh">{{ v }}</span>
                    </li>
                  </ul>
                </div>
                <div class="animate-fade-in-up" style="animation-delay: 0.2s">
                  <h3 class="font-serif text-xl text-white mb-5 tracking-zh">目標</h3>
                  <ul class="space-y-3">
                    <li v-for="g in goals" :key="g" class="flex items-center gap-4 group">
                      <span class="w-1.5 h-1.5 rounded-full bg-[#10b981] shrink-0 transform group-hover:scale-150 transition-transform duration-500"></span>
                      <span class="font-sans text-white/65 font-light tracking-zh">{{ g }}</span>
                    </li>
                  </ul>
                </div>
              </div>
            </div>

            <!-- 聯絡連結 -->
            <div class="animate-fade-in-up" style="animation-delay: 0.3s">
              <NuxtLink
                to="/contact"
                class="group flex items-center text-white/65 font-serif italic text-lg hover:text-[#10b981] transition-colors duration-500"
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
  </div>
</template>

<script setup>
const stats = [
  { value: '20+', label: 'Years of Heritage' },
  { value: '6', label: 'Green Certifications' },
  { value: '5', label: 'iHome Systems' },
  { value: '100%', label: 'Quality Traceability' }
]

const values = ['誠信開發', '工藝至上', '永續經營', '以人為本']
const goals = ['打造零碳建築', '提升居住品質', '活化都市空間', '引領建築潮流']

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
