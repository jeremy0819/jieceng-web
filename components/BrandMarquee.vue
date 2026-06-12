<template>
  <!-- 品牌跑馬燈帶：建築關鍵字無縫捲動，hover 暫停 -->
  <div
    class="marquee py-5 md:py-6 border-y bg-white"
    :class="dark ? 'bg-charcoal border-warm-white/[0.07]' : 'bg-white border-charcoal/[0.07]'"
    aria-hidden="true"
  >
    <div class="marquee-track">
      <div v-for="n in 2" :key="n" class="flex shrink-0 items-center">
        <template v-for="(word, i) in words" :key="`${n}-${i}`">
          <span
            class="font-serif text-xl md:text-2xl font-light tracking-zh px-6 md:px-10 whitespace-nowrap"
            :class="dark ? 'text-warm-white/60' : 'text-charcoal/55'"
          >
            {{ word }}
          </span>
          <span class="font-mono text-xs" :class="dark ? 'text-emerald-brand-light' : 'text-emerald-brand'">＋</span>
        </template>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  dark: { type: Boolean, default: false }
})

const words = [
  '百年宅', '健康宅', '節能宅', '智慧宅', '履歷宅',
  'iHome 5.0', '永續建築', '全案管理', '都市更新', '綠建築標章'
]
</script>
