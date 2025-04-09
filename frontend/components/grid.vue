<template>
  <div class="grid grid-cols-3 gap-4 overflow-x-hidden overflow-y-visible p-5">
    <a v-for="(item, index) in items" :href="`/details/${item.id}`" :key="index" class="grid-item flex items-center justify-center mt-3 text-2xl text-white transition-all hover:scale-110" :style="{ backgroundColor: item.farbe }">
      {{ item.name }}
    </a>
  </div>
</template>

<script setup>
defineProps({
  items: {
    type: Array,
    required: true
  }
})
</script>

<style scoped>
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.grid-item {
  height: 150px;
  padding: 16px;
  border: 1px solid #ccc;
  border-radius: 8px;
}
</style>