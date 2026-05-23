<template>
  <div class="bg-warm-white min-h-screen">
    <!-- 區塊1: 頁面標頭 -->
    <section class="pt-24 pb-12">
      <div class="container-custom text-center">
        <span class="font-mono text-emerald-brand text-xs tracking-[0.3em] uppercase mb-4 block animate-fade-in-up">
          Get In Touch
        </span>
        <h1 class="font-serif text-5xl md:text-6xl font-light text-charcoal mb-8 animate-fade-in-up">
          聯絡我們
        </h1>
        <p class="max-w-2xl mx-auto font-sans text-charcoal/60 leading-relaxed animate-fade-in-up" style="animation-delay: 0.2s">
          無論是新的建築計畫、空間改造諮詢，或是媒體採訪邀約，<br class="hidden md:block" />
          我們都期待聆聽您的想法，共同建構理想的空間未來。
        </p>
      </div>
    </section>

    <!-- 區塊2: 聯絡表單與資訊 -->
    <section class="section-spacing">
      <div class="container-custom">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-24 items-start">

          <!-- 左側：聯絡表單 (極簡線條風格) -->
          <div class="animate-fade-in-up" style="animation-delay: 0.4s">
            <form @submit.prevent class="space-y-12">
              <!-- 姓名欄位 -->
              <div class="group relative">
                <label class="block font-mono text-[10px] uppercase tracking-widest text-charcoal/40 mb-2 transition-colors group-focus-within:text-emerald-brand">
                  Full Name
                </label>
                <input
                  type="text"
                  placeholder="您的姓名"
                  class="w-full bg-transparent border-b border-charcoal/10 py-3 focus:outline-none focus:border-emerald-brand transition-colors duration-700 font-sans text-charcoal placeholder:text-charcoal/20"
                >
                <div class="absolute bottom-0 left-0 w-0 h-[1px] bg-emerald-brand transition-all duration-700 elegant-transition group-focus-within:w-full"></div>
              </div>

              <!-- 信箱欄位 -->
              <div class="group relative">
                <label class="block font-mono text-[10px] uppercase tracking-widest text-charcoal/40 mb-2 transition-colors group-focus-within:text-emerald-brand">
                  Email Address
                </label>
                <input
                  type="email"
                  placeholder="email@example.com"
                  class="w-full bg-transparent border-b border-charcoal/10 py-3 focus:outline-none focus:border-emerald-brand transition-colors duration-700 font-sans text-charcoal placeholder:text-charcoal/20"
                >
                <div class="absolute bottom-0 left-0 w-0 h-[1px] bg-emerald-brand transition-all duration-700 elegant-transition group-focus-within:w-full"></div>
              </div>

              <!-- 訊息內容 -->
              <div class="group relative">
                <label class="block font-mono text-[10px] uppercase tracking-widest text-charcoal/40 mb-2 transition-colors group-focus-within:text-emerald-brand">
                  Message
                </label>
                <textarea
                  rows="4"
                  placeholder="請描述您的需求..."
                  class="w-full bg-transparent border-b border-charcoal/10 py-3 focus:outline-none focus:border-emerald-brand transition-colors duration-700 font-sans text-charcoal placeholder:text-charcoal/20 resize-none"
                ></textarea>
                <div class="absolute bottom-0 left-0 w-0 h-[1px] bg-emerald-brand transition-all duration-700 elegant-transition group-focus-within:w-full"></div>
              </div>

              <!-- 送出按鈕 -->
              <button
                type="submit"
                class="group relative inline-flex items-center px-12 py-5 bg-charcoal text-warm-white text-xs tracking-[0.2em] uppercase overflow-hidden transition-all duration-700 hover:bg-emerald-brand"
              >
                <span class="relative z-10">送出訊息</span>
                <div class="absolute inset-0 bg-emerald-brand transform translate-y-full group-hover:translate-y-0 transition-transform duration-700 elegant-transition"></div>
              </button>
            </form>
          </div>

          <!-- 右側：聯繫資訊與地圖 -->
          <div class="animate-fade-in-up" style="animation-delay: 0.6s">
            <div class="space-y-16">
              <!-- 電話與地址 -->
              <div class="space-y-8">
                <div>
                  <h3 class="font-mono text-xs text-emerald-brand tracking-widest uppercase mb-4">Location</h3>
                  <p class="font-serif text-2xl text-charcoal leading-relaxed">
                    桃園市桃園區大興西路一段268號<br />
                    印象羅芙19樓
                  </p>
                </div>
                <div>
                  <h3 class="font-mono text-xs text-emerald-brand tracking-widest uppercase mb-4">Inquiry</h3>
                  <p class="font-serif text-2xl text-charcoal">(02) 2345-6789</p>
                  <p class="font-sans text-charcoal/60 mt-2">info@jieceng-arch.com</p>
                </div>
              </div>

              <!-- 社交媒體 -->
              <div>
                <h3 class="font-mono text-xs text-emerald-brand tracking-widest uppercase mb-6">Social Connect</h3>
                <div class="flex space-x-8">
                  <a href="#" class="text-charcoal/40 hover:text-emerald-brand transition-colors duration-500 font-sans text-sm tracking-widest uppercase">Facebook</a>
                  <a href="#" class="text-charcoal/40 hover:text-emerald-brand transition-colors duration-500 font-sans text-sm tracking-widest uppercase">Instagram</a>
                  <a href="#" class="text-charcoal/40 hover:text-emerald-brand transition-colors duration-500 font-sans text-sm tracking-widest uppercase">LinkedIn</a>
                </div>
              </div>

              <!-- 極簡地圖預留區 -->
              <div class="aspect-video bg-stone-100 grayscale hover:grayscale-0 transition-all duration-1200 elegant-transition border border-stone-200">
                <div class="w-full h-full flex items-center justify-center text-charcoal/20 font-mono text-[10px] tracking-widest uppercase">
                  Interactive Map Integration
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.elegant-transition {
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}

.animate-fade-in-up {
  opacity: 0;
  animation: fade-in-up 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>