<template>
  <div class="bg-warm-white min-h-screen">
    <!-- 區塊1: 頁面標頭 -->
    <section class="pt-24 pb-12">
      <div class="container-custom">
        <div class="text-center">
          <span class="font-mono text-emerald-brand text-xs tracking-[0.3em] uppercase mb-4 block animate-fade-in-up">
            PCM Cases
          </span>
          <h1 class="font-serif text-5xl md:text-6xl font-light text-charcoal mb-8 animate-fade-in-up">
            全案管理案例
          </h1>
          <div class="h-[1px] w-24 bg-emerald-brand mx-auto mb-16 animate-fade-in-up"></div>

          <!-- 分類過濾 (極簡導航) -->
          <div class="flex flex-wrap justify-center gap-8 md:gap-12 animate-fade-in-up" style="animation-delay: 0.2s">
            <button
              v-for="category in categories"
              :key="category.key"
              @click="currentCategory = category.key"
              :class="[
                'font-sans text-xs tracking-[0.2em] uppercase transition-all duration-500 relative pb-2 tracking-zh',
                currentCategory === category.key ? 'text-charcoal' : 'text-charcoal/40 hover:text-charcoal'
              ]"
            >
              {{ category.label }}
              <span
                v-if="currentCategory === category.key"
                class="absolute bottom-0 left-0 w-full h-[1px] bg-emerald-brand animate-expand-width"
              ></span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊2: 作品網格系統 -->
    <section class="pb-32 md:pb-48 overflow-hidden">
      <div class="container-custom">
        <!-- 使用 TransitionGroup 並指定 tag="div" 以及 grid 樣式 -->
        <TransitionGroup
          name="list"
          tag="div"
          class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-8 gap-y-16"
        >
          <div
            v-for="(project, index) in filteredProjects"
            :key="project.id"
            class="group"
          >
            <NuxtLink :to="`/project/${project.id}`" class="block">
              <!-- 圖片容器：高級感縮放與濾鏡 -->
              <div class="relative aspect-[3/4] overflow-hidden bg-stone-100 mb-6">
                <img
                  :src="project.image"
                  :alt="project.title"
                  class="w-full h-full object-cover transition-transform duration-1200 elegant-transition group-hover:scale-110"
                >
                <!-- 翡翠綠懸停遮罩 -->
                <div class="absolute inset-0 bg-emerald-brand/0 group-hover:bg-emerald-brand/10 transition-colors duration-700"></div>

                <!-- 專案類型標籤 (Mono 字體) -->
                <div class="absolute top-6 left-6 overflow-hidden">
                  <span class="inline-block bg-warm-white/90 backdrop-blur-sm px-3 py-1 text-[10px] font-mono tracking-tighter text-charcoal transform -translate-y-full group-hover:translate-y-0 transition-transform duration-500">
                    {{ project.category }}
                  </span>
                </div>
              </div>

              <!-- 資訊區 -->
              <div class="px-2">
                <div class="flex justify-between items-baseline mb-3">
                  <h3 class="font-serif text-2xl font-light text-charcoal group-hover:text-emerald-brand transition-colors duration-500">
                    {{ project.title }}
                  </h3>
                  <span class="font-mono text-[10px] text-charcoal/30 italic">0{{ index + 1 }}</span>
                </div>
                <p class="font-sans text-sm text-charcoal/50 leading-relaxed line-clamp-2">
                  {{ project.description }}
                </p>
              </div>
            </NuxtLink>
          </div>
        </TransitionGroup>
      </div>
    </section>
  </div>
</template>

<script setup>
const { projects } = useProjects()
const route = useRoute()

const categories = [
  { key: 'All', label: '全部' },
  { key: 'Residential', label: '住宅' },
  { key: 'Commercial', label: '商業' },
  { key: 'Landscape', label: '景觀' },
  { key: 'Renovation', label: '改造' }
]

const currentCategory = ref('All')

// 從網址 ?category= 帶入篩選（導覽列下拉選單會用到）
const applyQuery = () => {
  const q = route.query.category
  const match = categories.find((c) => c.key === q)
  currentCategory.value = match ? match.key : 'All'
}
applyQuery()
watch(() => route.query.category, applyQuery)

const filteredProjects = computed(() => {
  if (currentCategory.value === 'All') return projects
  return projects.filter(p => p.category === currentCategory.value)
})
</script>

<style scoped>
.elegant-transition {
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}

/* 基礎載入動畫 */
.animate-fade-in-up {
  opacity: 0;
  animation: fade-in-up 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes expand-width {
  from { width: 0; }
  to { width: 100%; }
}

.animate-expand-width {
  animation: expand-width 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

/* --- 修正後的 TransitionGroup 動態樣式 --- */

/* 1. 進入與離開過程的過渡設定 */
.list-enter-active,
.list-leave-active {
  transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

/* 2. 移動過程中的平滑動畫 (這是修正卡頓的關鍵) */
.list-move {
  transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

/* 3. 進入與離開的狀態 */
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(30px) scale(0.98);
}

/* 4. 離開時必須脫離文件流，讓其他元素能順利 move */
.list-leave-active {
  position: absolute;
  /* 寬度需要維持，避免縮小 */
  width: 100%;
  max-width: calc((100% / 3) - 21.3px); /* 針對 lg 3 欄計算，確保佈局不崩潰 */
}

/* 針對行動版與平板調整離開時的寬度 */
@media (max-width: 1024px) {
  .list-leave-active {
    max-width: calc((100% / 2) - 16px);
  }
}
@media (max-width: 768px) {
  .list-leave-active {
    max-width: calc(100% - 48px);
  }
}
</style>