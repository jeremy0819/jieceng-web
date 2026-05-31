<template>
  <header
    :class="[
      'fixed top-0 left-0 right-0 z-50 transition-all duration-700 elegant-transition',
      isScrolled || isMenuOpen ? 'bg-warm-white/90 backdrop-blur-md py-4 shadow-sm' : 'bg-warm-white py-6'
    ]"
  >
    <!-- 捲動進度指示條 -->
    <div
      class="absolute top-0 left-0 h-[2px] bg-emerald-brand origin-left will-change-transform"
      :style="{ transform: `scaleX(${scrollProgress})` }"
    ></div>

    <nav class="container-custom flex justify-between items-center">
      <!-- 品牌標誌 -->
      <NuxtLink
        to="/"
        class="text-2xl font-serif font-bold tracking-zh text-charcoal hover:text-emerald-brand transition-colors duration-500"
        @click="closeAll"
      >
        傑丞建築機構
      </NuxtLink>

      <!-- 桌機版選單 -->
      <div class="hidden md:flex items-center space-x-10">
        <template v-for="link in navLinks" :key="link.path">
          <!-- 一般連結 -->
          <NuxtLink
            v-if="!link.dropdown"
            :to="link.path"
            class="nav-link relative group overflow-hidden"
            active-class="active-link"
          >
            <span class="font-sans text-sm font-medium uppercase tracking-widest text-charcoal/70 group-hover:text-charcoal transition-colors duration-300">
              {{ link.name }}
            </span>
            <span class="absolute bottom-0 left-0 w-full h-[1px] bg-emerald-brand transform translate-x-[-105%] group-hover:translate-x-0 transition-transform duration-700 elegant-transition"></span>
          </NuxtLink>

          <!-- 含下拉選單的連結 -->
          <div
            v-else
            class="relative"
            @mouseenter="openMenu(link.name)"
            @mouseleave="closeMenu"
          >
            <NuxtLink
              :to="link.path"
              class="nav-link relative group overflow-hidden flex items-center gap-1.5"
              active-class="active-link"
            >
              <span class="font-sans text-sm font-medium uppercase tracking-widest text-charcoal/70 group-hover:text-charcoal transition-colors duration-300">
                {{ link.name }}
              </span>
              <svg
                class="w-2.5 h-2.5 text-charcoal/40 transition-transform duration-300"
                :class="{ 'rotate-180': activeMenu === link.name }"
                viewBox="0 0 10 6" fill="none"
              >
                <path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" />
              </svg>
              <span class="absolute bottom-0 left-0 w-full h-[1px] bg-emerald-brand transform translate-x-[-105%] group-hover:translate-x-0 transition-transform duration-700 elegant-transition"></span>
            </NuxtLink>

            <Transition name="dropdown">
              <!-- 全案管理案例：兩層（分類 → 個別案例） -->
              <div
                v-if="link.dropdown === 'cases' && activeMenu === link.name"
                class="absolute right-0 top-full pt-4 z-50"
              >
                <div class="flex w-[440px] bg-white shadow-xl ring-1 ring-black/[0.07] rounded-sm overflow-hidden">
                  <!-- 分類欄 -->
                  <ul class="w-40 shrink-0 py-3 bg-stone-50/60">
                    <li v-for="cat in caseCategories" :key="cat.key" @mouseenter="activeCat = cat.key">
                      <NuxtLink
                        :to="`/portfolio?tech=${cat.key}`"
                        class="flex items-center justify-between px-5 py-3 text-sm tracking-zh transition-colors duration-200"
                        :class="activeCat === cat.key ? 'bg-white text-emerald-brand' : 'text-charcoal/70 hover:text-charcoal'"
                        @click="closeMenu"
                      >
                        {{ cat.label }}
                        <span class="text-charcoal/25">›</span>
                      </NuxtLink>
                    </li>
                  </ul>
                  <!-- 案例欄 -->
                  <div class="flex-1 py-4 px-5">
                    <p class="font-mono text-[10px] tracking-[0.2em] uppercase text-emerald-brand mb-3">
                      {{ activeCatLabel }} Cases
                    </p>
                    <ul class="space-y-1">
                      <li v-for="p in projectsByCategory(activeCat)" :key="p.id">
                        <NuxtLink
                          :to="`/project/${p.id}`"
                          class="block py-2 text-sm text-charcoal/70 hover:text-emerald-brand tracking-zh transition-colors duration-200"
                          @click="closeMenu"
                        >
                          {{ p.title }}
                        </NuxtLink>
                      </li>
                      <li v-if="!projectsByCategory(activeCat).length" class="py-2 text-sm text-charcoal/30 tracking-zh">
                        案例即將推出
                      </li>
                    </ul>
                    <NuxtLink
                      to="/portfolio"
                      class="inline-block mt-4 font-mono text-[11px] tracking-wider text-charcoal/50 hover:text-emerald-brand transition-colors duration-200"
                      @click="closeMenu"
                    >
                      查看全部案例 →
                    </NuxtLink>
                  </div>
                </div>
              </div>

              <!-- 標章介紹：三大標章直接開啟簡報 -->
              <div
                v-else-if="link.dropdown === 'certs' && activeMenu === link.name"
                class="absolute right-0 top-full pt-4 z-50"
              >
                <div class="w-[320px] bg-white shadow-xl ring-1 ring-black/[0.07] rounded-sm py-3">
                  <a
                    v-for="c in certifications"
                    :key="c.file"
                    :href="withBase(c.file)"
                    target="_blank"
                    rel="noopener"
                    class="flex items-center justify-between gap-3 px-5 py-3 hover:bg-stone-50 transition-colors duration-200 group/cert"
                    @click="closeMenu"
                  >
                    <div>
                      <div class="text-sm text-charcoal/80 group-hover/cert:text-emerald-brand tracking-zh transition-colors duration-200">
                        {{ c.title }}
                      </div>
                      <div class="font-mono text-[10px] tracking-wider text-charcoal/35 mt-0.5">{{ c.sub }}</div>
                    </div>
                    <span class="text-charcoal/30 group-hover/cert:text-emerald-brand transition-colors duration-200">↗</span>
                  </a>
                  <NuxtLink
                    to="/presentations"
                    class="block px-5 pt-2 font-mono text-[11px] tracking-wider text-charcoal/50 hover:text-emerald-brand transition-colors duration-200"
                    @click="closeMenu"
                  >
                    全部標章介紹 →
                  </NuxtLink>
                </div>
              </div>
            </Transition>
          </div>
        </template>
      </div>

      <!-- 手機版選單按鈕 (簡約線條，可開合) -->
      <button
        class="md:hidden relative w-8 h-8 flex flex-col justify-center items-center focus:outline-none"
        :aria-expanded="isMenuOpen"
        aria-label="開啟選單"
        @click="isMenuOpen = !isMenuOpen"
      >
        <span
          :class="[
            'block w-6 h-[1px] bg-charcoal transition-all duration-500 elegant-transition',
            isMenuOpen ? 'translate-y-[3px] rotate-45' : '-translate-y-1'
          ]"
        ></span>
        <span
          :class="[
            'block w-6 h-[1px] bg-charcoal transition-all duration-500 elegant-transition',
            isMenuOpen ? '-translate-y-[2px] -rotate-45' : 'translate-y-1'
          ]"
        ></span>
      </button>
    </nav>

    <!-- 手機版展開選單 -->
    <Transition name="mobile-menu">
      <div v-if="isMenuOpen" class="md:hidden overflow-y-auto max-h-[80vh]">
        <div class="container-custom pt-8 pb-10 flex flex-col space-y-1">
          <template v-for="link in navLinks" :key="link.path">
            <!-- 一般連結 -->
            <NuxtLink
              v-if="!link.dropdown"
              :to="link.path"
              class="py-3 font-sans text-base tracking-zh-wide text-charcoal/70 active:text-emerald-brand"
              active-class="!text-charcoal font-medium"
              @click="closeAll"
            >
              {{ link.name }}
            </NuxtLink>

            <!-- 含下拉的連結 (手風琴) -->
            <div v-else>
              <button
                class="w-full flex items-center justify-between py-3 font-sans text-base tracking-zh-wide text-charcoal/70"
                @click="toggleMobile(link.name)"
              >
                {{ link.name }}
                <svg
                  class="w-3 h-3 text-charcoal/40 transition-transform duration-300"
                  :class="{ 'rotate-180': mobileOpen === link.name }"
                  viewBox="0 0 10 6" fill="none"
                >
                  <path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
              </button>

              <div v-show="mobileOpen === link.name" class="pl-4 pb-3 space-y-4">
                <!-- 案例：分類 + 個別案例 -->
                <template v-if="link.dropdown === 'cases'">
                  <div v-for="cat in caseCategories" :key="cat.key">
                    <NuxtLink
                      :to="`/portfolio?tech=${cat.key}`"
                      class="block py-1.5 text-sm font-medium tracking-zh text-charcoal/80"
                      @click="closeAll"
                    >
                      {{ cat.label }}
                    </NuxtLink>
                    <NuxtLink
                      v-for="p in projectsByCategory(cat.key)"
                      :key="p.id"
                      :to="`/project/${p.id}`"
                      class="block py-1.5 pl-3 text-sm tracking-zh text-charcoal/50 active:text-emerald-brand"
                      @click="closeAll"
                    >
                      — {{ p.title }}
                    </NuxtLink>
                  </div>
                  <NuxtLink
                    to="/portfolio"
                    class="block py-1.5 font-mono text-[11px] tracking-wider text-charcoal/40"
                    @click="closeAll"
                  >
                    查看全部案例 →
                  </NuxtLink>
                </template>

                <!-- 標章：直接開簡報 -->
                <template v-else>
                  <a
                    v-for="c in certifications"
                    :key="c.file"
                    :href="withBase(c.file)"
                    target="_blank"
                    rel="noopener"
                    class="block py-1.5 text-sm tracking-zh text-charcoal/60 active:text-emerald-brand"
                    @click="closeAll"
                  >
                    {{ c.title }} ↗
                  </a>
                </template>
              </div>
            </div>
          </template>
        </div>
      </div>
    </Transition>
  </header>
</template>

<script setup>
const { projectsByTech } = useProjects()
const { iHomeTech } = useIHome()

const base = useRuntimeConfig().app.baseURL
const withBase = (path) => `${base}${path}`.replace(/([^:]\/)\/+/g, '$1')

const navLinks = [
  { name: '首頁', path: '/' },
  { name: '關於我們', path: '/about' },
  { name: '全案管理', path: '/pcm' },
  { name: 'iHome 5.0', path: '/ihome' },
  { name: '全案管理案例', path: '/portfolio', dropdown: 'cases' },
  { name: '標章介紹', path: '/presentations', dropdown: 'certs' },
  { name: '聯絡方式', path: '/contact' }
]

// 下拉以 iHome 5.0 五大宅工法分類
const caseCategories = iHomeTech.map((t) => ({ key: t.key, label: t.title }))

const certifications = [
  { title: '綠建築標章', sub: 'EEWH', file: 'presentation.html' },
  { title: '智慧建築標章', sub: 'Intelligent Building', file: 'presentation-ib.html' },
  { title: '建築能效評估標示', sub: 'BERS', file: 'presentation-bers.html' }
]

const projectsByCategory = (key) => projectsByTech(key)

// 桌機下拉狀態
const firstCat = caseCategories[0]?.key ?? ''
const activeMenu = ref(null)
const activeCat = ref(firstCat)
const activeCatLabel = computed(
  () => caseCategories.find((c) => c.key === activeCat.value)?.label ?? ''
)
const openMenu = (name) => { activeMenu.value = name }
const closeMenu = () => { activeMenu.value = null; activeCat.value = firstCat }

// 手機選單狀態
const isScrolled = ref(false)
const isMenuOpen = ref(false)
const mobileOpen = ref(null)
const scrollProgress = ref(0)

const toggleMobile = (name) => { mobileOpen.value = mobileOpen.value === name ? null : name }
const closeAll = () => { isMenuOpen.value = false; mobileOpen.value = null }

watch(isMenuOpen, (open) => {
  if (process.client) {
    document.body.style.overflow = open ? 'hidden' : ''
  }
})

if (process.client) {
  onMounted(() => {
    const onScroll = () => {
      const doc = document.documentElement
      const scrollTop = doc.scrollTop || document.body.scrollTop
      const scrollHeight = doc.scrollHeight - doc.clientHeight
      scrollProgress.value = scrollHeight > 0 ? scrollTop / scrollHeight : 0
      isScrolled.value = scrollTop > 50
    }
    window.addEventListener('scroll', onScroll, { passive: true })
  })
}
</script>

<style scoped>
.nav-link.active-link span {
  @apply text-charcoal font-semibold;
}

.nav-link.active-link::after {
  content: '';
  @apply absolute bottom-0 left-0 w-full h-[1px] bg-emerald-brand;
}

.nav-link {
  padding: 4px 0;
}

/* 桌機下拉動畫 */
.dropdown-enter-active,
.dropdown-leave-active {
  transition: opacity 0.25s ease, transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}
.dropdown-enter-from,
.dropdown-leave-to {
  opacity: 0;
  transform: translateY(6px);
}

/* 手機選單展開動畫 */
.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: max-height 0.6s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.5s ease;
  max-height: 80vh;
}
.mobile-menu-enter-from,
.mobile-menu-leave-to {
  max-height: 0;
  opacity: 0;
}
</style>
