<template>
  <footer class="bg-charcoal text-warm-white py-24">
    <div class="container-custom">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-16 md:gap-8 items-start">

        <!-- 品牌資訊 -->
        <div class="md:col-span-6 space-y-8">
          <NuxtLink to="/" class="font-serif text-3xl font-bold tracking-zh inline-block">
            傑丞建築機構
          </NuxtLink>
          <p class="max-w-sm font-sans text-sm text-warm-white/40 leading-relaxed tracking-zh">
            構築永續未來，定義空間美學。我們透過專業的全案管理與專利工法，為每一位居住者打造具備人文溫度的建築藝術。
          </p>
        </div>

        <!-- 快速連結 -->
        <div class="md:col-span-3 space-y-6">
          <h4 class="font-mono text-[10px] uppercase tracking-[0.3em] text-emerald-brand-light">Navigation</h4>
          <ul class="space-y-4">
            <li v-for="link in navLinks" :key="link.path">
              <NuxtLink
                :to="link.path"
                class="font-sans text-sm text-warm-white/60 hover:text-warm-white transition-colors duration-500 tracking-zh"
              >
                {{ link.name }}
              </NuxtLink>
            </li>
          </ul>
        </div>

        <!-- 聯絡與版權資訊 -->
        <div class="md:col-span-3 space-y-6">
          <h4 class="font-mono text-[10px] uppercase tracking-[0.3em] text-emerald-brand-light">Contact</h4>
          <div class="space-y-2">
            <p class="font-sans text-sm text-warm-white/60 tracking-zh leading-relaxed">
              桃園市桃園區大興西路<br />一段268號 印象羅芙19樓
            </p>
            <a href="tel:+886223456789" class="font-sans text-sm text-warm-white/60 hover:text-warm-white transition-colors duration-500 block">
              (02) 2345-6789
            </a>
          </div>
          <p class="font-mono text-[10px] text-warm-white/30 tracking-[0.2em] leading-loose uppercase pt-2">
            &copy; {{ currentYear }} JIECENG ARCHITECTURE.<br />ALL RIGHTS RESERVED.
          </p>
        </div>

      </div>

      <!-- 底部裝飾線 -->
      <div class="mt-24 w-full h-[1px] bg-gradient-to-r from-warm-white/0 via-warm-white/5 to-warm-white/0"></div>
    </div>
  </footer>
</template>

<script setup>
const currentYear = new Date().getFullYear()

const navLinks = [
  { name: '首頁', path: '/' },
  { name: '關於我們', path: '/about' },
  { name: '全案管理', path: '/pcm' },
  { name: '全案管理案例', path: '/portfolio' },
  { name: '標章介紹', path: '/presentations' },
  { name: '聯絡方式', path: '/contact' }
]
</script>

<style scoped>
footer {
  position: relative;
  z-index: 10;
}

.text-emerald-brand-light {
  color: #10b981;
}
</style>
