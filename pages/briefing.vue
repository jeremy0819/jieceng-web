<template>
  <div class="bg-warm-white min-h-screen">

    <!-- 區塊1: 暗色 Hero -->
    <section class="grain-dark relative h-[55vh] flex items-end overflow-hidden bg-charcoal">
      <div class="absolute inset-0 z-0">
        <img
          src="/image/hero-background.jpg"
          alt="都更說明會"
          class="w-full h-full object-cover opacity-40 scale-105 animate-slow-zoom"
          loading="eager" fetchpriority="high" decoding="async"
        >
        <div class="absolute inset-0 bg-gradient-to-t from-charcoal/90 via-charcoal/40 to-charcoal/10"></div>
      </div>

      <div class="container-custom relative z-10 pb-16 md:pb-20">
        <div class="max-w-3xl">
          <div class="flex items-center gap-3 mb-5 animate-fade-in-up">
            <span class="glass-dark rounded-full px-4 py-1.5 font-mono text-[10px] text-emerald-brand-light tracking-[0.35em] uppercase">
              Briefing Sessions
            </span>
          </div>
          <div class="dim-line dim-line-light w-20 mb-6 animate-fade-in-up" style="animation-delay: 0.1s"></div>
          <h1 class="font-serif text-5xl md:text-7xl text-warm-white font-light tracking-tight mb-5 animate-fade-in-up" style="animation-delay: 0.15s">
            都更說明會
          </h1>
          <p class="font-sans text-lg text-warm-white/60 max-w-xl leading-relaxed animate-fade-in-up" style="animation-delay: 0.3s">
            傑丞建築機構定期舉辦都市更新說明會，提供地主與居民專業解說，讓每一位參與者都能清楚了解都更權益。
          </p>
        </div>
      </div>
    </section>

    <!-- 區塊2: 即將舉辦 -->
    <section class="section-spacing relative overflow-hidden">
      <span class="sheet-num top-8 right-0" aria-hidden="true">01</span>
      <div class="container-custom relative z-10">
        <div class="flex flex-col md:flex-row justify-between items-start md:items-end mb-16 gap-6">
          <div>
            <span class="font-mono text-emerald-brand text-[10px] uppercase tracking-[0.4em] mb-4 block animate-fade-in-up">
              Upcoming Events
            </span>
            <h2 class="font-serif text-4xl md:text-5xl font-light text-charcoal animate-fade-in-up" style="animation-delay: 0.1s">
              近期說明會場次
            </h2>
          </div>
          <NuxtLink
            to="/contact"
            class="shrink-0 px-8 py-3.5 bg-emerald-brand text-white rounded-full font-mono text-[10px] uppercase tracking-widest hover:bg-emerald-brand/80 transition-all duration-500 animate-fade-in-up"
          >
            預約洽詢
          </NuxtLink>
        </div>

        <div class="space-y-5">
          <div
            v-for="(session, i) in upcomingSessions"
            :key="i"
            class="glass-card rounded-2xl p-6 md:p-8 group glass-lift animate-fade-in-up"
            :style="`animation-delay: ${0.1 + i * 0.08}s`"
          >
            <div class="flex flex-col md:flex-row md:items-center gap-5 md:gap-10">
              <!-- 日期塊 -->
              <div class="shrink-0 glass rounded-xl px-5 py-4 text-center min-w-[80px]">
                <div class="font-mono text-xs text-emerald-brand uppercase tracking-widest mb-1">{{ session.month }}</div>
                <div class="font-serif text-4xl font-light text-charcoal leading-none">{{ session.day }}</div>
                <div class="font-mono text-[10px] text-charcoal/40 mt-1">{{ session.weekday }}</div>
              </div>

              <!-- 詳細資訊 -->
              <div class="flex-1">
                <div class="flex flex-wrap items-center gap-3 mb-3">
                  <span
                    class="font-mono text-[10px] uppercase tracking-wider px-3 py-1 rounded-full"
                    :class="session.type === '都更說明' ? 'bg-emerald-brand/10 text-emerald-brand' : 'bg-stone-100 text-charcoal/50'"
                  >
                    {{ session.type }}
                  </span>
                  <span v-if="session.spots" class="font-mono text-[10px] text-charcoal/40 tracking-wider">
                    剩餘名額 {{ session.spots }} 位
                  </span>
                </div>
                <h3 class="font-serif text-xl md:text-2xl text-charcoal mb-2 tracking-zh group-hover:text-emerald-brand transition-colors duration-500">
                  {{ session.title }}
                </h3>
                <div class="flex flex-wrap gap-x-6 gap-y-1.5 text-sm text-charcoal/50">
                  <span class="flex items-center gap-2">
                    <svg class="w-4 h-4 text-emerald-brand/60" viewBox="0 0 16 16" fill="none">
                      <path d="M8 1.5a4.5 4.5 0 1 0 0 9 4.5 4.5 0 0 0 0-9ZM0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-2a.75.75 0 0 1 .75.75v1.69l.97.97a.75.75 0 1 1-1.06 1.06l-1.25-1.25A.75.75 0 0 1 7.25 8.5v-1.75A.75.75 0 0 1 8 6Z" fill="currentColor"/>
                    </svg>
                    {{ session.time }}
                  </span>
                  <span class="flex items-center gap-2">
                    <svg class="w-4 h-4 text-emerald-brand/60" viewBox="0 0 16 16" fill="none">
                      <path d="M8 0a5.53 5.53 0 0 0-5.5 5.5C2.5 9.5 8 16 8 16s5.5-6.5 5.5-10.5A5.53 5.53 0 0 0 8 0Zm0 7.5a2 2 0 1 1 0-4 2 2 0 0 1 0 4Z" fill="currentColor"/>
                    </svg>
                    {{ session.location }}
                  </span>
                </div>
              </div>

              <!-- 報名按鈕 -->
              <div class="shrink-0">
                <NuxtLink
                  to="/contact"
                  class="inline-flex items-center gap-2 px-6 py-3 ring-1 ring-emerald-brand/30 text-emerald-brand rounded-full font-mono text-[10px] uppercase tracking-widest hover:bg-emerald-brand hover:text-white hover:ring-emerald-brand transition-all duration-500"
                >
                  立即報名
                  <span class="group-hover:translate-x-1 transition-transform duration-500">→</span>
                </NuxtLink>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊3: 重點案件 — 新店安和段 -->
    <section class="section-spacing bg-white border-t border-stone-100">
      <div class="container-custom">
        <div class="grid lg:grid-cols-2 gap-16 lg:gap-24 items-center">
          <div>
            <span class="font-mono text-emerald-brand text-[10px] uppercase tracking-[0.4em] mb-6 block animate-fade-in-up">
              Featured Case
            </span>
            <h2 class="font-serif text-4xl md:text-5xl font-light text-charcoal leading-tight mb-8 animate-fade-in-up" style="animation-delay: 0.1s">
              新店安和段<br />
              <span class="italic text-charcoal/30">都市更新案。</span>
            </h2>
            <div class="space-y-5 font-sans text-base text-charcoal/60 leading-relaxed tracking-zh animate-fade-in-up" style="animation-delay: 0.2s">
              <p>
                本案位於新北市新店區安和段，傑丞建築以全案管理方式協助地主整合都更意願，從法規諮詢、容積試算、設計規劃到施工監理，提供一條龍專業服務。
              </p>
              <p>
                都更說明會讓每位地主清楚了解自身權益、時程規劃與未來房屋規格，是傑丞推動「透明都更」的重要環節。
              </p>
            </div>

            <div class="mt-10 grid grid-cols-2 gap-6 animate-fade-in-up" style="animation-delay: 0.3s">
              <div v-for="kpi in projectKPIs" :key="kpi.label" class="glass-card rounded-xl p-5">
                <div class="font-serif text-3xl text-emerald-brand mb-1.5 font-light" :data-counter="kpi.num" :data-suffix="kpi.suffix">{{ kpi.value }}</div>
                <div class="font-mono text-[10px] uppercase tracking-[0.2em] text-charcoal/40">{{ kpi.label }}</div>
              </div>
            </div>

            <NuxtLink
              to="/project/3"
              class="inline-flex items-center gap-3 mt-10 font-mono text-[10px] uppercase tracking-widest text-charcoal/40 hover:text-emerald-brand transition-colors duration-500 animate-fade-in-up"
              style="animation-delay: 0.4s"
            >
              查看完整建案資料
              <svg class="w-10 h-3" fill="none" stroke="currentColor" viewBox="0 0 40 12">
                <path d="M0 6H38M38 6L33 1M38 6L33 11" stroke-width="1" stroke-linecap="round"/>
              </svg>
            </NuxtLink>
          </div>

          <div class="animate-fade-in-up" style="animation-delay: 0.15s">
            <div class="img-reveal corner-marks relative aspect-[4/3] overflow-hidden rounded-3xl bg-stone-100 shadow-lg ring-1 ring-black/[0.06] group">
              <img
                src="/image/project-3.jpg"
                alt="新店安和段都更案"
                class="w-full h-full object-cover transition-transform duration-1200 elegant-transition group-hover:scale-105"
                loading="lazy" decoding="async"
              >
              <div class="absolute inset-0 bg-gradient-to-t from-charcoal/40 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊4: 說明會流程 -->
    <section class="blueprint-grid section-spacing bg-warm-white border-t border-stone-100">
      <div class="container-custom">
        <div class="text-center mb-16">
          <span class="font-mono text-emerald-brand text-[10px] uppercase tracking-[0.4em] mb-4 block animate-fade-in-up">How It Works</span>
          <h2 class="font-serif text-4xl md:text-5xl font-light text-charcoal animate-fade-in-up" style="animation-delay: 0.1s">說明會流程</h2>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-5">
          <div
            v-for="(step, i) in briefingSteps"
            :key="i"
            class="glass-card rounded-2xl p-6 animate-fade-in-up relative overflow-hidden"
            :style="`animation-delay: ${0.1 + i * 0.1}s`"
          >
            <span class="absolute top-3 right-4 font-mono text-5xl font-light text-emerald-brand/[0.08] leading-none select-none">
              0{{ i + 1 }}
            </span>
            <div class="w-10 h-10 rounded-full bg-emerald-brand/10 flex items-center justify-center mb-5">
              <span class="font-mono text-xs text-emerald-brand font-medium">0{{ i + 1 }}</span>
            </div>
            <h3 class="font-serif text-xl text-charcoal mb-3 tracking-zh">{{ step.title }}</h3>
            <p class="font-sans text-sm text-charcoal/55 leading-relaxed tracking-zh">{{ step.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊5: 都更常見問題 -->
    <section class="section-spacing bg-white border-t border-stone-100">
      <div class="container-custom">
        <div class="max-w-3xl mx-auto">
          <div class="text-center mb-16 animate-fade-in-up">
            <span class="font-mono text-emerald-brand text-[10px] uppercase tracking-[0.4em] mb-4 block">FAQ</span>
            <h2 class="font-serif text-4xl md:text-5xl font-light text-charcoal">都更常見問題</h2>
          </div>
          <div class="space-y-3">
            <div
              v-for="(faq, i) in renewalFaqs"
              :key="i"
              class="glass-card rounded-2xl overflow-hidden animate-fade-in-up"
              :style="`animation-delay: ${i * 0.06}s`"
            >
              <button
                @click="openRenewalFaq = openRenewalFaq === i ? -1 : i"
                class="w-full flex justify-between items-center text-left p-6 group focus:outline-none"
              >
                <span class="font-serif text-lg text-charcoal tracking-zh group-hover:text-emerald-brand transition-colors duration-500 pr-6">
                  {{ faq.q }}
                </span>
                <span class="shrink-0 w-5 h-5 relative transition-transform duration-500 elegant-transition" :class="openRenewalFaq === i ? 'rotate-45' : ''">
                  <span class="absolute top-1/2 left-0 w-full h-[1px] bg-emerald-brand -translate-y-1/2"></span>
                  <span class="absolute left-1/2 top-0 h-full w-[1px] bg-emerald-brand -translate-x-1/2"></span>
                </span>
              </button>
              <div
                class="overflow-hidden transition-all duration-700 elegant-transition"
                :style="{ maxHeight: openRenewalFaq === i ? '300px' : '0px', opacity: openRenewalFaq === i ? 1 : 0 }"
              >
                <p class="font-sans text-charcoal/60 leading-relaxed tracking-zh pb-6 px-6">{{ faq.a }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 區塊6: CTA -->
    <section class="py-24 grain-dark bg-charcoal border-t border-white/5">
      <div class="container-custom text-center">
        <h2 class="font-serif text-3xl md:text-5xl text-warm-white font-light mb-4 animate-fade-in-up">
          想了解您的房屋都更可能性？
        </h2>
        <p class="font-sans text-warm-white/50 mb-10 animate-fade-in-up" style="animation-delay: 0.1s">
          歡迎報名說明會，或直接聯繫我們進行一對一諮詢。
        </p>
        <div class="flex flex-wrap justify-center gap-4 animate-fade-in-up" style="animation-delay: 0.2s">
          <NuxtLink
            to="/contact"
            class="btn-sheen px-10 py-4 bg-warm-white text-charcoal rounded-full font-mono text-xs uppercase tracking-widest hover:bg-emerald-brand hover:text-warm-white transition-all duration-700 elegant-transition"
          >
            免費諮詢
          </NuxtLink>
          <NuxtLink
            to="/portfolio"
            class="px-10 py-4 ring-1 ring-warm-white/30 text-warm-white rounded-full font-mono text-xs uppercase tracking-widest hover:ring-warm-white/60 transition-all duration-700 elegant-transition"
          >
            查看都更案例
          </NuxtLink>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
const upcomingSessions = [
  {
    month: 'JUL',
    day: '19',
    weekday: 'SAT',
    type: '都更說明',
    title: '新店安和段都市更新計畫第三次說明會',
    time: '14:00 – 16:00',
    location: '新北市新店區公所 3F 會議室',
    spots: 12
  },
  {
    month: 'AUG',
    day: '02',
    weekday: 'SAT',
    type: '都更說明',
    title: '安和段都更整合現況報告暨Q&A',
    time: '10:00 – 12:00',
    location: '傑丞建築機構 桃園辦公室',
    spots: 20
  },
  {
    month: 'AUG',
    day: '16',
    weekday: 'SAT',
    type: '新案說明',
    title: 'iHome 5.0 建築工法暨標章成果說明',
    time: '14:00 – 16:30',
    location: '印象羅芙社區 交誼廳',
    spots: null
  },
]

const projectKPIs = [
  { value: '20+', num: 20, suffix: '+', label: 'Years Experience' },
  { value: '6', num: 6, suffix: '', label: 'Green Certifications' },
]

const briefingSteps = [
  { title: '線上報名', desc: '點擊報名按鈕或致電洽詢，填寫基本資料確認場次。' },
  { title: '現場說明', desc: '專業團隊解說都更法規、時程、設計規劃與坪數試算。' },
  { title: 'Q&A 交流', desc: '現場逐一解答地主疑問，並提供個案初步評估。' },
  { title: '後續跟進', desc: '說明會結束後，專人提供書面資料與一對一深度諮詢。' }
]

const openRenewalFaq = ref(-1)
const renewalFaqs = [
  { q: '什麼是都市更新？', a: '都市更新是依據都市計畫，對老舊、危險或環境惡劣的建築進行整合重建。地主可透過重建取得更大坪數、更安全的全新建物，提升資產價值與居住品質。' },
  { q: '參與都更需要多少人同意？', a: '依現行《都市更新條例》，重建實施需取得同一更新單元內土地及建築物所有權人總數及面積的一定比例同意（通常為75%或三分之二），由主管機關審查核定後方可推動。' },
  { q: '都更期間我的房子怎麼辦？', a: '拆遷重建期間，傑丞會協助地主安排過渡租金補貼、搬遷協助，並提供完整時程規劃。全案管理確保每一個階段都有專人溝通，讓地主清楚掌握進度。' },
  { q: '都更後我能拿回多少坪數？', a: '依容積率試算，扣除開發成本後地主通常可取得「原坪數 + 增加坪數」的全新建物。具體比例依地塊位置與法規容積而定，歡迎親洽說明會或聯繫我們進行個案試算。' },
  { q: '傑丞如何確保都更過程透明公正？', a: '傑丞以「透明都更」為核心，所有地主均可參與每次說明會取得完整資訊，財務試算、設計方案與時程均公開呈現，並提供一對一諮詢服務，確保每位地主的權益都得到充分保障。' },
]

useSeoMeta({
  title: '都更說明會 - 傑丞建築機構',
  description: '傑丞建築機構定期舉辦都市更新說明會，提供地主專業諮詢、都更權益解說與建案規劃說明，歡迎報名參加。',
  ogTitle: '都更說明會 | 傑丞建築機構',
  ogDescription: '了解都更權益、掌握最新建案進度，立即報名傑丞說明會。',
  ogType: 'website',
  twitterCard: 'summary',
})
</script>
