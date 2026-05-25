<template>
  <header
    :class="[
      'fixed top-0 left-0 right-0 z-50 transition-all duration-700 elegant-transition',
      isScrolled || isMenuOpen ? 'bg-warm-white/90 backdrop-blur-md py-4 shadow-sm' : 'bg-warm-white py-6'
    ]"
  >
    <nav class="container-custom flex justify-between items-center">
      <!-- 品牌標誌：襯線體展現人文氣息，中文採用較舒展的字距 -->
      <NuxtLink
        to="/"
        class="text-2xl font-serif font-bold tracking-zh text-charcoal hover:text-emerald-brand transition-colors duration-500"
        @click="isMenuOpen = false"
      >
        傑丞建築機構
      </NuxtLink>

      <!-- 桌機版選單 -->
      <div class="hidden md:flex items-center space-x-12">
        <NuxtLink
          v-for="link in navLinks"
          :key="link.path"
          :to="link.path"
          class="nav-link relative group overflow-hidden"
          active-class="active-link"
        >
          <span class="font-sans text-sm font-medium uppercase tracking-widest text-charcoal/70 group-hover:text-charcoal transition-colors duration-300">
            {{ link.name }}
          </span>
          <!-- 翡翠綠裝飾底線 -->
          <span class="absolute bottom-0 left-0 w-full h-[1px] bg-emerald-brand transform translate-x-[-105%] group-hover:translate-x-0 transition-transform duration-700 elegant-transition"></span>
        </NuxtLink>
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
      <div v-if="isMenuOpen" class="md:hidden overflow-hidden">
        <div class="container-custom pt-8 pb-10 flex flex-col space-y-6">
          <NuxtLink
            v-for="link in navLinks"
            :key="link.path"
            :to="link.path"
            class="font-sans text-base tracking-zh-wide text-charcoal/70 active:text-emerald-brand"
            active-class="!text-charcoal font-medium"
            @click="isMenuOpen = false"
          >
            {{ link.name }}
          </NuxtLink>
        </div>
      </div>
    </Transition>
  </header>
</template>

<script setup>
const isScrolled = ref(false)
const isMenuOpen = ref(false)

const navLinks = [
  { name: '首頁', path: '/' },
  { name: '關於我們', path: '/about' },
  { name: '全案管理', path: '/pcm' },
  { name: '作品集', path: '/portfolio' },
  { name: '聯絡方式', path: '/contact' }
]

// 切換選單時鎖定/解鎖背景捲動
watch(isMenuOpen, (open) => {
  if (process.client) {
    document.body.style.overflow = open ? 'hidden' : ''
  }
})

if (process.client) {
  onMounted(() => {
    window.addEventListener('scroll', () => {
      isScrolled.value = window.scrollY > 50
    })
  })
}
</script>

<style scoped>
.elegant-transition {
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}

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

/* 手機選單展開動畫 */
.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: max-height 0.6s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.5s ease;
  max-height: 320px;
}
.mobile-menu-enter-from,
.mobile-menu-leave-to {
  max-height: 0;
  opacity: 0;
}
</style>
