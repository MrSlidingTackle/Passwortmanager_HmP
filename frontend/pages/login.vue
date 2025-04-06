<script setup lang="ts">
    definePageMeta({
      layout: 'empty'
    })
</script>

<template>
  <div class="h-screen w-screen bg-[#0B004D] flex justify-center items-center">
    <div class="h-1/3 w-1/3 bg-[#00026B] rounded-xl">
        <div class="w-full h-1/6 text-4xl text-white p-2 text-center underline">
            <p>SG-Passwortmanager</p>
        </div>
        <div class="w-full h-5/6 flex flex-col justify-center items-center p-2">
            <input type="text" placeholder="Username" class="w-5/6 text-2xl bg-white m-4">
            <input type="text" placeholder="Passwort" class="w-5/6 text-2xl bg-white m-4">
            <button type="button" onclick="" class="bg-white rounded-xl px-2 m-4 transition-all hover:cursor-pointer hover:scale-110">Login</button>
            <a href="http://localhost:3000/" class="absolute bottom-80 text-[#1900FF]">Registrieren</a>
        </div>
    </div>
  </div>
</template>
