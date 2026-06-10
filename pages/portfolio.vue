<template>
  <div class="bg-[#050505] min-h-screen">
    <!-- 區塊1: 頁面標頭 -->
    <section class="pt-32 md:pt-40 pb-12 bg-[#050505]">
      <div class="container-custom">
        <div class="max-w-4xl mb-16">
          <div class="flex items-center gap-4 mb-9 animate-fade-in-up">
            <span class="w-12 h-px bg-[#10b981]"></span>
            <span class="font-mono text-[10px] uppercase tracking-[0.45em] text-[#10b981]">Architectural Selection</span>
          </div>
          <h1 class="font-serif text-6xl md:text-8xl font-light leading-none tracking-tight text-white animate-fade-in-up" style="animation-delay: 0.1s">
            建築精選集。
          </h1>
        </div>

        <!-- 以 iHome 五大宅篩選 -->
        <div class="flex flex-wrap gap-2 md:gap-3 animate-fade-in-up" style="animation-delay: 0.2s">
          <button
            v-for="cat in filters"
            :key="cat.key"
            @click="currentTech = cat.key"
            :class="[
              'px-5 md:px-7 py-2.5 rounded-full text-sm tracking-zh transition-all duration-500 elegant-transition ring-1',
              currentTech === cat.key
                ? 'bg-[#10b981] text-[#050505] ring-[#10b981]'
                : 'glass text-white/50 ring-white/15 hover:ring-white/40 hover:text-white'
            ]"
          >
            {{ cat.label }}
          </button>
        </div>
      </div>
    </section>

    <!-- 區塊2: 作品網格 -->
    <section class="pb-32 md:pb-48 overflow-hidden bg-[#050505]">
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
            <div class="relative aspect-[4/5] overflow-hidden rounded-3xl bg-white/[0.06] mb-8">
              <img
                :src="project.image"
                :alt="project.title"
                class="w-full h-full object-cover opacity-75 group-hover:opacity-100 transition-all duration-1200 elegant-transition group-hover:scale-105"
                loading="lazy" decoding="async"
              >
              <!-- 漸層 + 探索提示 -->
              <div class="absolute inset-0 bg-gradient-to-t from-[#050505]/70 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 flex items-end p-8">
                <span class="inline-flex items-center gap-2 text-[#10b981] text-xs tracking-[0.2em] uppercase translate-y-3 group-hover:translate-y-0 transition-transform duration-500">
                  探索細節
                  <span class="transition-transform duration-500 group-hover:translate-x-1.5">→</span>
                </span>
              </div>
              <!-- 年份 -->
              <div class="absolute top-6 right-6">
                <span class="font-mono text-[10px] tracking-widest text-white/80 bg-[#050505]/30 backdrop-blur-sm px-3 py-1.5 rounded-full">
                  {{ project.year }}
                </span>
              </div>
            </div>

            <div class="flex justify-between items-start border-t border-white/[0.10] pt-7">
              <div class="flex-1">
                <span class="font-mono text-[10px] text-[#10b981] font-bold uppercase tracking-widest mb-2 block">{{ project.categoryLabel }}</span>
                <h2 class="font-serif text-3xl font-light text-white group-hover:text-[#10b981] transition-colors duration-500 tracking-zh mb-3">
                  {{ project.title }}
                </h2>
                <p class="font-sans text-sm text-white/50 leading-relaxed line-clamp-2 max-w-md">
                  {{ project.description }}
                </p>
                <!-- 五大宅標籤 -->
                <div class="flex flex-wrap gap-2 mt-5">
                  <span
                    v-for="t in project.technologies"
                    :key="t"
                    class="font-mono text-[10px] tracking-wider px-2.5 py-1 rounded-full bg-[#10b981]/10 text-[#10b981] border border-[#10b981]/20"
                  >
                    {{ labelOf(t) }}
                  </span>
                </div>
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
              <div class="absolute inset-0 bg-[#050505]/70 backdrop-blur-sm" @click="quickView = null"></div>
              <div class="qv-panel relative w-full md:max-w-[500px] h-full glass-card overflow-y-auto flex flex-col">
                <!-- 建案圖片 -->
                <div class="relative aspect-[16/10] overflow-hidden shrink-0 bg-white/[0.06]">
                  <img
                    :src="quickView.image"
                    :alt="quickView.title"
                    class="w-full h-full object-cover"
                    loading="lazy"
                    decoding="async"
                  >
                  <button
                    @click="quickView = null"
                    class="absolute top-4 right-4 glass w-9 h-9 text-white flex items-center justify-center rounded-full hover:bg-white/20 transition-colors duration-300 font-sans text-sm"
                    aria-label="關閉"
                  >
                    ✕
                  </button>
                </div>

                <!-- 內容 -->
                <div class="p-8 flex-1 space-y-7">
                  <div>
                    <span class="font-mono text-[10px] text-[#10b981] uppercase tracking-widest block mb-2">
                      {{ quickView.categoryLabel }} · {{ quickView.year }}
                    </span>
                    <h2 class="font-serif text-3xl font-light text-white tracking-zh">
                      {{ quickView.title }}
                    </h2>
                  </div>
                  <p class="font-sans text-white/60 leading-relaxed tracking-zh text-sm">
                    {{ quickView.fullDescription }}
                  </p>
                  <!-- 前兩個亮點 -->
                  <div class="space-y-3 border-t border-white/[0.08] pt-6">
                    <p class="font-mono text-[10px] uppercase tracking-[0.3em] text-white/35">Highlights</p>
                    <ul class="space-y-3">
                      <li
                        v-for="h in quickView.highlights.slice(0, 2)"
                        :key="h"
                        class="flex gap-3 text-sm text-white/65 font-light tracking-zh leading-relaxed"
                      >
                        <span class="text-[#10b981] shrink-0 mt-0.5 font-sans">—</span>
                        {{ h }}
                      </li>
                    </ul>
                  </div>
                  <!-- 五大宅工法標籤 -->
                  <div class="flex flex-wrap gap-2">
                    <span
                      v-for="t in quickView.technologies"
                      :key="t"
                      class="font-mono text-[10px] px-3 py-1 rounded-full bg-[#10b981]/10 text-[#10b981] ring-1 ring-[#10b981]/20 tracking-wider"
                    >
                      {{ labelOf(t) }}
                    </span>
                  </div>
                </div>

                <!-- CTA：前往完整建案頁 -->
                <div class="p-8 border-t border-white/[0.08] shrink-0">
                  <NuxtLink
                    :to="`/project/${quickView.id}`"
                    @click="quickView = null"
                    class="flex items-center justify-between w-full py-5 px-8 bg-[#10b981] text-[#050505] text-xs tracking-[0.2em] uppercase hover:bg-[#0d9668] transition-colors duration-700"
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
        <p v-if="!filteredProjects.length" class="text-center font-sans text-white/40 tracking-zh py-24">
          目前沒有符合此工法的案例，敬請期待。
        </p>
      </div>
    </section>
  </div>
</template>

<script setup>
const { projects, projectsByTech } = useProjects()
const { iHomeTech, labelOf } = useIHome()
const route = useRoute()

const filters = [
  { key: 'All', label: '全部' },
  ...iHomeTech.map((t) => ({ key: t.key, label: t.title }))
]

const currentTech = ref('All')

// 從網址 ?tech= 帶入篩選（導覽列下拉選單會用到）
const applyQuery = () => {
  const q = route.query.tech
  const match = filters.find((f) => f.key === q)
  currentTech.value = match ? match.key : 'All'
}
applyQuery()
watch(() => route.query.tech, applyQuery)

const filteredProjects = computed(() => {
  if (currentTech.value === 'All') return projects
  return projectsByTech(currentTech.value)
})

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
    max-width: calc(100% - 48px);
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
