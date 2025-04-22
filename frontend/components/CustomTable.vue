<template>
  <table class="table-auto w-full border border-gray-700 text-white">
    <thead class="bg-gray-800">
      <tr>
        <th v-for="(key, index) in headers" :key="index" class="border px-4 py-2 text-left">
          {{ key }}
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(entry, index) in entries" :key="index" class="hover:bg-gray-900">
        <td v-for="(key, jndex) in headers" :key="jndex" class="border px-4 py-2">
          {{ entry[key] }}
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
defineProps({
  headers: {
    type: Array,
    required: true
  },
  entries: {
    type: Array,
    required: true
  }
})
</script>