<template>
  <div class="bg-warm-white min-h-screen">
    <!-- 區塊1: 沉浸式 Hero -->
    <section class="grain-dark relative h-[55vh] flex items-center overflow-hidden bg-charcoal">
      <div class="absolute inset-0 z-0">
        <img
          src="/image/hero-background.jpg"
          alt="iHome 5.0 五大宅工法"
          class="w-full h-full object-cover opacity-35 scale-105 animate-slow-zoom"
          loading="eager" fetchpriority="high" decoding="async"
        >
        <div class="absolute inset-0 bg-gradient-to-r from-charcoal/90 via-charcoal/60 to-transparent"></div>
      </div>
      <div class="container-custom relative z-10">
        <div class="max-w-3xl">
          <div class="glass-dark rounded-full px-4 py-1.5 inline-block mb-4 animate-fade-in-up">
            <span class="font-mono text-emerald-brand-light text-[10px] tracking-[0.4em] uppercase">Architectural Strategy</span>
          </div>
          <div class="dim-line dim-line-light w-20 mb-6 animate-fade-in-up" style="animation-delay: 0.1s"></div>
          <h1 class="font-serif text-5xl md:text-7xl text-warm-white font-light tracking-tight mb-5 animate-fade-in-up" style="animation-delay: 0.15s">
            iHome 5.0<br />
            <span class="italic text-warm-white/40">The Method.</span>
          </h1>
          <p class="font-sans text-lg text-warm-white/60 max-w-xl leading-relaxed tracking-zh animate-fade-in-up" style="animation-delay: 0.3s">
            傑丞建築的技術脊樑——五大宅系統，是我們對每個家百年承諾的具體實踐。
          </p>
        </div>
      </div>
      <div class="hidden md:flex absolute right-10 bottom-16 z-10 flex-col items-center gap-5">
        <span class="text-vertical font-serif text-sm tracking-[0.5em] text-warm-white/35">五大系統 · 專利工法</span>
        <div class="w-px h-14 bg-warm-white/20"></div>
      </div>
    </section>

    <!-- 五大宅系統概覽帶 (DARK) -->
    <section class="grain-dark py-12 bg-charcoal border-t border-warm-white/5">
      <div class="container-custom">
        <div class="grid grid-cols-2 md:grid-cols-5 gap-3">
          <div
            v-for="(t, i) in iHomeTech" :key="t.key"
            class="glass-dark rounded-xl p-4 text-center animate-fade-in-up group hover:bg-warm-white/[0.05] transition-colors duration-500"
            :style="`animation-delay: ${i * 0.08}s`"
          >
            <div class="font-mono text-2xl text-warm-white/20 font-light mb-1">{{ t.num }}</div>
            <div class="font-serif text-lg text-warm-white mb-1 tracking-zh">{{ t.title }}</div>
            <div class="font-mono text-[9px] tracking-[0.25em] uppercase text-emerald-brand-light opacity-70">{{ t.en }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊2: 五大宅 左右交錯陳列 -->
    <section class="pt-20 pb-32 md:pt-28 md:pb-48 bg-warm-white relative overflow-hidden">
      <div class="container-custom">
        <div class="space-y-32 md:space-y-56">
          <div
            v-for="(t, idx) in iHomeTech"
            :key="t.key"
            class="relative grid lg:grid-cols-12 gap-12 lg:gap-24 items-center"
          >
            <!-- 圖紙水印編號 -->
            <span class="sheet-num -top-10 opacity-60" :class="idx % 2 !== 0 ? 'right-0' : 'left-0'" aria-hidden="true">{{ t.num }}</span>

            <!-- 文字側 -->
            <div :class="['lg:col-span-5 relative z-10 animate-fade-in-up', idx % 2 !== 0 ? 'lg:order-2' : '']">
              <h2 class="text-charcoal font-serif text-4xl md:text-5xl font-light mb-3 tracking-zh">
                {{ t.title }}
                <span class="text-charcoal/25 text-2xl md:text-3xl ml-2">{{ t.en }}</span>
              </h2>
              <p class="text-emerald-brand font-mono text-[11px] uppercase tracking-[0.35em]">
                {{ t.subtitle }}
              </p>
              <div class="dim-line w-16 mt-4 mb-9"></div>
              <p class="text-charcoal/55 font-sans text-lg font-light leading-relaxed mb-12 tracking-zh">
                {{ t.desc }}
              </p>
              <div class="space-y-9">
                <div v-for="d in t.details" :key="d.label">
                  <h3 class="text-charcoal/30 font-mono text-[10px] uppercase tracking-[0.2em] mb-2.5">{{ d.label }}</h3>
                  <p class="text-charcoal/50 font-sans font-light leading-relaxed tracking-zh">{{ d.value }}</p>
                </div>
              </div>
            </div>

            <!-- 圖片側 -->
            <div :class="['lg:col-span-7 relative corner-marks', idx % 2 !== 0 ? 'lg:order-1' : '']">
              <div class="img-reveal relative aspect-[16/11] overflow-hidden rounded-[2.5rem] bg-stone-100 shadow-md ring-1 ring-black/[0.07] group" style="animation-delay: 0.15s">
                <img
                  :src="t.image"
                  :alt="t.title"
                  class="w-full h-full object-cover grayscale transition-all duration-1200 elegant-transition group-hover:grayscale-0 group-hover:scale-105"
                  loading="lazy" decoding="async"
                >
                <div class="absolute top-7 left-7">
                  <span class="glass rounded-full px-3 py-1.5 font-mono text-[10px] tracking-[0.25em] uppercase text-charcoal/60">
                    {{ t.title }} · {{ t.en }}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊3: CTA -->
    <section class="py-28 md:py-36 grain-dark blueprint-grid-dark bg-charcoal border-t border-white/5">
      <div class="container-custom relative z-10 text-center">
        <h2 class="text-warm-white font-serif text-3xl md:text-5xl font-light mb-10 animate-fade-in-up tracking-zh">
          想了解 iHome 5.0 如何落實於每一個家？
        </h2>
        <div class="flex flex-wrap justify-center gap-4 animate-fade-in-up" style="animation-delay: 0.15s">
          <NuxtLink
            to="/portfolio"
            class="btn-sheen inline-flex items-center gap-3 px-10 py-4 bg-warm-white text-charcoal rounded-full font-mono text-xs tracking-[0.2em] uppercase hover:bg-emerald-brand hover:text-warm-white transition-colors duration-700 elegant-transition"
          >
            探索建案實踐
          </NuxtLink>
          <NuxtLink
            to="/contact"
            class="inline-flex items-center gap-3 px-10 py-4 ring-1 ring-warm-white/35 text-warm-white rounded-full font-mono text-xs tracking-[0.2em] uppercase hover:ring-warm-white/60 transition-all duration-700 elegant-transition"
          >
            預約諮詢
          </NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const { iHomeTech } = useIHome()

useSeoMeta({
  title: 'iHome 5.0 五大宅工法 - 傑丞建築機構',
  description: 'iHome 5.0 是傑丞建築的專利核心工法，涵蓋百年宅（耐震）、健康宅（抑菌）、節能宅（低碳）、智慧宅（智能家居）、履歷宅（全程溯源）五大系統。',
  ogTitle: 'iHome 5.0 五大宅工法',
  ogDescription: '百年宅、健康宅、節能宅、智慧宅、履歷宅——傑丞建築的五大技術承諾。',
  ogImage: 'https://jeremy0819.github.io/jieceng-web/image/hero-background.jpg',
  ogType: 'website',
  twitterCard: 'summary_large_image',
})
</script>
