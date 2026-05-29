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

    <!-- 區塊1.5: 為什麼需要全案管理 -->
    <section class="section-spacing bg-warm-white border-b border-stone-100">
      <div class="container-custom">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-start">
          <!-- 左：標題 -->
          <div class="lg:col-span-5">
            <span class="font-mono text-emerald-brand text-xs tracking-[0.3em] uppercase mb-4 block animate-fade-in-up">
              Why PCM
            </span>
            <h2 class="font-serif text-4xl md:text-5xl font-light tracking-zh text-charcoal leading-tight animate-fade-in-up" style="animation-delay: 0.1s">
              為什麼需要<br />全案管理？
            </h2>
            <div class="h-[1px] w-24 bg-emerald-brand mt-8 animate-fade-in-up" style="animation-delay: 0.2s"></div>
          </div>

          <!-- 右：說明與痛點解法 -->
          <div class="lg:col-span-7 space-y-12">
            <p class="font-sans text-lg text-charcoal/70 leading-relaxed tracking-zh animate-fade-in-up" style="animation-delay: 0.3s">
              一個建築開發案，往往牽涉地主、建築師、營造廠與銷售等多方角色。資訊不對等與權責不清，正是成本超支與品質失控的主因。全案管理 (PCM) 由單一專業團隊統籌全局，業主只需面對一個窗口，即可掌握從土地評估到交屋售後的每一個環節。
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-10 sm:gap-8">
              <div v-for="(item, i) in whyItems" :key="i" class="animate-fade-in-up" :style="{ animationDelay: `${0.4 + i * 0.1}s` }">
                <h4 class="font-mono text-[10px] tracking-[0.2em] uppercase text-charcoal/40 mb-3">{{ item.label }}</h4>
                <p class="font-serif text-xl text-charcoal mb-2 tracking-zh">{{ item.pain }}</p>
                <p class="font-sans text-sm text-emerald-brand leading-relaxed tracking-zh">{{ item.solution }}</p>
              </div>
            </div>
          </div>
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

    <!-- 區塊3.5: 服務範疇 -->
    <section class="section-spacing bg-white border-t border-stone-100">
      <div class="container-custom">
        <div class="text-center mb-24">
          <span class="font-mono text-emerald-brand text-xs tracking-[0.3em] uppercase mb-4 block animate-fade-in-up">
            Service Scope
          </span>
          <h2 class="font-serif text-4xl md:text-5xl font-light tracking-zh text-charcoal mb-4 animate-fade-in-up">服務範疇</h2>
          <div class="h-[1px] w-12 bg-emerald-brand mx-auto animate-fade-in-up" style="animation-delay: 0.2s"></div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-12 gap-y-16">
          <div v-for="(s, i) in serviceScope" :key="i"
            class="animate-fade-in-up" :style="{ animationDelay: `${i * 0.1}s` }">
            <span class="font-mono text-emerald-brand/50 text-xs tracking-widest">0{{ i + 1 }}</span>
            <h3 class="font-serif text-2xl text-charcoal mt-3 mb-5 tracking-zh">{{ s.title }}</h3>
            <ul class="space-y-2.5">
              <li v-for="item in s.items" :key="item"
                class="font-sans text-sm text-charcoal/60 leading-relaxed tracking-zh flex">
                <span class="text-emerald-brand mr-3 select-none">—</span>{{ item }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊3.6: 常見問題 FAQ -->
    <section class="section-spacing bg-warm-white">
      <div class="container-custom">
        <div class="max-w-3xl mx-auto">
          <div class="text-center mb-20">
            <span class="font-mono text-emerald-brand text-xs tracking-[0.3em] uppercase mb-4 block animate-fade-in-up">
              FAQ
            </span>
            <h2 class="font-serif text-4xl md:text-5xl font-light tracking-zh text-charcoal animate-fade-in-up">常見問題</h2>
          </div>

          <div class="border-t border-stone-200">
            <div v-for="(faq, i) in faqs" :key="i"
              class="border-b border-stone-200 animate-fade-in-up" :style="{ animationDelay: `${i * 0.05}s` }">
              <button
                @click="toggleFaq(i)"
                class="w-full flex justify-between items-center text-left py-8 group focus:outline-none"
                :aria-expanded="openFaq === i"
              >
                <span class="font-serif text-lg md:text-xl text-charcoal tracking-zh group-hover:text-emerald-brand transition-colors duration-500 pr-8">
                  {{ faq.q }}
                </span>
                <span
                  class="shrink-0 w-5 h-5 relative transition-transform duration-500 elegant-transition"
                  :class="openFaq === i ? 'rotate-45' : ''"
                >
                  <span class="absolute top-1/2 left-0 w-full h-[1px] bg-emerald-brand -translate-y-1/2"></span>
                  <span class="absolute left-1/2 top-0 h-full w-[1px] bg-emerald-brand -translate-x-1/2"></span>
                </span>
              </button>
              <div
                class="overflow-hidden transition-all duration-700 elegant-transition"
                :style="{ maxHeight: openFaq === i ? '400px' : '0px', opacity: openFaq === i ? 1 : 0 }"
              >
                <p class="font-sans text-charcoal/60 leading-relaxed tracking-zh pb-8 pr-4 md:pr-12">
                  {{ faq.a }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊4.5: 全案管理案例 -->
    <section class="section-spacing bg-white border-t border-stone-100">
      <div class="container-custom">
        <div class="text-center mb-16 md:mb-24">
          <span class="font-mono text-emerald-brand text-xs tracking-[0.3em] uppercase mb-5 block animate-fade-in-up">Cases</span>
          <h2 class="font-serif text-4xl md:text-5xl font-light tracking-zh text-charcoal mb-6 animate-fade-in-up">
            全案管理案例
          </h2>
          <div class="h-[1px] w-12 bg-emerald-brand mx-auto animate-fade-in-up"></div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8">
          <NuxtLink
            v-for="(project, index) in projects"
            :key="project.id"
            :to="`/project/${project.id}`"
            class="group relative block overflow-hidden rounded-3xl bg-charcoal aspect-[4/3] animate-fade-in-up shadow-sm"
            :style="`animation-delay: ${0.1 + index * 0.1}s`"
          >
            <img
              :src="project.image"
              :alt="project.title"
              class="absolute inset-0 w-full h-full object-cover transition-transform duration-1200 elegant-transition group-hover:scale-105"
            >
            <div class="absolute inset-0 bg-gradient-to-t from-charcoal/85 via-charcoal/20 to-transparent"></div>
            <div class="absolute top-7 left-7">
              <span class="font-mono text-[11px] tracking-[0.2em] uppercase text-warm-white/70">
                {{ project.categoryLabel }} · {{ project.year }}
              </span>
            </div>
            <div class="absolute bottom-0 left-0 right-0 p-8 md:p-10">
              <h3 class="font-serif text-3xl md:text-4xl font-light text-warm-white mb-3 tracking-zh">
                {{ project.title }}
              </h3>
              <p class="font-sans text-sm md:text-base text-warm-white/70 leading-relaxed max-w-md mb-5 line-clamp-2">
                {{ project.description }}
              </p>
              <span class="inline-flex items-center gap-2 text-warm-white text-xs tracking-[0.15em] uppercase">
                了解更多
                <span class="transition-transform duration-500 group-hover:translate-x-1.5">→</span>
              </span>
            </div>
          </NuxtLink>
        </div>

        <div class="mt-16 text-center">
          <NuxtLink
            to="/portfolio"
            class="inline-flex items-center gap-3 px-12 py-5 bg-charcoal text-warm-white text-xs tracking-[0.2em] uppercase rounded-full hover:bg-emerald-brand transition-colors duration-700 elegant-transition"
          >
            查看全部案例
          </NuxtLink>
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

const whyItems = [
  { label: 'Cost / 成本', pain: '預算屢屢超支', solution: '全程概算與採購控管，從源頭杜絕追加。' },
  { label: 'Quality / 品質', pain: '工程品質難把關', solution: '專業監理派駐工地，嚴格管控用料與工序。' },
  { label: 'Responsibility / 權責', pain: '出問題互踢皮球', solution: '單一窗口統籌，權責清晰、責任到位。' }
]

const serviceScope = [
  { title: '可行性評估', items: ['基地與區位分析', '法規與容積檢索', '開發財務試算'] },
  { title: '規劃設計整合', items: ['建築師媒合與管理', '設計圖說審查', '管線與結構優化'] },
  { title: '發包採購管理', items: ['廠商評選與議價', '合約條件擬定', '成本與變更控管'] },
  { title: '施工營造監理', items: ['工程品質查驗', '施工進度追蹤', '工地安全衛生'] },
  { title: '完工驗收交付', items: ['竣工驗收與點交', '保固條件確認', '建物履歷建檔'] },
  { title: '售後資產維護', items: ['管線維修諮詢', '長期保固服務', '資產價值管理'] }
]

const faqs = [
  { q: '全案管理和直接找建築師、營造廠有什麼不同？', a: '建築師負責設計、營造廠負責施工，但兩者之間的協調、成本控管與進度整合往往無人統籌。全案管理 (PCM) 站在業主立場統籌全局，確保各方目標一致、權責清晰。' },
  { q: '全案管理的收費方式為何？', a: '通常以開發案總造價的一定比例計費，或依專案規模採固定顧問費。我們會在評估階段提供透明的報價與服務範疇，絕無隱藏費用。' },
  { q: '哪些類型的業主適合導入全案管理？', a: '無論是個人地主、危老重建、都市更新，或企業自地開發，只要您希望降低開發風險、確保品質與成本，皆適合導入全案管理。' },
  { q: '應該在什麼時間點導入全案管理？', a: '越早越好。在土地評估與規劃初期就介入，能在源頭優化財務與設計決策，效益遠大於施工階段才補救。' },
  { q: '傑丞的專利工法能帶來什麼價值？', a: '當層配管、複層樓板等專利工法，從結構源頭解決傳統建築漏水、噪音與維修困難的痛點，大幅延長建物壽命並提升資產轉手價值。' }
]

const { projects } = useProjects()

const openFaq = ref(0)
const toggleFaq = (i) => {
  openFaq.value = openFaq.value === i ? -1 : i
}

useHead({
  title: '全案管理 PCM - 傑丞建築機構'
})
</script>

