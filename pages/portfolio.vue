<template>
  <div class="bg-warm-white min-h-screen">
    <!-- 區塊1: 頁面標頭 -->
    <section class="pt-40 md:pt-48 pb-12">
      <div class="container-custom">
        <div class="max-w-4xl mb-16">
          <div class="flex items-center gap-4 mb-9 animate-fade-in-up">
            <span class="w-12 h-px bg-emerald-brand"></span>
            <span class="font-mono text-[10px] uppercase tracking-[0.45em] text-emerald-brand">Architectural Selection</span>
          </div>
          <h1 class="font-serif text-6xl md:text-8xl font-light leading-none tracking-tight text-charcoal animate-fade-in-up" style="animation-delay: 0.1s">
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
              'px-5 md:px-7 py-2.5 rounded-full text-sm tracking-zh transition-all duration-500 elegant-transition border',
              currentTech === cat.key
                ? 'bg-charcoal text-warm-white border-charcoal'
                : 'bg-transparent text-charcoal/50 border-charcoal/15 hover:border-charcoal/40 hover:text-charcoal'
            ]"
          >
            {{ cat.label }}
          </button>
        </div>
      </div>
    </section>

    <!-- 區塊2: 作品網格 -->
    <section class="pb-32 md:pb-48 overflow-hidden">
      <div class="container-custom">
        <TransitionGroup
          name="list"
          tag="div"
          class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-20"
        >
          <NuxtLink
            v-for="(project, index) in filteredProjects"
            :key="project.id"
            :to="`/project/${project.id}`"
            :class="['group block', index % 2 !== 0 ? 'md:mt-24' : '']"
          >
            <div class="relative aspect-[4/5] overflow-hidden rounded-2xl bg-stone-100 mb-8">
              <img
                :src="project.image"
                :alt="project.title"
                class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-1200 elegant-transition group-hover:scale-105"
                loading="lazy" decoding="async"
              >
              <!-- 漸層 + 探索提示 -->
              <div class="absolute inset-0 bg-gradient-to-t from-charcoal/70 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 flex items-end p-8">
                <span class="inline-flex items-center gap-2 text-warm-white text-xs tracking-[0.2em] uppercase translate-y-3 group-hover:translate-y-0 transition-transform duration-500">
                  探索細節
                  <span class="transition-transform duration-500 group-hover:translate-x-1.5">→</span>
                </span>
              </div>
              <!-- 年份 -->
              <div class="absolute top-6 right-6">
                <span class="font-mono text-[10px] tracking-widest text-warm-white/80 bg-charcoal/30 backdrop-blur-sm px-3 py-1.5 rounded-full">
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
                <!-- 五大宅標籤 -->
                <div class="flex flex-wrap gap-2 mt-5">
                  <span
                    v-for="t in project.technologies"
                    :key="t"
                    class="font-mono text-[10px] tracking-wider px-2.5 py-1 rounded-full bg-emerald-brand/8 text-emerald-brand border border-emerald-brand/15"
                  >
                    {{ labelOf(t) }}
                  </span>
                </div>
              </div>
            </div>
          </NuxtLink>
        </TransitionGroup>

        <!-- 無符合結果 -->
        <p v-if="!filteredProjects.length" class="text-center font-sans text-charcoal/40 tracking-zh py-24">
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

useHead({ title: '建築精選集 - 傑丞建築機構' })
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
</style>
