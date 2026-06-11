<template>
  <div class="bg-warm-white min-h-screen">
    <div v-if="project">
      <!-- 區塊1: 沉浸式 Hero（保留深色）-->
      <section class="relative h-[80vh] overflow-hidden bg-charcoal">
        <img
          :src="project.image"
          :alt="project.title"
          class="w-full h-full object-cover opacity-70 scale-105 animate-slow-zoom"
          loading="eager" fetchpriority="high" decoding="async"
        >
        <div class="absolute inset-0 bg-gradient-to-t from-charcoal/88 via-charcoal/25 to-charcoal/15"></div>

        <div class="absolute bottom-0 left-0 w-full pb-16 md:pb-20">
          <div class="container-custom">
            <div class="flex items-center gap-5 mb-6 animate-fade-in-up">
              <span class="glass-dark rounded-full px-4 py-1.5 font-mono text-[10px] text-emerald-brand-light uppercase tracking-widest">
                {{ project.categoryLabel }}
              </span>
              <span class="font-mono text-warm-white/45 text-[10px] uppercase tracking-widest">{{ project.year }} Selection</span>
            </div>
            <h1 class="font-serif text-4xl md:text-8xl text-warm-white font-light tracking-tight animate-fade-in-up" style="animation-delay: 0.15s">
              {{ project.title }}
            </h1>
          </div>
        </div>
      </section>

      <!-- 區塊2: 建案總覽（淺色）-->
      <section class="section-spacing bg-warm-white">
        <div class="container-custom">
          <div class="grid lg:grid-cols-12 gap-16">
            <!-- 左：側欄資訊 -->
            <aside class="lg:col-span-4 space-y-12 animate-fade-in-up">
              <div>
                <div class="glass-card rounded-2xl p-8">
                  <p class="text-emerald-brand font-mono text-[10px] uppercase tracking-[0.3em] mb-6">Technical Standards</p>
                  <dl class="space-y-6">
                    <div v-for="(val, key) in project.specs" :key="key" class="border-b border-stone-200 pb-4 group">
                      <dt class="font-mono text-[10px] text-charcoal/40 uppercase tracking-widest mb-1.5 group-hover:text-emerald-brand transition-colors duration-500">{{ key }}</dt>
                      <dd class="font-serif text-xl text-charcoal">{{ val }}</dd>
                    </div>
                  </dl>
                </div>
              </div>

              <NuxtLink
                to="/portfolio"
                class="group inline-flex items-center text-charcoal/35 hover:text-emerald-brand transition-colors duration-500"
              >
                <svg class="mr-4 w-12 h-4 transform rotate-180 group-hover:-translate-x-3 transition-transform duration-700 elegant-transition" fill="none" stroke="currentColor" viewBox="0 0 48 16">
                  <path d="M0 8H46M46 8L39 1M46 8L39 15" stroke-width="1" />
                </svg>
                <span class="font-mono text-xs uppercase tracking-widest">Back to Portfolio</span>
              </NuxtLink>
            </aside>

            <!-- 右：敘述 -->
            <div class="lg:col-span-8 animate-fade-in-up" style="animation-delay: 0.15s">
              <h2 class="font-serif text-3xl font-light text-charcoal mb-10 tracking-zh">設計思維與工法實踐</h2>
              <p class="font-sans text-lg md:text-xl text-charcoal/60 font-light leading-relaxed first-letter:text-6xl first-letter:font-serif first-letter:mr-3 first-letter:float-left first-letter:text-emerald-brand first-letter:leading-none tracking-zh">
                {{ project.fullDescription }}
              </p>

              <!-- 核心亮點 -->
              <div class="mt-20">
                <div class="flex items-center gap-8 mb-12">
                  <h3 class="font-mono text-xs font-bold uppercase tracking-[0.4em] text-charcoal/30">Case Highlights</h3>
                  <div class="h-px flex-1 bg-stone-200"></div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-12">
                  <div v-for="(h, i) in project.highlights" :key="i" class="flex gap-7 items-start">
                    <span class="font-serif italic text-3xl text-stone-300">0{{ i + 1 }}</span>
                    <p class="font-sans text-charcoal/70 text-lg font-light leading-relaxed tracking-zh pt-1">{{ h }}</p>
                  </div>
                </div>
              </div>

              <!-- 次圖 -->
              <div class="mt-20 grid grid-cols-2 gap-4">
                <div class="aspect-square rounded-2xl bg-stone-100 overflow-hidden">
                  <img :src="project.image" class="w-full h-full object-cover hover:scale-110 transition-transform duration-1200 elegant-transition" loading="lazy" decoding="async">
                </div>
                <div class="aspect-square rounded-2xl bg-stone-100 overflow-hidden">
                  <img src="/image/hero-background.jpg" class="w-full h-full object-cover hover:scale-110 transition-transform duration-1200 elegant-transition" loading="lazy" decoding="async">
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 區塊3: iHome 5.0 工法導入（保留深色）-->
      <section class="pb-32 md:pb-48 bg-warm-white">
        <div class="container-custom">
          <div class="grain-dark relative overflow-hidden rounded-[2.5rem] md:rounded-[3.5rem] bg-[#0a2e26] p-12 md:p-24 animate-fade-in-up">
            <span class="absolute top-0 right-0 p-8 md:p-16 text-white/5 text-[10rem] md:text-[15rem] font-serif pointer-events-none select-none leading-none">iH</span>
            <div class="relative z-10 space-y-12">
              <div class="space-y-6 max-w-xl">
                <span class="font-mono text-[10px] font-bold uppercase tracking-[0.5em] text-emerald-brand-light">Methodology Integration</span>
                <h3 class="font-serif text-4xl md:text-5xl font-light italic text-emerald-50/90 leading-tight tracking-zh">
                  深植於建築基因中的
                  <br />iHome 5.0 智慧工法。
                </h3>
              </div>
              <div class="flex flex-wrap gap-3 pt-12 border-t border-white/10">
                <NuxtLink
                  v-for="t in project.technologies"
                  :key="t"
                  :to="`/portfolio?cat=All`"
                  class="px-6 py-2.5 bg-white/5 ring-1 ring-white/10 rounded-full font-mono text-[11px] tracking-wider text-emerald-brand-light hover:bg-[#10b981] hover:text-charcoal hover:ring-[#10b981] transition-all duration-500"
                >
                  {{ labelOf(t) }}
                </NuxtLink>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>

    <!-- 找不到專案 -->
    <div v-else class="h-screen flex items-center justify-center bg-warm-white">
      <div class="text-center">
        <h2 class="font-serif text-2xl text-charcoal mb-4">專案資料載入中或不存在</h2>
        <NuxtLink to="/portfolio" class="text-emerald-brand font-mono text-xs uppercase tracking-widest">Return to Portfolio</NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
const route = useRoute()
const { getProject } = useProjects()
const { labelOf } = useIHome()

const project = computed(() => getProject(route.params.id))

useSeoMeta({
  title: computed(() => project.value ? `${project.value.title} - 傑丞建築機構` : '建案詳情 - 傑丞建築機構'),
  description: computed(() => project.value?.description ?? '傑丞建築機構精選建案詳情。'),
  ogTitle: computed(() => project.value?.title ?? '傑丞建築機構'),
  ogDescription: computed(() => project.value?.description ?? ''),
  ogImage: computed(() => project.value ? `https://jeremy0819.github.io/jieceng-web/${project.value.image}` : 'https://jeremy0819.github.io/jieceng-web/image/hero-background.jpg'),
  ogType: 'website',
  twitterCard: 'summary_large_image',
})
</script>

<style scoped>
@keyframes slow-zoom {
  from { transform: scale(1); }
  to   { transform: scale(1.15); }
}
.animate-slow-zoom {
  animation: slow-zoom 30s linear infinite alternate;
}
</style>
