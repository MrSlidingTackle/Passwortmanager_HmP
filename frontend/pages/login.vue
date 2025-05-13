<script setup lang="ts">
    definePageMeta({
      layout: 'empty'
    });

    async function register() {
      const fields = document.getElementsByTagName("input")
      let data = {}

      Array.from(fields).forEach(input => {
          // Use the input's ID as the key, value as the value
          if (input.id) {
              data[input.id] = input.value
          }
      })

      try {
            const response = await fetch(`http://141.87.56.75:5000/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            })

            if (!response.ok) {
                throw new Error(`Error: ${response.statusText}`)
            }

            const result = await response.json()
            console.log("Successfully saved:", result)
        } catch (err) {
            console.error("Failed to save data:", err)
        } finally {
            window.location.reload()
        }
    }

    async function login() {
      const fields = document.getElementsByTagName("input")
      let data = {}

      Array.from(fields).forEach(input => {
          // Use the input's ID as the key, value as the value
          if (input.id) {
              data[input.id] = input.value
          }
      })

      try {
          const response = await fetch(`http://141.87.56.75:5000/login/${data.username}/${data.passwort}`, {
            method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
          })

          if (!response.ok) {
              alert("Wrong credentials!")
              throw new Error(`${response.statusText}`)
          }
          const result = await response.json()
          
        window.localStorage.setItem("user", result.id);
        window.localStorage.setItem("admin", result.isAdmin)
        window.location.href="/"

      } catch (err) {
          console.error("Error:", err)
      } finally {
      }
    }
</script>

<template>
  <div class="h-screen w-screen bg-[#0B004D] flex justify-center items-center">
    <div class="h-1/3 w-1/3 bg-[#00026B] rounded-xl">
        <div class="w-full h-1/6 text-4xl text-white p-2 text-center underline">
            <p>SG-Passwortmanager</p>
        </div>
        <div class="w-full h-5/6 flex flex-col justify-center items-center p-2">
            <input type="text" id="username" placeholder="Username" class="w-5/6 text-2xl bg-white m-4">
            <input type="text" id="passwort" placeholder="Passwort" class="w-5/6 text-2xl bg-white m-4">
            <button type="button" @click="login" class="bg-white rounded-xl px-2 m-4 transition-all hover:cursor-pointer hover:scale-110">Login</button>
            <button @click="register" class="absolute bottom-80 text-[#1900FF]">Registrieren</button>
        </div>
    </div>
  </div>
</template>
