<template>
  <header
    :class="[
      'fixed top-0 left-0 right-0 z-50 transition-all duration-700 elegant-transition',
      isScrolled || isMenuOpen
        ? 'backdrop-blur-2xl bg-[#050505]/80 border-b border-white/[0.08] py-4 shadow-[0_4px_30px_rgba(0,0,0,0.5)]'
        : 'backdrop-blur-md bg-transparent py-6'
    ]"
  >
    <!-- 捲動進度指示條 with emerald glow -->
    <div
      class="absolute top-0 left-0 h-[1.5px] bg-[#10b981] origin-left will-change-transform"
      :style="{ transform: `scaleX(${scrollProgress})`, boxShadow: scrollProgress > 0 ? '0 0 12px rgba(16,185,129,0.7)' : 'none' }"
    ></div>

    <nav class="container-custom flex justify-between items-center">
      <!-- 品牌標誌 -->
      <NuxtLink
        to="/"
        class="text-xl font-serif font-bold tracking-zh text-white hover:text-[#10b981] transition-colors duration-500"
        @click="closeAll"
      >
        傑丞建築機構
      </NuxtLink>

      <!-- 桌機版選單 -->
      <div class="hidden md:flex items-center space-x-9">
        <template v-for="link in navLinks" :key="link.path">
          <NuxtLink
            v-if="!link.dropdown"
            :to="link.path"
            class="nav-link relative group overflow-hidden"
            active-class="active-link"
          >
            <span class="font-sans text-xs font-medium uppercase tracking-widest text-white/55 group-hover:text-white transition-colors duration-300">
              {{ link.name }}
            </span>
            <span class="absolute bottom-0 left-0 w-full h-[1px] bg-[#10b981] transform translate-x-[-105%] group-hover:translate-x-0 transition-transform duration-700 elegant-transition" style="box-shadow: 0 0 6px rgba(16,185,129,0.8)"></span>
          </NuxtLink>

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
              <span class="font-sans text-xs font-medium uppercase tracking-widest text-white/55 group-hover:text-white transition-colors duration-300">
                {{ link.name }}
              </span>
              <svg
                class="w-2.5 h-2.5 text-white/30 transition-transform duration-300"
                :class="{ 'rotate-180': activeMenu === link.name }"
                viewBox="0 0 10 6" fill="none"
              >
                <path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" />
              </svg>
              <span class="absolute bottom-0 left-0 w-full h-[1px] bg-[#10b981] transform translate-x-[-105%] group-hover:translate-x-0 transition-transform duration-700 elegant-transition"></span>
            </NuxtLink>

            <Transition name="dropdown">
              <!-- 全案管理案例下拉 -->
              <div
                v-if="link.dropdown === 'cases' && activeMenu === link.name"
                class="absolute right-0 top-full pt-4 z-50"
              >
                <div class="flex w-[440px] glass-card rounded-xl overflow-hidden">
                  <ul class="w-40 shrink-0 py-3 bg-white/[0.04]">
                    <li v-for="cat in caseCategories" :key="cat.key" @mouseenter="activeCat = cat.key">
                      <NuxtLink
                        :to="`/portfolio?tech=${cat.key}`"
                        class="flex items-center justify-between px-5 py-3 text-sm tracking-zh transition-colors duration-200"
                        :class="activeCat === cat.key ? 'text-[#10b981]' : 'text-white/50 hover:text-white'"
                        @click="closeMenu"
                      >
                        {{ cat.label }}
                        <span class="text-white/20">›</span>
                      </NuxtLink>
                    </li>
                  </ul>
                  <div class="flex-1 py-4 px-5 bg-transparent">
                    <p class="font-mono text-[10px] tracking-[0.2em] uppercase text-[#10b981] mb-3">
                      {{ activeCatLabel }} Cases
                    </p>
                    <ul class="space-y-1">
                      <li v-for="p in projectsByCategory(activeCat)" :key="p.id">
                        <NuxtLink
                          :to="`/project/${p.id}`"
                          class="block py-2 text-sm text-white/55 hover:text-[#10b981] tracking-zh transition-colors duration-200"
                          @click="closeMenu"
                        >
                          {{ p.title }}
                        </NuxtLink>
                      </li>
                      <li v-if="!projectsByCategory(activeCat).length" class="py-2 text-sm text-white/25 tracking-zh">
                        案例即將推出
                      </li>
                    </ul>
                    <NuxtLink
                      to="/portfolio"
                      class="inline-block mt-4 font-mono text-[11px] tracking-wider text-white/35 hover:text-[#10b981] transition-colors duration-200"
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
                class="absolute right-0 top-full pt-4 z-50"
              >
                <div class="w-[320px] glass-card rounded-xl py-3">
                  <a
                    v-for="c in certifications"
                    :key="c.file"
                    :href="withBase(c.file)"
                    target="_blank"
                    rel="noopener"
                    class="flex items-center justify-between gap-3 px-5 py-3 hover:bg-white/[0.06] transition-colors duration-200 group/cert"
                    @click="closeMenu"
                  >
                    <div>
                      <div class="text-sm text-white/70 group-hover/cert:text-[#10b981] tracking-zh transition-colors duration-200">
                        {{ c.title }}
                      </div>
                      <div class="font-mono text-[10px] tracking-wider text-white/30 mt-0.5">{{ c.sub }}</div>
                    </div>
                    <span class="text-white/25 group-hover/cert:text-[#10b981] transition-colors duration-200">↗</span>
                  </a>
                  <NuxtLink
                    to="/presentations"
                    class="block px-5 pt-2 font-mono text-[11px] tracking-wider text-white/35 hover:text-[#10b981] transition-colors duration-200"
                    @click="closeMenu"
                  >
                    全部標章介紹 →
                  </NuxtLink>
                </div>
              </div>
            </Transition>
          </div>
        </template>

        <!-- Contact CTA pill -->
        <NuxtLink
          to="/contact"
          class="ml-2 px-5 py-2 glass rounded-full font-mono text-[10px] uppercase tracking-widest text-white/70 hover:text-white hover:bg-[#10b981]/20 hover:border-[#10b981]/40 transition-all duration-500"
        >
          聯絡
        </NuxtLink>
      </div>

      <!-- 手機版選單按鈕 -->
      <button
        class="md:hidden relative w-8 h-8 flex flex-col justify-center items-center focus:outline-none"
        :aria-expanded="isMenuOpen"
        aria-label="開啟選單"
        @click="isMenuOpen = !isMenuOpen"
      >
        <span
          :class="[
            'block w-6 h-[1px] bg-white transition-all duration-500 elegant-transition',
            isMenuOpen ? 'translate-y-[3px] rotate-45' : '-translate-y-1'
          ]"
        ></span>
        <span
          :class="[
            'block w-6 h-[1px] bg-white transition-all duration-500 elegant-transition',
            isMenuOpen ? '-translate-y-[2px] -rotate-45' : 'translate-y-1'
          ]"
        ></span>
      </button>
    </nav>

    <!-- 手機版展開選單 -->
    <Transition name="mobile-menu">
      <div v-if="isMenuOpen" class="md:hidden overflow-y-auto max-h-[80vh] backdrop-blur-2xl bg-[#050505]/95 border-t border-white/[0.08]">
        <div class="container-custom pt-8 pb-10 flex flex-col space-y-1">
          <template v-for="link in navLinks" :key="link.path">
            <NuxtLink
              v-if="!link.dropdown"
              :to="link.path"
              class="py-3 font-sans text-base tracking-zh-wide text-white/55 active:text-[#10b981]"
              active-class="!text-white font-medium"
              @click="closeAll"
            >
              {{ link.name }}
            </NuxtLink>

            <div v-else>
              <button
                class="w-full flex items-center justify-between py-3 font-sans text-base tracking-zh-wide text-white/55"
                @click="toggleMobile(link.name)"
              >
                {{ link.name }}
                <svg
                  class="w-3 h-3 text-white/30 transition-transform duration-300"
                  :class="{ 'rotate-180': mobileOpen === link.name }"
                  viewBox="0 0 10 6" fill="none"
                >
                  <path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
              </button>

              <div v-show="mobileOpen === link.name" class="pl-4 pb-3 space-y-4">
                <template v-if="link.dropdown === 'cases'">
                  <div v-for="cat in caseCategories" :key="cat.key">
                    <NuxtLink
                      :to="`/portfolio?tech=${cat.key}`"
                      class="block py-1.5 text-sm font-medium tracking-zh text-white/70"
                      @click="closeAll"
                    >
                      {{ cat.label }}
                    </NuxtLink>
                    <NuxtLink
                      v-for="p in projectsByCategory(cat.key)"
                      :key="p.id"
                      :to="`/project/${p.id}`"
                      class="block py-1.5 pl-3 text-sm tracking-zh text-white/40 active:text-[#10b981]"
                      @click="closeAll"
                    >
                      — {{ p.title }}
                    </NuxtLink>
                  </div>
                  <NuxtLink
                    to="/portfolio"
                    class="block py-1.5 font-mono text-[11px] tracking-wider text-white/30"
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
                    class="block py-1.5 text-sm tracking-zh text-white/50 active:text-[#10b981]"
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
]

const caseCategories = iHomeTech.map((t) => ({ key: t.key, label: t.title }))

const certifications = [
  { title: '綠建築標章', sub: 'EEWH', file: 'presentation.html' },
  { title: '智慧建築標章', sub: 'Intelligent Building', file: 'presentation-ib.html' },
  { title: '建築能效評估標示', sub: 'BERS', file: 'presentation-bers.html' }
]

const projectsByCategory = (key) => projectsByTech(key)

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
      isScrolled.value = scrollTop > 50
    }
    window.addEventListener('scroll', onScroll, { passive: true })
  })
}
</script>

<style scoped>
.nav-link.active-link span {
  color: white;
  font-weight: 500;
}

.nav-link.active-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 1px;
  background: #10b981;
  box-shadow: 0 0 6px rgba(16,185,129,0.8);
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
