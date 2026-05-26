<template>
  <header
    :class="[
      'fixed top-0 left-0 right-0 z-50 transition-all duration-700 elegant-transition',
      isScrolled ? 'bg-warm-white/90 backdrop-blur-md py-4 shadow-sm' : 'bg-warm-white py-6'
    ]"
  >
    <nav class="container-custom flex justify-between items-center">
      <!-- 品牌標誌：使用襯線體展現人文氣息 -->
      <NuxtLink
        to="/"
        class="text-2xl font-serif font-bold tracking-tighter text-charcoal hover:text-emerald-brand transition-colors duration-500"
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
          <span class="absolute bottom-0 left-0 w-full h-[1px] bg-emerald-brand transform translate-x-[-105%] group-hover:translate-x-0 transition-transform duration-700 cubic-bezier(0.16, 1, 0.3, 1)"></span>
        </NuxtLink>
      </div>

      <!-- 手機版選單按鈕 (簡約線條) -->
      <button class="md:hidden flex flex-col space-y-1.5 p-2 focus:outline-none">
        <span class="w-6 h-[1px] bg-charcoal"></span>
        <span class="w-6 h-[1px] bg-charcoal"></span>
      </button>
    </nav>
  </header>
</template>

<script setup>
const isScrolled = ref(false)

const navLinks = [
  { name: '首頁', path: '/' },
  { name: '關於我們', path: '/about' },
  { name: '全案管理', path: '/pcm' },
  { name: '作品集', path: '/portfolio' },
  { name: '簡報', path: '/presentations' },
  { name: '聯絡方式', path: '/contact' }
]

// 處理滾動效果
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

/* 確保點擊連結後平滑感 */
.nav-link {
  padding: 4px 0;
}
</style>