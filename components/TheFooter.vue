<template>
  <footer class="bg-charcoal text-warm-white py-24">
    <div class="container-custom">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-16 md:gap-8 items-start">

        <!-- 品牌資訊 -->
        <div class="md:col-span-6 space-y-8">
          <NuxtLink to="/" class="font-serif text-3xl font-bold tracking-tighter">
            傑丞建築機構
          </NuxtLink>
          <p class="max-w-sm font-sans text-sm text-warm-white/40 leading-relaxed tracking-wide">
            構築永續未來，定義空間美學。我們透過專業的全案管理與專利工法，為每一位居住者打造具備人文溫度的建築藝術。
          </p>
        </div>

        <!-- 快速連結 -->
        <div class="md:col-span-3 space-y-6">
          <h4 class="font-mono text-[10px] uppercase tracking-[0.3em] text-emerald-brand-light">Navigation</h4>
          <ul class="space-y-4">
            <li v-for="link in ['首頁', '關於我們', '作品集', '聯絡方式']" :key="link">
              <NuxtLink
                to="#"
                class="font-sans text-xs text-warm-white/60 hover:text-warm-white transition-colors duration-500 uppercase tracking-widest"
              >
                {{ link }}
              </NuxtLink>
            </li>
          </ul>
        </div>

        <!-- 版權資訊 -->
        <div class="md:col-span-3 space-y-6">
          <h4 class="font-mono text-[10px] uppercase tracking-[0.3em] text-emerald-brand-light">Legal</h4>
          <p class="font-sans text-[10px] text-warm-white/30 tracking-widest leading-loose uppercase">
            &copy; 2025 JIECENG ARCHITECTURE.<br />
            ALL RIGHTS RESERVED.
          </p>
          <div class="pt-4 flex space-x-4">
             <div class="w-8 h-[1px] bg-warm-white/10"></div>
             <span class="font-mono text-[9px] text-warm-white/20 tracking-tighter">TSMC-COMPLIANT DESIGN</span>
          </div>
        </div>

      </div>

      <!-- 底部裝飾線 -->
      <div class="mt-24 w-full h-[1px] bg-gradient-to-r from-warm-white/0 via-warm-white/5 to-warm-white/0"></div>
    </div>
  </footer>
</template>

<style scoped>
/* 頁尾專用微調 */
footer {
  position: relative;
  z-index: 10;
}
</style>