<script setup>
  onMounted(async () => {
    try{
      if(window.localStorage.getItem("admin") == 1) {
        console.log("basst");
        let aTag = document.createElement('a');
        aTag.href = 'http://localhost:3001/admin';
        aTag.textContent = "(Admin-Panel)";
        document.getElementById("nav").appendChild(aTag);
      }
    }
    catch (err){
      console.error(err)  // Fehler auch in der Konsole ausgeben
    }
  })

  function removeToken(){
    window.localStorage.removeItem("user")
    window.localStorage.removeItem("admin")
  }
</script>

<template>
  <div class="h-screen w-screen bg-[#0B004D] text-white">
    <div id="nav" class="w-full h-[calc(1/15*100%)] bg-[#00026B] flex items-center">
        <p class="text-2xl p-2">SG-Passwortmanager</p>
        <div class="absolute right-0">
            <p class="text-xl p-2">Hallo, Benutzer!
                <a @click="removeToken" href="http://localhost:3001/login">(Logout)</a>
            </p>
        </div>
    </div>
    <div class="w-full h-[calc(14/15*100%)]">
        <NuxtPage />
    </div>
  </div>
</template>