<template>
  <div class="bg-warm-white min-h-screen">
    <!-- 區塊1: 頁面標題區 -->
    <section class="grain-dark relative min-h-[65vh] flex items-center overflow-hidden bg-charcoal">
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
          <h1 class="font-serif text-5xl md:text-7xl font-light text-warm-white leading-tight animate-fade-in-up" style="animation-delay: 0.15s">
            築跡與未來，<br />
            在空間中對話。
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
            <div class="font-mono text-[9px] tracking-[0.35em] uppercase text-warm-white/35">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊3: 理念詳述 -->
    <section class="section-spacing border-t border-stone-100">
      <div class="container-custom">
        <div class="grid grid-cols-1 md:grid-cols-12 gap-16 items-start">
          <!-- 左側：沉浸式大圖 -->
          <div class="md:col-span-7 relative group animate-fade-in-up">
            <div class="overflow-hidden aspect-[4/5] bg-stone-200">
              <img
                src="/image/hero-background.jpg"
                alt="建築設計細節"
                class="w-full h-full object-cover grayscale-[0.25] group-hover:grayscale-0 transition-all duration-1200 elegant-transition group-hover:scale-105"
              >
            </div>
            <div class="absolute -bottom-6 -right-6 w-28 h-28 border-r border-b border-emerald-brand/25 z-[-1]"></div>
            <div class="absolute -top-6 -left-6 w-28 h-28 border-l border-t border-stone-200 z-[-1]"></div>
          </div>

          <!-- 右側：文字內容 -->
          <div class="md:col-span-5 md:pt-16">
            <h2 class="font-serif text-3xl font-light text-charcoal mb-8 animate-fade-in-up" style="animation-delay: 0.2s">
              我們的理念
            </h2>
            <div class="space-y-6 text-charcoal/65 leading-relaxed font-sans animate-fade-in-up" style="animation-delay: 0.35s">
              <p>
                「傑丞建築機構」相信建築不僅是鋼筋水泥的堆疊，更是對環境、人文與未來生活的承諾。我們的設計理念始於對基地紋理的尊重，透過精確的空間規劃，創造出既具功能性又充滿情感的場所。
              </p>
              <p>
                我們致力於將永續材料與前瞻性技術融入設計，確保每個作品都能在美學與環保之間取得平衡，利用自然光影變化，為居住者帶來舒適且富有層次感的空間體驗。
              </p>
            </div>

            <!-- 核心價值清單 -->
            <div class="mt-14 animate-fade-in-up" style="animation-delay: 0.5s">
              <h3 class="font-mono text-[10px] tracking-[0.3em] uppercase text-emerald-brand mb-7">Core Values</h3>
              <ul class="space-y-4">
                <li v-for="item in values" :key="item" class="flex items-center gap-4 group">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-brand shrink-0 transform group-hover:scale-150 transition-transform duration-500"></span>
                  <span class="font-sans text-sm text-charcoal/80 tracking-zh">{{ item }}</span>
                </li>
              </ul>
            </div>

            <!-- 聯絡連結 -->
            <div class="mt-14 animate-fade-in-up" style="animation-delay: 0.7s">
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
  { value: '10+',  label: 'Years of Excellence' },
  { value: '50+',  label: 'Projects Completed' },
  { value: '3',    label: 'Patent Systems' },
  { value: '100%', label: 'Client Commitment' }
]

const values = [
  '永續建築工法 (Sustainable Design)',
  '精確空間規劃 (Precision Planning)',
  '人文與美學對話 (Humanistic Aesthetics)',
  '前瞻性建築技術 (Advanced Technology)'
]

useHead({ title: '關於我們 - 傑丞建築機構' })
</script>
