<template>
  <div class="bg-warm-white min-h-screen">
    <!-- 區塊1: 暗色 Hero -->
    <section class="grain-dark relative h-[45vh] flex items-end overflow-hidden bg-charcoal">
      <div class="absolute inset-0 z-0">
        <img
          src="/image/project-1.jpg"
          alt="傑丞建築精選集"
          class="w-full h-full object-cover opacity-45 animate-slow-zoom"
          loading="eager" fetchpriority="high" decoding="async"
        >
        <div class="absolute inset-0 bg-gradient-to-t from-charcoal/90 via-charcoal/40 to-transparent"></div>
      </div>
      <div class="container-custom relative z-10 pb-14">
        <div class="flex items-center gap-4 mb-5 animate-fade-in-up">
          <span class="glass-dark rounded-full px-4 py-1.5 font-mono text-[10px] text-emerald-brand-light tracking-[0.35em] uppercase">
            Architectural Selection · INDEX
          </span>
        </div>
        <div class="dim-line dim-line-light w-20 mb-5 animate-fade-in-up" style="animation-delay: 0.1s"></div>
        <h1 class="font-serif text-5xl md:text-7xl text-warm-white font-light leading-none tracking-tight animate-fade-in-up" style="animation-delay: 0.15s">
          建築精選集。
        </h1>
      </div>
    </section>

    <!-- 篩選條 -->
    <section class="relative overflow-hidden py-5 bg-warm-white border-b border-stone-100">
      <span class="sheet-num top-2 -right-8" aria-hidden="true">01</span>
      <div class="container-custom relative z-10">
        <div class="flex flex-wrap gap-2 md:gap-3 animate-fade-in-up">
          <button
            v-for="cat in filters"
            :key="cat.key"
            @click="currentCat = cat.key"
            :class="[
              'px-5 md:px-7 py-2.5 rounded-full text-sm tracking-zh transition-all duration-500 elegant-transition ring-1',
              currentCat === cat.key
                ? 'bg-charcoal text-warm-white ring-charcoal ring-1'
                : 'glass ring-1 ring-charcoal/15 text-charcoal/50 hover:ring-charcoal/35 hover:text-charcoal'
            ]"
          >
            {{ cat.label }}
          </button>
        </div>
      </div>
    </section>

    <!-- 區塊2: 作品網格 -->
    <section class="pb-32 md:pb-48 bg-warm-white overflow-hidden">
      <div class="container-custom">
        <TransitionGroup
          name="list"
          tag="div"
          class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-20"
        >
          <div
            v-for="(project, index) in filteredProjects"
            :key="project.id"
            :class="['group block cursor-pointer', index % 2 !== 0 ? 'md:mt-24' : '']"
            @click="quickView = project"
          >
            <div class="img-reveal relative aspect-[16/10] md:aspect-[4/5] overflow-hidden rounded-2xl bg-stone-100 mb-8 shadow-sm ring-1 ring-black/[0.06]">
              <img
                :src="project.image"
                :alt="project.title"
                class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-1200 elegant-transition group-hover:scale-105"
                loading="lazy" decoding="async"
              >
              <!-- 漸層 + 探索提示 -->
              <div class="absolute inset-0 bg-gradient-to-t from-charcoal/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 flex items-end p-8">
                <span class="inline-flex items-center gap-2 text-warm-white text-xs tracking-[0.2em] uppercase translate-y-3 group-hover:translate-y-0 transition-transform duration-500">
                  探索細節
                  <span class="transition-transform duration-500 group-hover:translate-x-1.5">→</span>
                </span>
              </div>
              <!-- 年份 -->
              <div class="absolute top-6 right-6">
                <span class="font-mono text-[10px] tracking-widest text-warm-white/80 bg-black/25 backdrop-blur-sm px-3 py-1.5 rounded-full">
                  {{ project.year }}
                </span>
              </div>
            </div>

            <div class="flex justify-between items-start border-t border-stone-200 pt-7">
              <div class="flex-1">
                <span class="font-mono text-[10px] text-emerald-brand font-bold uppercase tracking-widest mb-2 block">{{ project.categoryLabel }}</span>
                <h2 class="font-serif text-3xl font-light text-charcoal group-hover:text-emerald-brand transition-colors duration-500 tracking-zh mb-3">
                  {{ project.title }}
                </h2>
                <p class="font-sans text-sm text-charcoal/50 leading-relaxed line-clamp-2 max-w-md">
                  {{ project.description }}
                </p>
              </div>
            </div>
          </div>
        </TransitionGroup>

        <!-- Quick-view 抽屜 -->
        <Teleport to="body">
          <Transition name="qv">
            <div
              v-if="quickView"
              class="fixed inset-0 z-[200] flex justify-end"
              @click.self="quickView = null"
            >
              <div class="absolute inset-0 bg-charcoal/40 backdrop-blur-sm" @click="quickView = null"></div>
              <div class="qv-panel relative w-full md:max-w-[480px] h-full glass-card overflow-y-auto flex flex-col">
                <!-- 建案圖片 -->
                <div class="relative aspect-[16/10] overflow-hidden shrink-0 bg-stone-100">
                  <img
                    :src="quickView.image"
                    :alt="quickView.title"
                    class="w-full h-full object-cover"
                    loading="lazy"
                    decoding="async"
                  >
                  <button
                    @click="quickView = null"
                    class="absolute top-4 right-4 glass w-9 h-9 text-charcoal/70 flex items-center justify-center rounded-full hover:text-charcoal transition-colors duration-300 font-sans text-sm"
                    aria-label="關閉"
                  >
                    ✕
                  </button>
                </div>

                <!-- 內容 -->
                <div class="relative corner-marks p-8 flex-1 space-y-7">
                  <div>
                    <span class="font-mono text-[10px] text-emerald-brand uppercase tracking-widest block mb-2">
                      {{ quickView.categoryLabel }} · {{ quickView.year }}
                    </span>
                    <h2 class="font-serif text-3xl font-light text-charcoal tracking-zh">
                      {{ quickView.title }}
                    </h2>
                  </div>
                  <p class="font-sans text-charcoal/60 leading-relaxed tracking-zh text-sm">
                    {{ quickView.fullDescription }}
                  </p>
                  <!-- 前兩個亮點 -->
                  <div class="space-y-3 border-t border-stone-100 pt-6">
                    <p class="font-mono text-[10px] uppercase tracking-[0.3em] text-charcoal/30">Highlights</p>
                    <ul class="space-y-3">
                      <li
                        v-for="h in quickView.highlights.slice(0, 2)"
                        :key="h"
                        class="flex gap-3 text-sm text-charcoal/65 font-light tracking-zh leading-relaxed"
                      >
                        <span class="text-emerald-brand shrink-0 mt-0.5 font-sans">—</span>
                        {{ h }}
                      </li>
                    </ul>
                  </div>
                  <!-- iHome 五大宅工法標籤（detail drawer 中仍顯示） -->
                  <div class="flex flex-wrap gap-2">
                    <span
                      v-for="t in quickView.technologies"
                      :key="t"
                      class="glass font-mono text-[10px] px-3 py-1 rounded-full text-emerald-brand ring-1 ring-emerald-brand/20 tracking-wider"
                    >
                      {{ labelOf(t) }}
                    </span>
                  </div>
                </div>

                <!-- CTA：前往完整建案頁 -->
                <div class="p-8 border-t border-stone-100 shrink-0">
                  <NuxtLink
                    :to="`/project/${quickView.id}`"
                    @click="quickView = null"
                    class="flex items-center justify-between w-full py-5 px-8 bg-charcoal text-warm-white text-xs tracking-[0.2em] uppercase hover:bg-emerald-brand transition-colors duration-700"
                  >
                    查看完整建案詳情
                    <span>→</span>
                  </NuxtLink>
                </div>
              </div>
            </div>
          </Transition>
        </Teleport>

        <!-- 無符合結果 -->
        <p v-if="!filteredProjects.length" class="text-center font-sans text-charcoal/40 tracking-zh py-24">
          目前沒有符合此類別的案例，敬請期待。
        </p>
      </div>
    </section>
  </div>
</template>

<script setup>
const { projects, projectsByCategory } = useProjects()
const { labelOf } = useIHome()
const route = useRoute()

const filters = [
  { key: 'All', label: '全部案例' },
  { key: 'residential', label: '住宅建案' },
  { key: 'renewal', label: '都更案' },
]

const currentCat = ref('All')

// 從網址 ?cat= 帶入篩選
const applyQuery = () => {
  const q = route.query.cat
  const match = filters.find((f) => f.key === q)
  currentCat.value = match ? match.key : 'All'
}
applyQuery()
watch(() => route.query.cat, applyQuery)

const filteredProjects = computed(() => projectsByCategory(currentCat.value))

// Quick-view drawer
const quickView = ref(null)

if (process.client) {
  onMounted(() => {
    const onKey = (e) => { if (e.key === 'Escape') quickView.value = null }
    window.addEventListener('keydown', onKey)
    onUnmounted(() => window.removeEventListener('keydown', onKey))
  })
}

useSeoMeta({
  title: '全案管理案例 - 傑丞建築機構',
  description: '傑丞建築機構精選建案：印象羅芙（2020）、印象天裔（2022），採用 iHome 5.0 百年宅、健康宅、節能宅、智慧宅、履歷宅五大工法建造。',
  ogTitle: '傑丞建築 - 全案管理案例精選',
  ogDescription: '結合 iHome 5.0 工法的精品建案集，永續建築與人文美學的實踐。',
  ogImage: 'https://jeremy0819.github.io/jieceng-web/image/hero-background.jpg',
  ogType: 'website',
  twitterCard: 'summary_large_image',
})
</script>

<style scoped>
/* TransitionGroup 動態樣式 */
.list-enter-active,
.list-leave-active {
  transition: all 0.7s cubic-bezier(0.16, 1, 0.3, 1);
}
.list-move {
  transition: transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(30px) scale(0.98);
}
.list-leave-active {
  position: absolute;
  width: 100%;
  max-width: calc((100% / 2) - 24px);
}
@media (max-width: 768px) {
  .list-leave-active {
    max-width: calc(100% - 40px);
  }
}

/* Quick-view drawer slide-in */
.qv-enter-active,
.qv-leave-active {
  transition: opacity 0.4s ease;
}
.qv-enter-active .qv-panel,
.qv-leave-active .qv-panel {
  transition: transform 0.55s cubic-bezier(0.16, 1, 0.3, 1);
}
.qv-enter-from,
.qv-leave-to {
  opacity: 0;
}
.qv-enter-from .qv-panel,
.qv-leave-to .qv-panel {
  transform: translateX(100%);
}
</style>
