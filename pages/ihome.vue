<template>
  <div class="bg-[#050505] min-h-screen">
    <!-- 區塊1: 頁面標頭 -->
    <section class="pt-32 md:pt-40 pb-20 md:pb-28 bg-[#050505]">
      <div class="container-custom">
        <div class="max-w-4xl">
          <div class="flex items-center gap-4 mb-10 animate-fade-in-up">
            <span class="w-12 h-px bg-[#10b981]"></span>
            <span class="font-mono text-[10px] uppercase tracking-[0.45em] text-[#10b981]">Architectural Strategy</span>
          </div>
          <h1 class="font-serif text-6xl md:text-[7rem] font-light leading-[0.9] tracking-tight text-white mb-10 animate-fade-in-up" style="animation-delay: 0.1s">
            iHome 5.0
            <br />
            <span class="italic text-white/25">The Method.</span>
          </h1>
          <p class="font-sans text-lg md:text-xl font-light text-white/55 leading-relaxed max-w-2xl tracking-zh animate-fade-in-up" style="animation-delay: 0.25s">
            我們將「iHome 5.0」專利工法定義為品牌的技術脊樑。對傑丞而言，美學不應是奢侈的堆砌，而是基於物理性能的自然延伸——五大宅，是我們對一個家百年承諾的具體實踐。
          </p>
        </div>
      </div>
    </section>

    <!-- 區塊2: 五大宅 左右交錯陳列 -->
    <section class="pb-32 md:pb-48 bg-[#050505]">
      <div class="container-custom">
        <div class="space-y-32 md:space-y-56">
          <div
            v-for="(t, idx) in iHomeTech"
            :key="t.key"
            class="grid lg:grid-cols-12 gap-12 lg:gap-24 items-center"
          >
            <!-- 文字側 -->
            <div :class="['lg:col-span-5 animate-fade-in-up', idx % 2 !== 0 ? 'lg:order-2' : '']">
              <span class="block font-mono text-4xl text-white/10 mb-7">{{ t.num }}</span>
              <h2 class="font-serif text-5xl md:text-6xl font-light text-white mb-3 tracking-zh">
                {{ t.title }}
                <span class="text-white/30 text-3xl ml-2">{{ t.en }}</span>
              </h2>
              <p class="font-mono text-[11px] font-medium uppercase tracking-[0.35em] text-[#10b981] mb-9">
                {{ t.subtitle }}
              </p>
              <p class="font-sans text-lg text-white/55 font-light leading-relaxed mb-12 tracking-zh">
                {{ t.desc }}
              </p>
              <div class="space-y-9">
                <div v-for="d in t.details" :key="d.label">
                  <h3 class="font-mono text-[10px] font-bold uppercase tracking-[0.2em] text-white/30 mb-2.5">{{ d.label }}</h3>
                  <p class="font-sans text-white/50 font-light leading-relaxed tracking-zh">{{ d.value }}</p>
                </div>
              </div>
            </div>

            <!-- 圖片側 -->
            <div :class="['lg:col-span-7 animate-fade-in-up', idx % 2 !== 0 ? 'lg:order-1' : '']" style="animation-delay: 0.15s">
              <div class="relative aspect-[16/11] overflow-hidden rounded-[2.5rem] bg-white/[0.06] ring-1 ring-white/[0.10] shadow-[0_8px_40px_rgba(0,0,0,0.5)] group">
                <img
                  :src="t.image"
                  :alt="t.title"
                  class="w-full h-full object-cover opacity-75 transition-all duration-1200 elegant-transition group-hover:scale-105 group-hover:opacity-100"
                  loading="lazy" decoding="async"
                >
                <div class="absolute top-7 left-7">
                  <span class="font-mono text-[10px] tracking-[0.25em] uppercase text-white/80 glass rounded-full px-3 py-1.5">
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
    <section
      class="py-28 md:py-36 grain-dark bg-[#0a0a0a] border-t border-white/[0.08] relative overflow-hidden"
    >
      <div
        class="absolute inset-0 pointer-events-none"
        style="background: radial-gradient(ellipse at center, rgba(16,185,129,0.08) 0%, transparent 70%)"
      ></div>
      <div class="container-custom relative z-10 text-center">
        <h2 class="font-serif text-3xl md:text-5xl font-light text-white mb-10 animate-fade-in-up tracking-zh">
          想了解 iHome 5.0 如何落實於每一個家？
        </h2>
        <div class="flex flex-wrap justify-center gap-4 animate-fade-in-up" style="animation-delay: 0.15s">
          <NuxtLink
            to="/portfolio"
            class="inline-flex items-center gap-3 px-10 py-4 bg-[#10b981] text-[#050505] font-mono text-xs tracking-[0.2em] uppercase rounded-full hover:bg-[#0d9668] transition-colors duration-700 elegant-transition"
          >
            探索建案實踐
          </NuxtLink>
          <NuxtLink
            to="/contact"
            class="inline-flex items-center gap-3 px-10 py-4 glass rounded-full font-mono text-xs tracking-[0.2em] uppercase text-white/70 hover:text-white hover:bg-white/[0.12] transition-all duration-700 elegant-transition"
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
