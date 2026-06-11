<template>
  <header
    :class="[
      'fixed top-0 left-0 right-0 z-50 transition-all duration-700 elegant-transition',
      isScrolled || isMenuOpen
        ? 'glass border-b border-black/[0.07] py-3.5 shadow-[0_2px_20px_rgba(28,26,23,0.08)]'
        : 'bg-transparent py-5'
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
        :class="[
          'text-xl font-serif font-bold tracking-zh transition-colors duration-500',
          isScrolled ? 'text-charcoal hover:text-emerald-brand' : 'text-white hover:text-emerald-brand-light'
        ]"
        @click="closeAll"
      >
        傑丞建築機構
      </NuxtLink>

      <!-- 桌機版選單 -->
      <div class="hidden md:flex items-center space-x-8">
        <template v-for="link in navLinks" :key="link.path">
          <NuxtLink
            v-if="!link.dropdown"
            :to="link.path"
            class="nav-link relative group overflow-hidden pb-1"
            active-class="active-link"
          >
            <span :class="[
              'font-mono text-[10px] font-medium uppercase tracking-[0.18em] transition-colors duration-300',
              isScrolled ? 'text-charcoal/55 group-hover:text-charcoal' : 'text-white/65 group-hover:text-white'
            ]">
              {{ link.name }}
            </span>
            <!-- 滑入底線 -->
            <span class="absolute bottom-0 left-0 w-full h-[1.5px] bg-emerald-brand transform translate-x-[-105%] group-hover:translate-x-0 transition-transform duration-600 elegant-transition"></span>
          </NuxtLink>

          <div
            v-else
            class="relative"
            @mouseenter="openMenu(link.name)"
            @mouseleave="closeMenu"
          >
            <NuxtLink
              :to="link.path"
              class="nav-link relative group overflow-hidden pb-1 flex items-center gap-1.5"
              active-class="active-link"
            >
              <span :class="[
                'font-mono text-[10px] font-medium uppercase tracking-[0.18em] transition-colors duration-300',
                isScrolled ? 'text-charcoal/55 group-hover:text-charcoal' : 'text-white/65 group-hover:text-white'
              ]">
                {{ link.name }}
              </span>
              <svg
                :class="[
                  'w-2.5 h-2.5 transition-all duration-400',
                  isScrolled ? 'text-charcoal/30' : 'text-white/35',
                  activeMenu === link.name ? 'rotate-180' : ''
                ]"
                viewBox="0 0 10 6" fill="none"
              >
                <path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" />
              </svg>
              <span class="absolute bottom-0 left-0 w-full h-[1.5px] bg-emerald-brand transform translate-x-[-105%] group-hover:translate-x-0 transition-transform duration-600 elegant-transition"></span>
            </NuxtLink>

            <Transition name="dropdown">
              <!-- 全案管理案例：類別 + 建案列表 -->
              <div
                v-if="link.dropdown === 'cases' && activeMenu === link.name"
                class="absolute left-0 top-full pt-3 z-50"
              >
                <div class="flex w-[420px] glass-card rounded-xl overflow-hidden">
                  <ul class="w-36 shrink-0 py-3 bg-black/[0.025]">
                    <li v-for="cat in caseCategories" :key="cat.key" @mouseenter="activeCat = cat.key">
                      <button
                        class="w-full flex items-center justify-between px-5 py-3 text-sm tracking-zh transition-colors duration-200 text-left"
                        :class="activeCat === cat.key ? 'text-emerald-brand font-medium' : 'text-charcoal/55 hover:text-charcoal'"
                      >
                        {{ cat.label }}
                        <span class="text-charcoal/20">›</span>
                      </button>
                    </li>
                  </ul>
                  <div class="flex-1 py-4 px-5">
                    <p class="font-mono text-[10px] tracking-[0.2em] uppercase text-emerald-brand mb-3">
                      {{ activeCatLabel }}
                    </p>
                    <ul class="space-y-1">
                      <li v-for="p in projectsByCat(activeCat)" :key="p.id">
                        <NuxtLink
                          :to="`/project/${p.id}`"
                          class="block py-2 text-sm text-charcoal/60 hover:text-emerald-brand tracking-zh transition-colors duration-200"
                          @click="closeMenu"
                        >
                          {{ p.title }}
                        </NuxtLink>
                      </li>
                      <li v-if="!projectsByCat(activeCat).length" class="py-2 text-sm text-charcoal/30 tracking-zh">
                        案例即將推出
                      </li>
                    </ul>
                    <NuxtLink
                      to="/portfolio"
                      class="inline-block mt-4 font-mono text-[11px] tracking-wider text-charcoal/40 hover:text-emerald-brand transition-colors duration-200"
                      @click="closeMenu"
                    >
                      查看全部案例 →
                    </NuxtLink>
                  </div>
                </div>
              </div>

              <!-- 標章介紹下拉 -->
              <div
                v-else-if="link.dropdown === 'certs' && activeMenu === link.name"
                class="absolute right-0 top-full pt-3 z-50"
              >
                <div class="w-[300px] glass-card rounded-xl py-3">
                  <a
                    v-for="c in certifications"
                    :key="c.file"
                    :href="withBase(c.file)"
                    target="_blank"
                    rel="noopener"
                    class="flex items-center justify-between gap-3 px-5 py-3 hover:bg-emerald-brand/5 transition-colors duration-200 group/cert"
                    @click="closeMenu"
                  >
                    <div>
                      <div class="text-sm text-charcoal/75 group-hover/cert:text-emerald-brand tracking-zh transition-colors duration-200">
                        {{ c.title }}
                      </div>
                      <div class="font-mono text-[10px] tracking-wider text-charcoal/35 mt-0.5">{{ c.sub }}</div>
                    </div>
                    <span class="text-charcoal/25 group-hover/cert:text-emerald-brand transition-colors duration-200">↗</span>
                  </a>
                  <NuxtLink
                    to="/presentations"
                    class="block px-5 pt-2 pb-1 font-mono text-[11px] tracking-wider text-charcoal/40 hover:text-emerald-brand transition-colors duration-200"
                    @click="closeMenu"
                  >
                    全部標章介紹 →
                  </NuxtLink>
                </div>
              </div>
            </Transition>
          </div>
        </template>

        <!-- 聯絡 CTA -->
        <NuxtLink
          to="/contact"
          class="ml-1 px-5 py-2.5 bg-emerald-brand text-white rounded-full font-mono text-[10px] uppercase tracking-widest hover:bg-emerald-brand/80 transition-all duration-500 shadow-sm"
        >
          聯絡諮詢
        </NuxtLink>
      </div>

      <!-- 手機版漢堡按鈕 -->
      <button
        class="md:hidden relative w-8 h-8 flex flex-col justify-center items-center focus:outline-none"
        :aria-expanded="isMenuOpen"
        aria-label="開啟選單"
        @click="isMenuOpen = !isMenuOpen"
      >
        <span
          :class="[
            'block w-6 h-[1.5px] transition-all duration-500 elegant-transition',
            isScrolled || isMenuOpen ? 'bg-charcoal' : 'bg-white',
            isMenuOpen ? 'translate-y-[3.5px] rotate-45' : '-translate-y-1'
          ]"
        ></span>
        <span
          :class="[
            'block w-6 h-[1.5px] transition-all duration-500 elegant-transition',
            isScrolled || isMenuOpen ? 'bg-charcoal' : 'bg-white',
            isMenuOpen ? '-translate-y-[3px] -rotate-45' : 'translate-y-1'
          ]"
        ></span>
      </button>
    </nav>

    <!-- 手機版展開選單 -->
    <Transition name="mobile-menu">
      <div v-if="isMenuOpen" class="md:hidden overflow-y-auto max-h-[85vh] glass border-t border-black/[0.06]">
        <div class="container-custom pt-6 pb-10 flex flex-col space-y-0.5">
          <template v-for="link in allMobileLinks" :key="link.path">
            <NuxtLink
              v-if="!link.dropdown"
              :to="link.path"
              class="py-3.5 font-sans text-base tracking-zh-wide text-charcoal/65 border-b border-black/[0.05] last:border-0"
              active-class="!text-charcoal font-medium"
              @click="closeAll"
            >
              {{ link.name }}
            </NuxtLink>

            <div v-else class="border-b border-black/[0.05]">
              <button
                class="w-full flex items-center justify-between py-3.5 font-sans text-base tracking-zh-wide text-charcoal/65"
                @click="toggleMobile(link.name)"
              >
                {{ link.name }}
                <svg
                  class="w-3 h-3 text-charcoal/30 transition-transform duration-300"
                  :class="{ 'rotate-180': mobileOpen === link.name }"
                  viewBox="0 0 10 6" fill="none"
                >
                  <path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
              </button>

              <div v-show="mobileOpen === link.name" class="pl-4 pb-4 space-y-3">
                <template v-if="link.dropdown === 'cases'">
                  <div v-for="cat in caseCategories" :key="cat.key">
                    <p class="py-1.5 text-xs font-mono tracking-widest text-emerald-brand uppercase">{{ cat.label }}</p>
                    <NuxtLink
                      v-for="p in projectsByCat(cat.key)"
                      :key="p.id"
                      :to="`/project/${p.id}`"
                      class="block py-1.5 pl-3 text-sm tracking-zh text-charcoal/55"
                      @click="closeAll"
                    >
                      — {{ p.title }}
                    </NuxtLink>
                  </div>
                  <NuxtLink
                    to="/portfolio"
                    class="block py-1.5 font-mono text-[11px] tracking-wider text-charcoal/35"
                    @click="closeAll"
                  >
                    查看全部案例 →
                  </NuxtLink>
                </template>

                <template v-else>
                  <a
                    v-for="c in certifications"
                    :key="c.file"
                    :href="withBase(c.file)"
                    target="_blank"
                    rel="noopener"
                    class="block py-1.5 text-sm tracking-zh text-charcoal/55"
                    @click="closeAll"
                  >
                    {{ c.title }} ↗
                  </a>
                </template>
              </div>
            </div>
          </template>

          <!-- 手機版 CTA -->
          <div class="pt-6">
            <NuxtLink
              to="/contact"
              class="block text-center py-4 bg-emerald-brand text-white rounded-full font-mono text-xs uppercase tracking-widest hover:bg-emerald-brand/80 transition-colors duration-500"
              @click="closeAll"
            >
              聯絡諮詢
            </NuxtLink>
          </div>
        </div>
      </div>
    </Transition>
  </header>
</template>

<script setup>
const { projectsByCategory } = useProjects()
const { iHomeTech } = useIHome()

const base = useRuntimeConfig().app.baseURL
const withBase = (path) => `${base}${path}`.replace(/([^:]\/)\/+/g, '$1')

// 全案管理案例下拉：依案件類型分類（非 iHome 五大宅）
const caseCategories = [
  { key: 'residential', label: '住宅建案' },
  { key: 'renewal', label: '都更案' },
]

const certifications = [
  { title: '綠建築標章', sub: 'EEWH', file: 'presentation.html' },
  { title: '智慧建築標章', sub: 'Intelligent Building', file: 'presentation-ib.html' },
  { title: '建築能效評估標示', sub: 'BERS', file: 'presentation-bers.html' }
]

const projectsByCat = (key) => projectsByCategory(key)

const navLinks = [
  { name: '首頁', path: '/' },
  { name: '關於我們', path: '/about' },
  { name: '全案管理', path: '/pcm' },
  { name: 'iHome 5.0', path: '/ihome' },
  { name: '全案管理案例', path: '/portfolio', dropdown: 'cases' },
  { name: '說明會', path: '/briefing' },
  { name: '標章介紹', path: '/presentations', dropdown: 'certs' },
]

// 手機版所有連結（展開展示）
const allMobileLinks = navLinks

const firstCat = caseCategories[0]?.key ?? ''
const activeMenu = ref(null)
const activeCat = ref(firstCat)
const activeCatLabel = computed(
  () => caseCategories.find((c) => c.key === activeCat.value)?.label ?? ''
)
const openMenu = (name) => { activeMenu.value = name }
const closeMenu = () => { activeMenu.value = null; activeCat.value = firstCat }

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
      isScrolled.value = scrollTop > 60
    }
    window.addEventListener('scroll', onScroll, { passive: true })
  })
}
</script>

<style scoped>
.nav-link.active-link span {
  color: #064e3b;
  font-weight: 500;
}

.nav-link.active-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 1.5px;
  background: #064e3b;
}

.nav-link {
  padding: 4px 0;
}

.dropdown-enter-active,
.dropdown-leave-active {
  transition: opacity 0.22s ease, transform 0.22s cubic-bezier(0.16, 1, 0.3, 1);
}
.dropdown-enter-from,
.dropdown-leave-to {
  opacity: 0;
  transform: translateY(8px);
}

.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: max-height 0.55s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.45s ease;
  max-height: 85vh;
}
.mobile-menu-enter-from,
.mobile-menu-leave-to {
  max-height: 0;
  opacity: 0;
}
</style>
