<template>
  <div class="bg-warm-white min-h-screen">
    <!-- 區塊1: 頁面標題區 -->
    <section class="grain-dark relative min-h-[60vh] flex items-center overflow-hidden bg-charcoal">
      <div class="absolute inset-0 z-0">
        <img
          src="/image/hero-background.jpg"
          alt="關於我們背景"
          class="w-full h-full object-cover opacity-45 animate-slow-zoom"
        >
        <div class="absolute inset-0 bg-gradient-to-r from-charcoal/85 via-charcoal/50 to-transparent"></div>
      </div>

      <div class="container-custom relative z-10">
        <div class="max-w-3xl">
          <span class="font-mono text-emerald-brand-light text-[10px] tracking-[0.4em] uppercase mb-6 block animate-fade-in-up">
            Our Philosophy
          </span>
          <h1 class="font-serif text-6xl md:text-8xl font-light text-warm-white leading-none animate-fade-in-up" style="animation-delay: 0.15s">
            關於
            <br />
            <span class="italic text-warm-white/40">傑丞。</span>
          </h1>
        </div>
      </div>
    </section>

    <!-- 區塊2: 數字亮點 -->
    <section class="grain-dark py-20 md:py-24 bg-charcoal border-t border-warm-white/5">
      <div class="container-custom relative z-10">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-10 md:gap-8">
          <div
            v-for="(stat, i) in stats"
            :key="stat.label"
            class="text-center animate-fade-in-up"
            :style="`animation-delay: ${0.1 + i * 0.1}s`"
          >
            <div class="font-serif text-5xl md:text-6xl text-warm-white font-light mb-3 tracking-tight">{{ stat.value }}</div>
            <div class="font-mono text-[9px] tracking-[0.3em] uppercase text-warm-white/35">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊3: 品牌故事 + 企業核心 -->
    <section class="section-spacing border-t border-stone-100">
      <div class="container-custom">
        <div class="grid lg:grid-cols-12 gap-16 items-start">
          <!-- 左：大圖 -->
          <div class="lg:col-span-5 space-y-12">
            <div class="aspect-[3/4] rounded-3xl overflow-hidden bg-stone-100 shadow-xl ring-1 ring-black/[0.07] grayscale hover:grayscale-0 transition-all duration-1200 elegant-transition group animate-fade-in-up">
              <img
                src="/image/project-4.jpg"
                alt="傑丞團隊與作品"
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-1200 elegant-transition"
              >
            </div>
          </div>

          <!-- 右：文字 -->
          <div class="lg:col-span-7 lg:pl-12 space-y-16">
            <!-- 品牌故事 -->
            <div class="space-y-8">
              <h2 class="font-mono text-xs uppercase tracking-[0.3em] font-bold text-emerald-brand animate-fade-in-up">品牌故事</h2>
              <p class="font-serif text-3xl font-light text-charcoal leading-tight tracking-zh animate-fade-in-up" style="animation-delay: 0.1s">
                傑丞建築不僅是建築商，更是您生活夢想的構築者與守護者。
              </p>
              <div class="space-y-6 font-sans text-lg text-charcoal/55 font-light leading-relaxed max-w-2xl tracking-zh animate-fade-in-up" style="animation-delay: 0.2s">
                <p>我們深信建築應該具有生命力。傑丞團隊由資深建築師、室內設計師與永續科技專家組成，共同追求「極簡、機能、永續」的核心價值。</p>
                <p>在過去的時光中，我們在多個城市核心區留下作品。每一個作品都象徵著我們對品質的挑剔，以及對居住者幸福感的重視。</p>
              </div>
            </div>

            <!-- 企業核心 -->
            <div class="space-y-8 border-t border-stone-200 pt-16">
              <h2 class="font-mono text-xs uppercase tracking-[0.3em] font-bold text-emerald-brand animate-fade-in-up">企業核心</h2>
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

useHead({ title: '關於我們 - 傑丞建築機構' })
</script>
