<template>
  <div class="bg-warm-white min-h-screen">
    <!-- 區塊1: 沉浸式 Hero -->
    <section class="grain-dark relative h-[45vh] flex items-center overflow-hidden bg-charcoal">
      <div class="absolute inset-0 z-0">
        <img
          src="/image/hero-background.jpg"
          alt="聯絡傑丞建築"
          class="w-full h-full object-cover opacity-35 scale-105 animate-slow-zoom"
          loading="eager" fetchpriority="high" decoding="async"
        >
        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-charcoal/40 to-charcoal/80"></div>
      </div>
      <div class="container-custom relative z-10 text-center">
        <div class="glass-dark rounded-full px-4 py-1.5 inline-block mb-5 animate-fade-in-up">
          <span class="font-mono text-emerald-brand-light text-[10px] tracking-[0.4em] uppercase">Get In Touch</span>
        </div>
        <div class="dim-line dim-line-light w-16 mx-auto mb-6 animate-fade-in-up" style="animation-delay: 0.1s"></div>
        <h1 class="font-serif text-5xl md:text-7xl text-warm-white font-light mb-5 animate-fade-in-up" style="animation-delay: 0.15s">
          聯絡我們
        </h1>
        <p class="max-w-2xl mx-auto font-sans text-warm-white/60 leading-relaxed animate-fade-in-up" style="animation-delay: 0.3s">
          無論是新的建築計畫、空間改造諮詢，或是媒體採訪邀約，我們都期待聆聽您的想法。
        </p>
      </div>
    </section>

    <!-- 區塊2: 聯絡表單與資訊 -->
    <section class="blueprint-grid relative overflow-hidden pt-8 md:pt-12 pb-32 md:pb-40 bg-warm-white">
      <div class="container-custom relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24 items-start">

          <!-- 左側：聯絡表單 -->
          <div class="glass-card relative corner-marks rounded-3xl p-8 md:p-12 animate-fade-in-up" style="animation-delay: 0.4s">
            <form @submit.prevent="submitForm" class="space-y-10">
              <!-- 姓名欄位 -->
              <div class="group relative">
                <label class="block font-mono text-[10px] uppercase tracking-widest text-charcoal/35 mb-2 transition-colors group-focus-within:text-emerald-brand">
                  Full Name
                </label>
                <input
                  v-model="form.name"
                  type="text"
                  placeholder="您的姓名"
                  required
                  class="w-full bg-transparent border-b border-stone-200 py-3 focus:outline-none focus:border-emerald-brand transition-colors duration-700 font-sans text-charcoal placeholder:text-charcoal/20"
                >
                <div
                  class="absolute bottom-0 left-0 w-0 h-[1px] bg-emerald-brand transition-all duration-700 elegant-transition group-focus-within:w-full"
                ></div>
              </div>

              <!-- 信箱欄位 -->
              <div class="group relative">
                <label class="block font-mono text-[10px] uppercase tracking-widest text-charcoal/35 mb-2 transition-colors group-focus-within:text-emerald-brand">
                  Email Address
                </label>
                <input
                  v-model="form.email"
                  type="email"
                  placeholder="email@example.com"
                  required
                  class="w-full bg-transparent border-b border-stone-200 py-3 focus:outline-none focus:border-emerald-brand transition-colors duration-700 font-sans text-charcoal placeholder:text-charcoal/20"
                >
                <div
                  class="absolute bottom-0 left-0 w-0 h-[1px] bg-emerald-brand transition-all duration-700 elegant-transition group-focus-within:w-full"
                ></div>
              </div>

              <!-- 訊息內容 -->
              <div class="group relative">
                <label class="block font-mono text-[10px] uppercase tracking-widest text-charcoal/35 mb-2 transition-colors group-focus-within:text-emerald-brand">
                  Message
                </label>
                <textarea
                  v-model="form.message"
                  rows="4"
                  placeholder="請描述您的需求..."
                  required
                  class="w-full bg-transparent border-b border-stone-200 py-3 focus:outline-none focus:border-emerald-brand transition-colors duration-700 font-sans text-charcoal placeholder:text-charcoal/20 resize-none"
                ></textarea>
                <div
                  class="absolute bottom-0 left-0 w-0 h-[1px] bg-emerald-brand transition-all duration-700 elegant-transition group-focus-within:w-full"
                ></div>
              </div>

              <!-- 送出按鈕 + 狀態回饋 -->
              <div class="space-y-5">
                <button
                  type="submit"
                  :disabled="status === 'loading'"
                  class="group relative inline-flex items-center px-12 py-5 bg-charcoal text-warm-white text-xs tracking-[0.2em] uppercase rounded-full overflow-hidden transition-all duration-700 hover:bg-emerald-brand disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <span class="absolute inset-0 bg-emerald-brand transform translate-y-full group-hover:translate-y-0 transition-transform duration-700 elegant-transition"></span>
                  <span class="relative z-10">
                    {{ status === 'loading' ? '傳送中⋯' : '送出訊息' }}
                  </span>
                </button>
                <Transition name="fade-quick">
                  <p v-if="status === 'success'" class="font-sans text-sm text-emerald-brand tracking-zh">
                    ✓ 訊息已送出，我們將盡快與您聯繫。
                  </p>
                  <p v-else-if="status === 'error'" class="font-sans text-sm text-red-500 tracking-zh">
                    ✗ 傳送失敗，請直接寄信至 jason.house2007@gmail.com
                  </p>
                </Transition>
              </div>
            </form>
          </div>

          <!-- 右側：聯繫資訊與地圖 -->
          <div class="space-y-16 animate-fade-in-up" style="animation-delay: 0.6s">
            <!-- 電話與地址 -->
            <div class="space-y-8">
              <div>
                <h3 class="text-emerald-brand font-mono text-xs tracking-widest uppercase mb-4">Location</h3>
                <p class="font-serif text-2xl text-charcoal leading-relaxed">
                  桃園市桃園區大興西路一段268號<br />
                  印象羅芙19樓
                </p>
              </div>
              <div>
                <h3 class="text-emerald-brand font-mono text-xs tracking-widest uppercase mb-4">Inquiry</h3>
                <p class="font-serif text-2xl text-charcoal">(03) 316-7799</p>
                <a href="mailto:jason.house2007@gmail.com" class="font-sans text-charcoal/55 hover:text-emerald-brand transition-colors duration-500 mt-2 block">jason.house2007@gmail.com</a>
              </div>
            </div>

            <!-- 社交媒體 -->
            <div>
              <h3 class="text-emerald-brand font-mono text-xs tracking-widest uppercase mb-6">Social Connect</h3>
              <div class="flex space-x-8">
                <a href="#" class="text-charcoal/35 hover:text-emerald-brand transition-colors duration-500 font-sans text-sm tracking-widest uppercase">Facebook</a>
                <a href="#" class="text-charcoal/35 hover:text-emerald-brand transition-colors duration-500 font-sans text-sm tracking-widest uppercase">Instagram</a>
                <a href="#" class="text-charcoal/35 hover:text-emerald-brand transition-colors duration-500 font-sans text-sm tracking-widest uppercase">LinkedIn</a>
              </div>
            </div>

            <!-- Google Maps 嵌入 -->
            <div>
              <p class="font-mono text-[9px] tracking-[0.25em] uppercase text-charcoal/30 mb-3">24.9937°N 121.2958°E — Taoyuan</p>
              <div class="glass rounded-2xl overflow-hidden grayscale hover:grayscale-0 transition-all duration-1200 elegant-transition">
                <iframe
                  src="https://www.google.com/maps?q=%E6%A1%83%E5%9C%92%E5%B8%82%E6%A1%83%E5%9C%92%E5%8D%80%E5%A4%A7%E8%88%88%E8%A5%BF%E8%B7%AF%E4%B8%80%E6%AE%B5268%E8%99%9F&output=embed&z=17"
                  width="100%"
                  height="280"
                  style="border:0; display:block;"
                  allowfullscreen
                  loading="lazy"
                  referrerpolicy="no-referrer-when-downgrade"
                  title="傑丞建築機構位置"
                ></iframe>
              </div>
            </div>
            <a
              href="https://maps.app.goo.gl/AYb92M8zd5Rp3KuT9"
              target="_blank"
              rel="noopener"
              class="inline-flex items-center gap-2 text-charcoal/35 hover:text-emerald-brand font-mono text-[11px] tracking-widest uppercase transition-colors duration-500"
            >
              在 Google Maps 開啟 ↗
            </a>
          </div>

        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
// EmailJS 設定（靜態網站直接送信，不需後端）
// 設定步驟：
//   1. 前往 https://emailjs.com 免費註冊
//   2. 新增 Service（連結你的 Gmail）→ 取得 Service ID
//   3. 新增 Email Template，變數使用 {{from_name}} {{from_email}} {{message}}
//   4. 到 Account → API Keys 取得 Public Key
//   5. 將下方三個佔位符換成你的實際值

const EMAILJS_SERVICE_ID  = 'YOUR_SERVICE_ID'   // ← 替換
const EMAILJS_TEMPLATE_ID = 'YOUR_TEMPLATE_ID'  // ← 替換
const EMAILJS_PUBLIC_KEY  = 'YOUR_PUBLIC_KEY'   // ← 替換

useHead({
  script: [{ src: 'https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js', defer: true }]
})

const form = reactive({ name: '', email: '', message: '' })
const status = ref('idle') // 'idle' | 'loading' | 'success' | 'error'

const submitForm = async () => {
  if (status.value === 'loading') return
  status.value = 'loading'
  try {
    // @ts-ignore
    await window.emailjs.send(
      EMAILJS_SERVICE_ID,
      EMAILJS_TEMPLATE_ID,
      { from_name: form.name, from_email: form.email, message: form.message },
      EMAILJS_PUBLIC_KEY
    )
    status.value = 'success'
    form.name = ''
    form.email = ''
    form.message = ''
  } catch {
    status.value = 'error'
  }
}

useSeoMeta({
  title: '聯絡我們 - 傑丞建築機構',
  description: '歡迎聯繫傑丞建築機構，提出您的建築計畫、都更諮詢或媒體採訪邀約。桃園市桃園區大興西路一段268號印象羅芙19樓。',
  ogTitle: '聯絡傑丞建築機構',
  ogDescription: '歡迎聯繫傑丞建築機構，共同規劃您的建築藍圖。',
  ogType: 'website',
  twitterCard: 'summary',
})
</script>

<style scoped>
.fade-quick-enter-active,
.fade-quick-leave-active {
  transition: opacity 0.4s ease;
}
.fade-quick-enter-from,
.fade-quick-leave-to {
  opacity: 0;
}
</style>
