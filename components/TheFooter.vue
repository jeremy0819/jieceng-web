<template>
  <footer class="relative bg-[#080808] border-t border-white/[0.07]">
    <!-- 頂部翠綠環境光 -->
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[600px] h-[1px] bg-gradient-to-r from-transparent via-[#10b981]/30 to-transparent pointer-events-none"></div>

    <div class="container-custom py-20 md:py-24">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-14 md:gap-8 items-start">

        <!-- 品牌資訊 -->
        <div class="md:col-span-6 space-y-7">
          <NuxtLink to="/" class="font-serif text-2xl font-bold tracking-zh text-white hover:text-[#10b981] transition-colors duration-500 inline-block">
            傑丞建築機構
          </NuxtLink>
          <p class="max-w-sm font-sans text-sm text-white/40 leading-relaxed tracking-zh">
            構築永續未來，定義空間美學。以 iHome 5.0 專利工法，為每一位居住者打造具備人文溫度的百年建築。
          </p>
          <div class="flex items-center gap-2 pt-2">
            <span class="w-5 h-px bg-[#10b981]"></span>
            <span class="font-mono text-[10px] tracking-[0.35em] uppercase text-[#10b981]">Sustainable · Centennial</span>
          </div>
        </div>

        <!-- 快速連結 -->
        <div class="md:col-span-3 space-y-6">
          <h4 class="font-mono text-[10px] uppercase tracking-[0.3em] text-[#10b981]">Navigation</h4>
          <ul class="space-y-3.5">
            <li v-for="link in navLinks" :key="link.path">
              <NuxtLink
                :to="link.path"
                class="font-sans text-sm text-white/45 hover:text-white transition-colors duration-500 tracking-zh"
              >
                {{ link.name }}
              </NuxtLink>
            </li>
          </ul>
        </div>

        <!-- 聯絡與版權 -->
        <div class="md:col-span-3 space-y-6">
          <h4 class="font-mono text-[10px] uppercase tracking-[0.3em] text-[#10b981]">Contact</h4>
          <div class="space-y-2.5">
            <p class="font-sans text-sm text-white/45 tracking-zh leading-relaxed">
              桃園市桃園區大興西路<br />一段268號 印象羅芙19樓
            </p>
            <a href="mailto:jason.house2007@gmail.com" class="font-sans text-sm text-white/45 hover:text-[#10b981] transition-colors duration-500 block">
              jason.house2007@gmail.com
            </a>
          </div>
          <p class="font-mono text-[10px] text-white/20 tracking-[0.15em] leading-loose uppercase pt-2">
            &copy; {{ currentYear }} JIECENG ARCHITECTURE.<br />ALL RIGHTS RESERVED.
          </p>
        </div>

      </div>

      <!-- 底部裝飾線 -->
      <div class="mt-20 w-full h-px bg-gradient-to-r from-transparent via-white/[0.06] to-transparent"></div>
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
  { name: '標章介紹', path: '/presentations' },
  { name: '聯絡方式', path: '/contact' }
]
</script>
