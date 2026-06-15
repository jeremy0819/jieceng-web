<template>
  <div class="bg-warm-white min-h-screen">
    <!-- 區塊1: 沉浸式 Hero -->
    <section class="grain-dark relative h-[60vh] flex items-center overflow-hidden bg-charcoal">
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
            <span class="font-mono text-emerald-brand-light text-[10px] tracking-[0.4em] uppercase">超未來建築 · Evolved Living</span>
          </div>
          <div class="dim-line dim-line-light w-20 mb-6 animate-fade-in-up" style="animation-delay: 0.1s"></div>
          <h1 class="font-serif text-5xl md:text-7xl text-warm-white font-light tracking-tight mb-5 animate-fade-in-up" style="animation-delay: 0.15s">
            iHome 5.0<br />
            <span class="italic text-warm-white/40">傑丞先進 DNA。</span>
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

    <!-- 區塊1.5: 品牌 DNA 三大支柱 (DARK) -->
    <section class="grain-dark blueprint-grid-dark py-20 md:py-24 bg-charcoal border-t border-warm-white/5 relative overflow-hidden">
      <span class="sheet-num-light top-10 -right-4" aria-hidden="true">DNA</span>
      <div class="container-custom relative z-10">
        <div class="flex items-center gap-4 mb-14 animate-fade-in-up">
          <span class="font-mono text-[10px] tracking-[0.3em] uppercase text-emerald-brand-light">The Philosophy</span>
          <div class="dim-line dim-line-light w-12"></div>
          <span class="font-mono text-[10px] tracking-[0.3em] uppercase text-warm-white/40">Evolved Living</span>
        </div>
        <div class="grid md:grid-cols-3 gap-px bg-warm-white/[0.06] rounded-2xl overflow-hidden">
          <div
            v-for="(p, i) in iHomePillars" :key="p.code"
            class="bg-charcoal p-8 md:p-10 animate-fade-in-up group hover:bg-warm-white/[0.03] transition-colors duration-700"
            :style="`animation-delay: ${i * 0.12}s`"
          >
            <div class="flex items-baseline gap-3 mb-6">
              <span class="font-mono text-[11px] tracking-[0.3em] uppercase text-emerald-brand-light">{{ p.code }}</span>
              <span class="font-serif text-3xl text-warm-white font-light">{{ p.title }}</span>
            </div>
            <p class="font-sans text-sm text-warm-white/55 font-light leading-relaxed tracking-zh">{{ p.desc }}</p>
            <div class="dim-line dim-line-light w-10 mt-8 group-hover:w-20 transition-all duration-700"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 五大宅系統概覽帶 (DARK) — 附 DNA 指標 -->
    <section class="grain-dark py-12 bg-charcoal border-t border-warm-white/5">
      <div class="container-custom">
        <div class="grid grid-cols-2 md:grid-cols-5 gap-3">
          <a
            v-for="(t, i) in iHomeTech" :key="t.key"
            :href="`#${t.key}`"
            class="glass-dark rounded-xl p-5 text-center animate-fade-in-up group hover:bg-warm-white/[0.05] transition-colors duration-500"
            :style="`animation-delay: ${i * 0.08}s`"
          >
            <div class="font-mono text-2xl text-warm-white/15 font-light mb-2">{{ t.num }}</div>
            <div class="font-serif text-lg text-warm-white mb-2 tracking-zh">{{ t.title }}</div>
            <div class="flex items-baseline justify-center gap-1 mb-1">
              <span class="font-serif text-2xl text-emerald-brand-light font-light leading-none">{{ t.metric.value }}</span>
              <span class="font-mono text-[8px] tracking-[0.15em] uppercase text-emerald-brand-light/70">{{ t.metric.unit }}</span>
            </div>
            <div class="font-mono text-[8px] tracking-[0.2em] uppercase text-warm-white/30">{{ t.metric.caption }}</div>
          </a>
        </div>
      </div>
    </section>

    <!-- 區塊2: 五大宅 左右交錯陳列 -->
    <section class="pt-20 pb-24 md:pt-24 md:pb-32 bg-warm-white relative overflow-hidden">
      <div class="container-custom">
        <div class="space-y-20 md:space-y-28">
          <div
            v-for="(t, idx) in iHomeTech"
            :key="t.key"
            :id="t.key"
            class="relative grid lg:grid-cols-12 gap-12 lg:gap-24 items-center scroll-mt-24"
          >
            <!-- 圖紙水印編號 -->
            <span class="sheet-num -top-10 opacity-60" :class="idx % 2 !== 0 ? 'right-0' : 'left-0'" aria-hidden="true">{{ t.num }}</span>

            <!-- 文字側 -->
            <div :class="['lg:col-span-5 relative z-10 animate-fade-in-up', idx % 2 !== 0 ? 'lg:order-2' : '']">
              <!-- DNA 標語 -->
              <div class="flex items-center gap-3 mb-5">
                <span class="font-mono text-[10px] tracking-[0.3em] uppercase text-emerald-brand">{{ t.dna }}</span>
                <div class="dim-line w-10"></div>
              </div>
              <h2 class="text-charcoal font-serif text-4xl md:text-5xl font-light mb-2 tracking-zh">
                {{ t.title }}
              </h2>
              <p class="text-charcoal/30 font-serif italic text-xl md:text-2xl mb-4">{{ t.en }}</p>
              <p class="text-emerald-brand font-mono text-[11px] uppercase tracking-[0.35em]">
                {{ t.subtitle }}
              </p>

              <!-- 量化指標徽章 -->
              <div class="flex items-end gap-4 mt-8 mb-8">
                <div class="flex items-baseline gap-1.5">
                  <span class="font-serif text-6xl md:text-7xl font-light text-charcoal leading-none tracking-tight">{{ t.metric.value }}</span>
                  <span v-if="t.metric.unit" class="font-mono text-sm tracking-[0.15em] uppercase text-emerald-brand">{{ t.metric.unit }}</span>
                </div>
                <span class="font-sans text-sm text-charcoal/40 tracking-zh pb-2">{{ t.metric.caption }}</span>
              </div>

              <p class="text-charcoal/55 font-sans text-lg font-light leading-relaxed mb-10 tracking-zh">
                {{ t.desc }}
              </p>

              <!-- 工法/設備清單 chips -->
              <div class="flex flex-wrap gap-2 mb-10">
                <span
                  v-for="f in t.features" :key="f"
                  class="glass font-mono text-[11px] tracking-zh px-3.5 py-1.5 rounded-full text-charcoal/55 ring-1 ring-charcoal/10"
                >
                  {{ f }}
                </span>
              </div>

              <div class="space-y-7 border-t border-stone-200 pt-9">
                <div v-for="d in t.details" :key="d.label">
                  <h3 class="text-charcoal/30 font-mono text-[10px] uppercase tracking-[0.2em] mb-2.5">{{ d.label }}</h3>
                  <p class="text-charcoal/50 font-sans font-light leading-relaxed tracking-zh">{{ d.value }}</p>
                </div>
              </div>
            </div>

            <!-- 圖片側 -->
            <div :class="['lg:col-span-7 relative corner-marks pb-6', idx % 2 !== 0 ? 'lg:order-1' : '']">
              <div class="relative aspect-[16/11] overflow-hidden rounded-[2.5rem] bg-stone-100 shadow-md ring-1 ring-black/[0.07] group animate-fade-in-up" :style="`animation-delay: 0.15s`">
                <img
                  :src="t.image"
                  :alt="t.title"
                  class="w-full h-full object-cover grayscale transition-all duration-1200 elegant-transition group-hover:grayscale-0 group-hover:scale-105"
                  loading="lazy" decoding="async"
                >
                <div class="absolute top-7 left-7">
                  <span class="glass rounded-full px-3 py-1.5 font-mono text-[10px] tracking-[0.25em] uppercase text-charcoal/60">
                    {{ t.en }}
                  </span>
                </div>
                <!-- 浮貼 DNA 指標卡 -->
                <div class="absolute -bottom-5 right-7 glass-card rounded-xl px-5 py-3.5 z-10">
                  <div class="flex items-baseline gap-1">
                    <span class="font-serif text-2xl text-emerald-brand font-light leading-none">{{ t.metric.value }}</span>
                    <span v-if="t.metric.unit" class="font-mono text-[9px] tracking-widest uppercase text-emerald-brand/70">{{ t.metric.unit }}</span>
                  </div>
                  <p class="font-mono text-[9px] tracking-[0.2em] uppercase text-charcoal/40 mt-0.5">{{ t.dna }}</p>
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
const { iHomeTech, iHomePillars } = useIHome()

useSeoMeta({
  title: 'iHome 5.0 五大宅工法 - 傑丞建築機構',
  description: 'iHome 5.0 是傑丞建築的專利核心工法：百年宅（100年耐久結構）、健康宅（當層防疫）、節能宅（BERS第1級能效）、智慧宅（銀級智慧建築）、履歷宅（SGS全程履歷）五大系統。',
  ogTitle: 'iHome 5.0 五大宅工法',
  ogDescription: '百年宅、健康宅、節能宅、智慧宅、履歷宅——傑丞建築的五大技術承諾。',
  ogImage: 'https://jeremy0819.github.io/jieceng-web/image/hero-background.jpg',
  ogType: 'website',
  twitterCard: 'summary_large_image',
})
</script>
