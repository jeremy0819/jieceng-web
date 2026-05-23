<template>
  <div class="bg-warm-white min-h-screen">
    <!-- 區塊1: 沉浸式標頭 -->
    <section class="relative h-[60vh] flex items-center overflow-hidden bg-charcoal">
      <div class="absolute inset-0 z-0">
        <img
          src="/image/hero-background.jpg"
          alt="PCM 全案管理"
          class="w-full h-full object-cover opacity-40 scale-105 animate-slow-zoom"
        >
        <div class="absolute inset-0 bg-gradient-to-b from-charcoal/60 to-charcoal/20"></div>
      </div>

      <div class="container-custom relative z-10">
        <div class="max-w-3xl">
          <span class="font-mono text-emerald-brand-light text-xs tracking-[0.3em] uppercase mb-4 block animate-fade-in-up">
            Professional Case Management
          </span>
          <h1 class="font-serif text-5xl md:text-7xl text-warm-white font-light mb-8 animate-fade-in-up" style="animation-delay: 0.2s">
            全案管理 · 價值最大化
          </h1>
          <p class="font-sans text-lg text-warm-white/70 leading-relaxed max-w-xl animate-fade-in-up" style="animation-delay: 0.4s">
            我們提供建築物全生命週期的精準控制，從土地評估、建築設計、到專利工法營造，為地主與企業構築最堅實的資產價值。
          </p>
        </div>
      </div>
    </section>

    <!-- 區塊2: 四大核心價值 -->
    <section class="section-spacing bg-white">
      <div class="container-custom">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
          <div v-for="(value, index) in coreValues" :key="index"
            class="animate-fade-in-up" :style="{ animationDelay: `${index * 0.2}s` }">
            <span class="font-mono text-emerald-brand text-3xl font-light mb-6 block">0{{ index + 1 }}</span>
            <h3 class="font-serif text-xl text-charcoal mb-4">{{ value.title }}</h3>
            <p class="font-sans text-sm text-charcoal/60 leading-relaxed">{{ value.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊3: PCM 服務流程 (垂直時間軸) -->
    <section class="section-spacing bg-warm-white overflow-hidden">
      <div class="container-custom">
        <div class="text-center mb-24">
          <h2 class="font-serif text-4xl md:text-5xl font-light text-charcoal mb-4 animate-fade-in-up">服務流程</h2>
          <div class="h-[1px] w-12 bg-emerald-brand mx-auto animate-fade-in-up" style="animation-delay: 0.2s"></div>
        </div>

        <div class="relative max-w-4xl mx-auto">
          <!-- 中央引導線 -->
          <div class="absolute left-0 md:left-1/2 top-0 bottom-0 w-[1px] bg-charcoal/10 transform md:translate-x-[-0.5px]"></div>

          <!-- 流程節點 -->
          <div v-for="(step, index) in steps" :key="index"
            class="relative mb-24 last:mb-0 flex flex-col md:flex-row items-start animate-fade-in-up"
            :style="{ animationDelay: `${index * 0.2}s` }">

            <!-- 節點圓點 -->
            <div class="absolute left-[-4px] md:left-1/2 md:translate-x-[-4.5px] top-2 w-2.5 h-2.5 rounded-full bg-emerald-brand border-4 border-warm-white"></div>

            <!-- 內容區 -->
            <div :class="[
              'md:w-1/2 pl-8 md:pl-0',
              index % 2 === 0 ? 'md:pr-16 md:text-right' : 'md:ml-auto md:pl-16 text-left'
            ]">
              <span class="font-mono text-[10px] tracking-widest text-emerald-brand uppercase mb-2 block">Phase 0{{ index + 1 }}</span>
              <h4 class="font-serif text-2xl text-charcoal mb-4">{{ step.title }}</h4>
              <p class="font-sans text-sm text-charcoal/60 leading-relaxed">{{ step.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊4: CTA 聯絡我們 -->
    <section class="py-32 bg-charcoal">
      <div class="container-custom text-center">
        <h2 class="font-serif text-3xl md:text-5xl text-warm-white font-light mb-12 animate-fade-in-up">
          準備好開始您的建築計畫？
        </h2>
        <NuxtLink
          to="/contact"
          class="inline-block px-12 py-5 border border-warm-white text-warm-white text-xs tracking-[0.2em] uppercase hover:bg-warm-white hover:text-charcoal transition-all duration-1200 elegant-transition animate-fade-in-up"
        >
          與我們聯繫諮詢
        </NuxtLink>
      </div>
    </section>
  </div>
</template>

<script setup>
const coreValues = [
  { title: '精準成本控制', desc: '透過詳細的概算規劃與採購管理，有效杜絕預算超支，確保每一分投資都精確到位。' },
  { title: '專利工法導入', desc: '整合傑丞研發之當層配管、複層樓板等專利工法，從結構源頭解決漏水與噪音痛點。' },
  { title: '嚴謹進度管理', desc: '數位化工程進度追蹤，確保設計、發包、施工各階段無縫銜接，準時完工交付。' },
  { title: '永續資產維護', desc: '代管期滿後提供完整的建物身分證，讓未來維修管理透明化，提升房產轉手價值。' }
]

const steps = [
  { title: '土地與財務分析', desc: '針對開發基地進行法规檢索、容積率分析與成本回報試算。' },
  { title: '建築設計管理', desc: '媒合頂尖建築師，並由傑丞技術團隊介入，優化管線與結構細節。' },
  { title: '營造發包監理', desc: '公正透明的發包流程，並派駐專業監工，嚴格把關工程品質與用料。' },
  { title: '行銷與售後服務', desc: '結合品牌美學進行銷售規劃，並提供長期的建物保固與管線維護諮詢。' }
]

useHead({
  title: '全案管理 PCM - 傑丞建築機構'
})
</script>

<style scoped>
.elegant-transition {
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes slow-zoom {
  from { transform: scale(1); }
  to { transform: scale(1.1); }
}

.animate-slow-zoom {
  animation: slow-zoom 20s linear infinite alternate;
}

.animate-fade-in-up {
  opacity: 0;
  animation: fade-in-up 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.text-emerald-brand-light {
  color: #10b981;
}
</style>