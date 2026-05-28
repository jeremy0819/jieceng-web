<template>
  <div class="bg-warm-white min-h-screen">
    <div v-if="project">
      <!-- 區塊1: 沉浸式 Hero Section -->
      <section class="relative h-[70vh] overflow-hidden bg-charcoal">
        <img
          :src="project.image"
          :alt="project.title"
          class="w-full h-full object-cover opacity-80 scale-105 animate-slow-zoom"
        >
        <div class="absolute inset-0 bg-gradient-to-t from-charcoal/80 via-transparent to-transparent"></div>

        <!-- 標題懸浮於圖片底部 -->
        <div class="absolute bottom-0 left-0 w-full pb-16">
          <div class="container-custom">
            <span class="font-mono text-emerald-brand-light text-xs tracking-[0.3em] uppercase mb-4 block animate-fade-in-up">
              Selected Project / {{ project.category }}
            </span>
            <h1 class="font-serif text-5xl md:text-7xl text-warm-white font-light animate-fade-in-up" style="animation-delay: 0.2s">
              {{ project.title }}
            </h1>
          </div>
        </div>
      </section>

      <!-- 區塊2: 專案資訊與描述 -->
      <section class="section-spacing">
        <div class="container-custom">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-16">

            <!-- 左側：技術參數 (Architecture Specs) -->
            <div class="lg:col-span-4 space-y-12 animate-fade-in-up" style="animation-delay: 0.4s">
              <div>
                <h3 class="font-mono text-[10px] uppercase tracking-[0.3em] text-emerald-brand mb-6">Technical Data</h3>
                <dl class="space-y-6">
                  <div v-for="(val, key) in project.specs" :key="key" class="border-b border-stone-200 pb-4">
                    <dt class="font-sans text-[10px] text-charcoal/40 uppercase tracking-widest mb-1">{{ key }}</dt>
                    <dd class="font-serif text-lg text-charcoal">{{ val }}</dd>
                  </div>
                </dl>
              </div>

              <!-- 返回按鈕 -->
              <NuxtLink
                to="/portfolio"
                class="group inline-flex items-center text-charcoal/40 hover:text-emerald-brand transition-colors duration-500"
              >
                <svg class="mr-4 w-12 h-4 transform rotate-180 group-hover:-translate-x-3 transition-transform duration-700 elegant-transition" fill="none" stroke="currentColor" viewBox="0 0 48 16">
                  <path d="M0 8H46M46 8L39 1M46 8L39 15" stroke-width="1" />
                </svg>
                <span class="font-mono text-xs uppercase tracking-widest">Back to Portfolio</span>
              </NuxtLink>
            </div>

            <!-- 右側：深度描述 -->
            <div class="lg:col-span-8 animate-fade-in-up" style="animation-delay: 0.6s">
              <h2 class="font-serif text-3xl font-light text-charcoal mb-10">設計思維與工法實踐</h2>
              <div class="prose prose-stone max-w-none">
                <p class="font-sans text-lg text-charcoal/70 leading-relaxed mb-8">
                  {{ project.fullDescription }}
                </p>
                <p class="font-sans text-lg text-charcoal/70 leading-relaxed">
                  在「{{ project.title }}」的實踐中，我們不只是建造一個空間，更是在探討人與環境、技術與美學之間的動態平衡。透過傑丞建築獨有的專利技術，確保了結構的永續性與生活的舒適度。
                </p>
              </div>

              <!-- 專案展示次圖 -->
              <div class="mt-20 grid grid-cols-2 gap-4">
                <div class="aspect-square bg-stone-100 overflow-hidden">
                  <img :src="project.image" class="w-full h-full object-cover hover:scale-110 transition-transform duration-1200 elegant-transition">
                </div>
                <div class="aspect-square bg-stone-100 overflow-hidden">
                  <img src="/image/hero-background.jpg" class="w-full h-full object-cover hover:scale-110 transition-transform duration-1200 elegant-transition">
                </div>
              </div>
            </div>

          </div>
        </div>
      </section>
    </div>

    <!-- 錯誤處理：找不到專案時 -->
    <div v-else class="h-screen flex items-center justify-center">
      <div class="text-center">
        <h2 class="font-serif text-2xl text-charcoal mb-4">專案資料載入中或不存在</h2>
        <NuxtLink to="/portfolio" class="text-emerald-brand font-mono text-xs uppercase tracking-widest">Return Home</NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
const route = useRoute()
const { getProject } = useProjects()

const project = computed(() => getProject(route.params.id))

// SEO 標題設定
useHead({
  title: project.value ? `${project.value.title} - 傑丞建築機構` : '專案詳情 - 傑丞建築機構'
})
</script>

<style scoped>
/* 詳情頁背景縮放比首頁更緩更深：30s / scale 1.15 */
@keyframes slow-zoom {
  from { transform: scale(1); }
  to   { transform: scale(1.15); }
}

.animate-slow-zoom {
  animation: slow-zoom 30s linear infinite alternate;
}
</style>