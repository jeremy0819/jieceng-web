<template>
  <div class="bg-warm-white">
    <!-- 區塊1: 首頁 Hero Section -->
    <section class="grain-dark relative h-[95vh] flex items-center justify-center overflow-hidden bg-charcoal">
      <!-- 背景圖 + 漸層 -->
      <div class="absolute inset-0 z-0">
        <img
          src="/image/hero-background.jpg"
          alt="傑丞建築首頁背景"
          class="w-full h-full object-cover opacity-55 scale-105 animate-slow-zoom"
        >
        <div class="absolute inset-0 bg-gradient-to-b from-charcoal/30 via-transparent to-charcoal/70"></div>
      </div>

      <!-- 主文字 -->
      <div class="relative z-10 text-center px-6">
        <!-- 小標眉 -->
        <p
          class="font-mono text-[10px] tracking-[0.45em] text-warm-white/50 uppercase mb-8 animate-fade-in-up"
          style="animation-delay: 0.1s"
        >
          Architecture · Construction · Heritage
        </p>

        <h1 class="font-serif text-6xl md:text-9xl font-light tracking-zh-wide text-warm-white mb-8 animate-fade-in-up">
          傑丞建築機構
        </h1>
        <p
          class="font-sans text-base md:text-xl font-extralight tracking-[0.3em] text-warm-white/75 mb-14 animate-fade-in-up"
          style="animation-delay: 0.3s"
        >
          構築永續未來 · 定義空間美學
        </p>
        <NuxtLink
          to="/portfolio"
          class="inline-block px-10 py-4 border border-warm-white/70 text-warm-white text-xs tracking-widest uppercase hover:bg-warm-white hover:text-charcoal transition-all duration-700 elegant-transition animate-fade-in-up"
          style="animation-delay: 0.6s"
        >
          查看全案管理案例
        </NuxtLink>
      </div>

      <!-- 向下捲動指示 -->
      <div
        class="absolute bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center gap-3 z-10 animate-fade-in-up"
        style="animation-delay: 1.4s"
      >
        <span class="font-mono text-[9px] tracking-[0.4em] text-warm-white/35 uppercase">Scroll</span>
        <div class="relative w-px h-12 overflow-hidden">
          <div class="absolute left-0 w-full bg-warm-white/50 animate-scroll-bar" style="height: 40%"></div>
        </div>
      </div>
    </section>

    <!-- 區塊2: 全案管理案例 (Apple 風格大圖卡) -->
    <section class="section-spacing bg-warm-white">
      <div class="container-custom">
        <!-- 大標題區 -->
        <div class="text-center mb-16 md:mb-24 animate-fade-in-up">
          <span class="font-mono text-emerald-brand text-xs tracking-[0.35em] uppercase mb-5 block">Featured Cases</span>
          <h2 class="font-serif text-5xl md:text-7xl font-light tracking-zh text-charcoal mb-6 leading-tight">
            全案管理案例
          </h2>
          <p class="font-sans text-base md:text-lg font-light text-charcoal/45 max-w-xl mx-auto tracking-zh leading-relaxed">
            從住宅到商業，每一個案例都是傑丞全案管理與專利工法的具體實踐。
          </p>
        </div>

        <!-- 大圖卡網格：上方 2 欄橫向、下方 2 欄橫向 -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-5 md:gap-6">
          <NuxtLink
            v-for="(project, index) in featuredProjects"
            :key="project.id"
            :to="`/project/${project.id}`"
            class="group relative block overflow-hidden rounded-2xl bg-charcoal aspect-[4/3] animate-fade-in-up shadow-sm"
            :style="`animation-delay: ${0.1 + index * 0.12}s`"
          >
            <img
              :src="project.image"
              :alt="project.title"
              class="absolute inset-0 w-full h-full object-cover transition-transform duration-1200 elegant-transition group-hover:scale-[1.06]"
            >
            <!-- 底部漸層遮罩 -->
            <div class="absolute inset-0 bg-gradient-to-t from-charcoal/90 via-charcoal/25 to-transparent"></div>

            <!-- 分類標籤 -->
            <div class="absolute top-6 left-6">
              <span class="font-mono text-[10px] tracking-[0.25em] uppercase text-warm-white/60 bg-charcoal/30 backdrop-blur-sm px-2.5 py-1 rounded-sm">
                {{ categoryLabel(project.category) }}
              </span>
            </div>

            <!-- 文字內容 -->
            <div class="absolute bottom-0 left-0 right-0 p-7 md:p-9">
              <h3 class="font-serif text-2xl md:text-3xl font-light text-warm-white mb-2.5 tracking-zh">
                {{ project.title }}
              </h3>
              <p class="font-sans text-sm text-warm-white/60 leading-relaxed max-w-xs mb-4 line-clamp-2">
                {{ project.description }}
              </p>
              <span class="inline-flex items-center gap-2 text-warm-white/80 text-[11px] tracking-[0.2em] uppercase group-hover:text-warm-white transition-colors duration-500">
                了解更多
                <span class="transition-transform duration-500 group-hover:translate-x-2">→</span>
              </span>
            </div>
          </NuxtLink>
        </div>

        <div class="mt-14 md:mt-20 text-center">
          <NuxtLink
            to="/portfolio"
            class="inline-flex items-center gap-3 px-10 py-4 border border-charcoal/20 text-charcoal text-xs tracking-[0.2em] uppercase rounded-full hover:bg-charcoal hover:text-warm-white transition-all duration-700 elegant-transition"
          >
            查看全部案例
          </NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const { projects } = useProjects()
const featuredProjects = projects.slice(0, 4)

const categoryLabels = {
  Residential: '住宅',
  Commercial: '商業',
  Landscape: '景觀',
  Renovation: '改造'
}
const categoryLabel = (key) => categoryLabels[key] ?? key
</script>
