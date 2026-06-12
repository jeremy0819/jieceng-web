<template>
  <footer class="relative bg-charcoal">
    <!-- 頂部翠綠分隔光 -->
    <div class="absolute top-0 inset-x-0 h-[1px] bg-gradient-to-r from-transparent via-emerald-brand/25 to-transparent"></div>

    <div class="container-custom py-20 md:py-24">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-14 md:gap-8 items-start">

        <!-- 品牌資訊 -->
        <div class="md:col-span-5 space-y-7">
          <NuxtLink to="/" class="font-serif text-2xl font-bold tracking-zh text-warm-white hover:text-emerald-brand-light transition-colors duration-500 inline-block">
            傑丞建築機構
          </NuxtLink>
          <p class="max-w-xs font-sans text-sm text-warm-white/40 leading-relaxed tracking-zh">
            構築永續未來，定義空間美學。以 iHome 5.0 專利工法，為每位居住者打造具備人文溫度的百年建築。
          </p>
          <div class="flex items-center gap-3 pt-1">
            <span class="w-6 h-px bg-emerald-brand"></span>
            <span class="font-mono text-[10px] tracking-[0.35em] uppercase text-emerald-brand-light">Sustainable · Centennial · 2006–</span>
          </div>
        </div>

        <!-- 快速連結 -->
        <div class="md:col-span-3 space-y-6">
          <h4 class="font-mono text-[10px] uppercase tracking-[0.3em] text-emerald-brand-light">Navigation</h4>
          <ul class="space-y-3.5">
            <li v-for="link in navLinks" :key="link.path">
              <NuxtLink
                :to="link.path"
                class="font-sans text-sm text-warm-white/45 hover:text-warm-white transition-colors duration-500 tracking-zh"
              >
                {{ link.name }}
              </NuxtLink>
            </li>
          </ul>
        </div>

        <!-- 聯絡與版權 -->
        <div class="md:col-span-4 space-y-6">
          <h4 class="font-mono text-[10px] uppercase tracking-[0.3em] text-emerald-brand-light">Contact</h4>
          <div class="space-y-3">
            <p class="font-sans text-sm text-warm-white/45 tracking-zh leading-relaxed">
              桃園市桃園區大興西路一段 268 號<br />印象羅芙 19 樓
            </p>
            <a href="mailto:jason.house2007@gmail.com" class="font-sans text-sm text-warm-white/45 hover:text-emerald-brand-light transition-colors duration-500 block">
              jason.house2007@gmail.com
            </a>
          </div>
          <div class="pt-4 border-t border-warm-white/[0.06]">
            <p class="font-mono text-[10px] text-warm-white/20 tracking-[0.15em] leading-loose uppercase">
              &copy; {{ currentYear }} JIECENG ARCHITECTURE<br />ALL RIGHTS RESERVED.
            </p>
          </div>
        </div>

      </div>

      <!-- 底部裝飾線 -->
      <div class="mt-20 w-full h-px bg-gradient-to-r from-transparent via-warm-white/[0.06] to-transparent"></div>
    </div>
  </footer>
</template>

<script setup>
const currentYear = new Date().getFullYear()

const navLinks = [
  { name: '首頁', path: '/' },
  { name: '關於我們', path: '/about' },
  { name: '全案管理', path: '/pcm' },
  { name: 'iHome 5.0', path: '/ihome' },
  { name: '全案管理案例', path: '/portfolio' },
  { name: '都更說明會', path: '/briefing' },
  { name: '標章介紹', path: '/presentations' },
  { name: '聯絡方式', path: '/contact' },
]
</script>
