<template>
  <div class="bg-warm-white">
    <!-- 區塊1: 首頁 Hero Section -->
    <section class="relative h-[90vh] flex items-center justify-center overflow-hidden bg-charcoal">
      <div class="absolute inset-0 z-0">
        <img
          src="/image/hero-background.jpg"
          alt="傑丞建築首頁背景"
          class="w-full h-full object-cover opacity-60 scale-105 animate-slow-zoom"
        >
        <div class="absolute inset-0 bg-gradient-to-b from-charcoal/20 to-charcoal/60"></div>
      </div>

      <div class="relative z-10 text-center px-6">
        <h1 class="font-serif text-5xl md:text-8xl font-light tracking-zh-wide text-warm-white mb-6 animate-fade-in-up">
          傑丞建築機構
        </h1>
        <p
          class="font-sans text-lg md:text-2xl font-extralight tracking-[0.25em] text-warm-white/90 mb-12 animate-fade-in-up"
          style="animation-delay: 0.3s"
        >
          構築永續未來 · 定義空間美學
        </p>
        <NuxtLink
          to="/portfolio"
          class="inline-block px-10 py-4 border border-warm-white text-warm-white text-sm tracking-widest uppercase hover:bg-warm-white hover:text-charcoal transition-all duration-1200 elegant-transition animate-fade-in-up"
          style="animation-delay: 0.6s"
        >
          查看全案管理案例
        </NuxtLink>
      </div>
    </section>

    <!-- 區塊2: 全案管理案例 (Apple 風格大圖卡) -->
    <section class="section-spacing bg-warm-white">
      <div class="container-custom">
        <!-- 大標題區 -->
        <div class="text-center mb-16 md:mb-24 animate-fade-in-up">
          <span class="font-mono text-emerald-brand text-xs tracking-[0.3em] uppercase mb-5 block">Featured Cases</span>
          <h2 class="font-serif text-5xl md:text-7xl font-light tracking-zh text-charcoal mb-6 leading-tight">
            全案管理案例
          </h2>
          <p class="font-sans text-base md:text-xl font-light text-charcoal/50 max-w-2xl mx-auto tracking-zh leading-relaxed">
            從住宅到商業，每一個案例都是傑丞全案管理與專利工法的具體實踐。
          </p>
        </div>

        <!-- 大圖卡網格 (2 欄、圓角、滿版照片、漸層字幕) -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8">
          <NuxtLink
            v-for="(project, index) in featuredProjects"
            :key="project.id"
            :to="`/project/${project.id}`"
            class="group relative block overflow-hidden rounded-3xl bg-charcoal aspect-[4/3] animate-fade-in-up shadow-sm"
            :style="`animation-delay: ${0.1 + index * 0.1}s`"
          >
            <img
              :src="project.image"
              :alt="project.title"
              class="absolute inset-0 w-full h-full object-cover transition-transform duration-1200 elegant-transition group-hover:scale-105"
            >
            <!-- 底部漸層遮罩 -->
            <div class="absolute inset-0 bg-gradient-to-t from-charcoal/85 via-charcoal/20 to-transparent"></div>

            <!-- 分類標籤 -->
            <div class="absolute top-7 left-7">
              <span class="font-mono text-[11px] tracking-[0.2em] uppercase text-warm-white/70">
                {{ categoryLabel(project.category) }}
              </span>
            </div>

            <!-- 文字內容 -->
            <div class="absolute bottom-0 left-0 right-0 p-8 md:p-10">
              <h3 class="font-serif text-3xl md:text-4xl font-light text-warm-white mb-3 tracking-zh">
                {{ project.title }}
              </h3>
              <p class="font-sans text-sm md:text-base text-warm-white/70 leading-relaxed max-w-md mb-5 line-clamp-2">
                {{ project.description }}
              </p>
              <span class="inline-flex items-center gap-2 text-warm-white text-xs tracking-[0.15em] uppercase">
                了解更多
                <span class="transition-transform duration-500 group-hover:translate-x-1.5">→</span>
              </span>
            </div>
          </NuxtLink>
        </div>

        <div class="mt-16 md:mt-24 text-center">
          <NuxtLink
            to="/portfolio"
            class="inline-flex items-center gap-3 px-12 py-5 bg-charcoal text-warm-white text-xs tracking-[0.2em] uppercase rounded-full hover:bg-emerald-brand transition-colors duration-700 elegant-transition"
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

<style scoped>
.elegant-transition {
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes slow-zoom {
  from { transform: scale(1); }
  to { transform: scale(1.1); }
}

.animate-slow-zoom {
  animation: slow-zoom 20s linear infinite alternate;
}

.animate-fade-in-up {
  opacity: 0;
  animation: fade-in-up 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>