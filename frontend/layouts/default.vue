<template>
  <div class="h-screen w-screen bg-[#0B004D] text-white">
    <div class="w-full h-[calc(1/15*100%)] bg-[#00026B] flex items-center">
        <p class="text-2xl p-2">SG-Passwortmanager</p>
        <div class="absolute right-0">
            <p class="text-xl p-2">Hallo, Benutzer!
                <a href="">(Logout)</a>
            </p>
        </div>
    </div>
    <div class="w-full h-[calc(14/15*100%)]">
        <NuxtPage />
    </div>
  </div>
</template>