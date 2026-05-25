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
          查看作品集
        </NuxtLink>
      </div>
    </section>

    <!-- 區塊2: 全案管理介紹 (優化高度統一與圖片不裁切) -->
    <section class="section-spacing bg-warm-white">
      <div class="container-custom">
        <div class="flex flex-col items-center mb-24 animate-fade-in-up">
          <span class="font-mono text-emerald-brand text-xs tracking-[0.3em] uppercase mb-4">Core Management</span>
          <h2 class="font-serif text-4xl md:text-5xl font-light tracking-zh text-charcoal mb-6">全案管理介紹</h2>
          <div class="h-[1px] w-24 bg-emerald-brand"></div>
        </div>

        <!-- 作品網格 (使用 flex h-full 統一高度) -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-12 md:gap-8 items-stretch">
          <div
            v-for="project in featuredProjects"
            :key="project.id"
            class="group cursor-pointer flex flex-col h-full"
          >
            <NuxtLink :to="`/project/${project.id}`" class="flex flex-col h-full overflow-hidden bg-white shadow-sm">
              <!-- 圖片容器 (調整為不裁切 object-contain) -->
              <div class="relative h-80 overflow-hidden bg-stone-50 flex items-center justify-center">
                <img
                  :src="project.image"
                  :alt="project.title"
                  class="max-w-full max-h-full object-contain transition-transform duration-1200 elegant-transition group-hover:scale-105"
                >
                <div class="absolute inset-0 bg-emerald-brand/0 group-hover:bg-emerald-brand/5 transition-colors duration-700"></div>
              </div>

              <!-- 文字描述 (flex-grow 確保底部對齊) -->
              <div class="p-8 border-t border-stone-100 flex flex-col flex-grow">
                <h3 class="font-serif text-xl font-medium text-charcoal mb-3">{{ project.title }}</h3>
                <p class="font-sans text-sm text-charcoal/60 leading-relaxed mb-8 flex-grow">
                  {{ project.description }}
                </p>
                <div class="flex items-center text-emerald-brand text-xs font-mono tracking-widest uppercase overflow-hidden mt-auto">
                  <span class="transform translate-x-0 group-hover:translate-x-2 transition-transform duration-500">View Detail</span>
                  <div class="ml-2 w-0 group-hover:w-8 h-[1px] bg-emerald-brand transition-all duration-500"></div>
                </div>
              </div>
            </NuxtLink>
          </div>
        </div>

        <div class="mt-24 text-center">
          <NuxtLink
            to="/portfolio"
            class="inline-block px-12 py-5 bg-charcoal text-warm-white text-xs tracking-[0.2em] uppercase hover:bg-emerald-brand transition-colors duration-700 elegant-transition"
          >
            查看所有作品
          </NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const { projects } = useProjects()
const featuredProjects = projects.slice(0, 3)
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