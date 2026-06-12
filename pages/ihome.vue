<template>
  <div class="bg-warm-white min-h-screen">
    <!-- 區塊1: 頁面標頭 -->
    <section class="pt-32 md:pt-40 pb-20 md:pb-28 bg-warm-white">
      <div class="container-custom">
        <div class="max-w-4xl">
          <div class="flex items-center gap-4 mb-10 animate-fade-in-up">
            <span class="w-12 h-px bg-emerald-brand"></span>
            <span class="font-mono text-[10px] uppercase tracking-[0.45em] text-emerald-brand">Architectural Strategy</span>
          </div>
          <h1 class="text-charcoal font-serif text-5xl md:text-[7rem] font-light leading-[0.9] tracking-tight mb-10 animate-fade-in-up" style="animation-delay: 0.1s">
            iHome 5.0
            <br />
            <span class="italic text-stroke">The Method.</span>
          </h1>
          <p class="text-charcoal/55 font-sans text-lg md:text-xl font-light leading-relaxed max-w-2xl tracking-zh animate-fade-in-up" style="animation-delay: 0.25s">
            我們將「iHome 5.0」專利工法定義為品牌的技術脊樑。對傑丞而言，美學不應是奢侈的堆砌，而是基於物理性能的自然延伸——五大宅，是我們對一個家百年承諾的具體實踐。
          </p>
          <div class="flex items-center gap-5 mt-10 animate-fade-in-up" style="animation-delay: 0.35s">
            <div class="dim-line w-24"></div>
            <span class="font-mono text-[9px] tracking-[0.3em] uppercase text-charcoal/35">Five Systems — Patented Methodology</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊2: 五大宅 左右交錯陳列 -->
    <section class="pb-32 md:pb-48 bg-warm-white relative overflow-hidden">
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
