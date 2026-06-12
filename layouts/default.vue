<template>
  <div class="min-h-screen flex flex-col relative bg-warm-white">
    <TheNavbar />
    <main class="flex-grow">
      <slot />
    </main>
    <TheFooter />
  </div>
</template>

<script setup>
const router = useRouter()
router.afterEach(() => {
  if (process.client) {
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
})
</script>
