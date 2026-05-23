<template>
  <div class="min-h-screen flex flex-col relative bg-warm-white selection:bg-emerald-brand selection:text-emerald-brand-soft">
    <!-- 導覽列組件預留位置 -->
    <TheNavbar />

    <!-- 主內容區 -->
    <main class="flex-grow pt-24">
      <slot />
    </main>

    <!-- 頁尾組件預留位置 -->
    <TheFooter />
  </div>
</template>

<script setup>
/**
 * 專業網站工程師註解：
 * 實作自動平滑滾動至頂端
 */
const router = useRouter();

router.afterEach(() => {
  if (process.client) {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }
});
</script>

<style scoped>
/* 佈局專用樣式 */
.min-h-screen {
  display: flex;
  flex-direction: column;
}
</style>