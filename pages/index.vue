<template>
  <div class="bg-warm-white">
    <!-- 區塊1: 首頁 Hero Section -->
    <section class="grain-dark relative h-[95vh] flex items-end overflow-hidden bg-charcoal">
      <div class="absolute inset-0 z-0">
        <img
          src="/image/hero-background.jpg"
          alt="傑丞建築首頁背景"
          class="w-full h-full object-cover opacity-55 scale-105 animate-slow-zoom"
          loading="eager" fetchpriority="high" decoding="async"
        >
        <div class="absolute inset-0 bg-gradient-to-t from-charcoal/90 via-charcoal/30 to-charcoal/10"></div>
      </div>

      <div class="relative z-10 w-full pb-20 md:pb-28">
        <div class="container-custom">
          <p class="font-mono text-[10px] tracking-[0.45em] text-warm-white/50 uppercase mb-8 animate-fade-in-up" style="animation-delay: 0.1s">
            Sustainable Architecture · Centennial Heritage
          </p>
          <h1 class="font-serif text-5xl sm:text-7xl md:text-9xl font-light tracking-tight text-warm-white mb-7 animate-fade-in-up">
            傑丞建築機構
          </h1>
          <div class="flex flex-col sm:flex-row sm:items-center gap-7 sm:gap-12 animate-fade-in-up" style="animation-delay: 0.3s">
            <p class="font-sans text-base font-light tracking-[0.25em] text-warm-white/55">
              永續建築 · 傳承百年
            </p>
            <NuxtLink
              to="/portfolio"
              class="self-start inline-block px-8 py-3.5 ring-1 ring-warm-white/35 text-warm-white text-xs tracking-widest uppercase rounded-full hover:bg-warm-white hover:text-charcoal transition-all duration-700 elegant-transition"
            >
              探索建築誌
            </NuxtLink>
          </div>
        </div>
      </div>

      <div class="absolute bottom-10 right-8 md:right-14 flex flex-col items-center gap-3 z-10 animate-fade-in-up" style="animation-delay: 1.4s">
        <span class="font-mono text-[9px] tracking-[0.4em] text-warm-white/35 uppercase">Scroll</span>
        <div class="relative w-px h-12 overflow-hidden">
          <div class="absolute left-0 w-full bg-warm-white/50 animate-scroll-bar" style="height: 40%"></div>
        </div>
      </div>
    </section>

    <!-- 區塊2: 品牌策略 -->
    <section class="section-spacing bg-white overflow-hidden">
      <div class="container-custom">
        <div class="grid lg:grid-cols-12 gap-16 lg:gap-24 items-center">
          <div class="lg:col-span-5">
            <h2 class="font-mono text-[10px] uppercase tracking-[0.5em] text-emerald-brand mb-9 flex items-center animate-fade-in-up">
              <span class="w-8 h-px bg-emerald-brand mr-4"></span>
              Creative Strategy
            </h2>
            <p class="font-serif text-4xl md:text-5xl font-light text-charcoal leading-tight mb-10 tracking-zh animate-fade-in-up" style="animation-delay: 0.1s">
              我們不只是建造物理結構，更是在策劃一種<span class="italic text-emerald-brand">永續的生活藍圖。</span>
            </p>
            <div class="space-y-6 font-sans text-lg text-charcoal/55 font-light leading-relaxed tracking-zh animate-fade-in-up" style="animation-delay: 0.2s">
              <p>傑丞建築機構深耕桃園與雙北逾二十載，我們將「iHome 5.0」專利工法定義為品牌的技術脊樑。</p>
              <p>對我們而言，美學不應是奢侈的堆砌，而是基於物理性能的自然延伸。</p>
            </div>
          </div>
          <div class="lg:col-span-7">
            <div class="aspect-[4/5] md:aspect-[16/11] rounded-3xl overflow-hidden bg-stone-100 shadow-2xl ring-1 ring-black/[0.07] group animate-fade-in-up" style="animation-delay: 0.15s">
              <img
                src="/image/project-3.jpg"
                alt="傑丞設計細節"
                class="w-full h-full object-cover transition-transform duration-1200 elegant-transition group-hover:scale-105"
                loading="lazy" decoding="async"
              >
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊3: iHome 5.0 互動式展示（蘋果式分頁切換）-->
    <section class="section-spacing bg-warm-white vw-sep">
      <div class="container-custom">
        <div class="mb-14 md:mb-20 animate-fade-in-up">
          <span class="font-mono text-emerald-brand text-xs tracking-[0.35em] uppercase mb-6 block">The Method</span>
          <div class="flex flex-col lg:flex-row lg:items-baseline gap-4 lg:gap-10">
            <h2 class="font-serif text-5xl md:text-6xl font-light tracking-tight text-charcoal shrink-0 leading-tight">
              iHome 5.0 五大宅
            </h2>
            <p class="font-sans text-base md:text-lg font-light text-charcoal/40 max-w-[38ch] leading-relaxed tracking-zh">
              點選標籤，探索定義傑丞建築的五大工法核心。
            </p>
          </div>
        </div>

        <!-- 分段標籤 -->
        <div class="flex flex-wrap justify-center gap-2 md:gap-3 mb-12 animate-fade-in-up" style="animation-delay: 0.1s">
          <button
            v-for="t in iHomeTech"
            :key="t.key"
            @click="activeKey = t.key"
            :class="[
              'px-6 md:px-8 py-3 rounded-full text-sm tracking-zh transition-all duration-500 elegant-transition ring-1',
              activeKey === t.key
                ? 'bg-charcoal text-warm-white ring-charcoal'
                : 'bg-transparent text-charcoal/50 ring-charcoal/15 hover:ring-charcoal/40 hover:text-charcoal'
            ]"
          >
            <span class="font-mono text-[10px] mr-2 opacity-50">{{ t.num }}</span>{{ t.title }}
          </button>
        </div>

        <!-- 內容面板 -->
        <div class="relative rounded-[2.5rem] overflow-hidden bg-charcoal min-h-[460px] md:min-h-[520px] animate-fade-in-up" style="animation-delay: 0.15s">
          <Transition name="ihome-fade" mode="out-in">
            <div :key="active.key" class="grid md:grid-cols-2">
              <!-- 圖片 -->
              <div class="relative h-64 md:h-[520px] overflow-hidden">
                <img :src="active.image" :alt="active.title" class="w-full h-full object-cover" loading="lazy" decoding="async">
                <div class="absolute inset-0 bg-gradient-to-r from-charcoal/10 to-charcoal/60 md:bg-gradient-to-r md:from-transparent md:to-charcoal/70"></div>
              </div>
              <!-- 文字 -->
              <div class="p-9 md:p-16 flex flex-col justify-center">
                <span class="font-mono text-5xl text-warm-white/15 mb-6 block">{{ active.num }}</span>
                <h3 class="font-serif text-4xl md:text-5xl font-light text-warm-white mb-2 tracking-zh">
                  {{ active.title }}
                </h3>
                <p class="font-mono text-[11px] uppercase tracking-[0.3em] text-emerald-brand-light mb-7">{{ active.subtitle }}</p>
                <p class="font-sans text-warm-white/65 font-light leading-relaxed mb-9 tracking-zh">{{ active.desc }}</p>
                <div class="space-y-5 border-t border-warm-white/10 pt-7">
                  <div v-for="d in active.details" :key="d.label">
                    <h4 class="font-mono text-[10px] uppercase tracking-[0.2em] text-warm-white/40 mb-1.5">{{ d.label }}</h4>
                    <p class="font-sans text-sm text-warm-white/70 font-light leading-relaxed tracking-zh">{{ d.value }}</p>
                  </div>
                </div>
              </div>
            </div>
          </Transition>
        </div>

        <div class="mt-12 text-center animate-fade-in-up">
          <NuxtLink
            to="/ihome"
            class="inline-flex items-center gap-3 px-10 py-4 ring-1 ring-charcoal/20 text-charcoal text-xs tracking-[0.2em] uppercase rounded-full hover:bg-charcoal hover:text-warm-white hover:ring-charcoal transition-all duration-700 elegant-transition"
          >
            深入了解 iHome 5.0
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- 區塊4: 精選建築誌（交錯網格）-->
    <section class="section-spacing bg-white vw-sep">
      <div class="container-custom">
        <div class="flex flex-col md:flex-row justify-between items-start md:items-end mb-16 md:mb-24 gap-8">
          <h2 class="font-serif text-5xl md:text-7xl font-light leading-none tracking-tight text-charcoal animate-fade-in-up">
            精選
            <br />
            <span class="italic text-charcoal/25">建築誌。</span>
          </h2>
          <NuxtLink
            to="/portfolio"
            class="px-10 py-4 ring-1 ring-charcoal/20 rounded-full font-mono text-[10px] font-bold uppercase tracking-widest text-charcoal hover:bg-charcoal hover:text-warm-white hover:ring-charcoal transition-all duration-700 elegant-transition animate-fade-in-up"
          >
            探索所有案例
          </NuxtLink>
        </div>

        <div class="grid md:grid-cols-2 gap-12 lg:gap-24">
          <NuxtLink
            v-for="(project, index) in projects"
            :key="project.id"
            :to="`/project/${project.id}`"
            :class="['group block animate-fade-in-up', index % 2 !== 0 ? 'md:mt-32' : '']"
            :style="`animation-delay: ${0.1 + index * 0.12}s`"
          >
            <div class="aspect-[3/4] rounded-2xl overflow-hidden bg-stone-100 mb-9 transition-shadow duration-700 group-hover:shadow-2xl">
              <img
                :src="project.image"
                :alt="project.title"
                class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-1200 elegant-transition group-hover:scale-105"
                loading="lazy" decoding="async"
              >
            </div>
            <div class="flex justify-between items-start border-t border-stone-200 pt-7">
              <div>
                <span class="font-mono text-[10px] text-emerald-brand font-bold uppercase tracking-widest mb-2 block">Featured Case</span>
                <h3 class="font-serif text-3xl font-light text-charcoal group-hover:text-emerald-brand transition-colors duration-500 tracking-zh">
                  {{ project.title }}
                </h3>
              </div>
              <span class="font-sans text-sm font-light text-charcoal/40">{{ project.year }}</span>
            </div>
          </NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const { projects } = useProjects()
const { iHomeTech } = useIHome()

const activeKey = ref(iHomeTech[0].key)
const active = computed(() => iHomeTech.find((t) => t.key === activeKey.value) ?? iHomeTech[0])

useSeoMeta({
  title: '傑丞建築機構 | 構築永續未來，定義空間美學',
  description: '傑丞建築機構深耕桃園與雙北逾二十載，以 iHome 5.0 專利工法打造百年宅、健康宅、節能宅、智慧宅、履歷宅，提供都更全案管理與永續建築設計。',
  ogTitle: '傑丞建築機構 | 構築永續未來，定義空間美學',
  ogDescription: '以 iHome 5.0 專利工法打造永續建築精品，全案管理一條龍服務。',
  ogImage: 'https://jeremy0819.github.io/jieceng-web/image/hero-background.jpg',
  ogType: 'website',
  twitterCard: 'summary_large_image',
  twitterTitle: '傑丞建築機構 | 永續建築美學',
  twitterDescription: '以 iHome 5.0 專利工法打造永續建築精品。',
})
</script>

<style scoped>
/* iHome 互動面板切換動畫 */
.ihome-fade-enter-active,
.ihome-fade-leave-active {
  transition: opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}
.ihome-fade-enter-from,
.ihome-fade-leave-to {
  opacity: 0;
}
</style>
