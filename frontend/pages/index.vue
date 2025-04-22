<template>
  <div class="w-full h-1/12 text-4xl items-center justify-center flex">
    <p>Deine Accountdaten</p>
  </div>
  <div v-if="itemList" class="w-full h-10/12 overflow-y-scroll">
    <grid :items="itemList" />
  </div>
  <div class="w-full h-1/12 flex justify-center">
    <div>
      <dialog class="centered-dialog rounded-xl">
        <div class="h-[600px] w-[800px] bg-[#00026B] rounded-xl p-6 text-xl text-white">
          <div class="w-full h-1/7 flex flex-row">
              <div class="w-1/2 flex items-center justify-center">
                  <label for="username">Username:</label>
              </div>
              <div class="w-1/2 flex items-center justify-center">
                  <input type="text" id="username" class="bg-white text-black">
              </div>
          </div>
          <div class="w-full h-1/7 flex flex-row">
              <div class="w-1/2 flex items-center justify-center">
                  <label for="username">URL:</label>
              </div>
              <div class="w-1/2 flex items-center justify-center">
                  <input type="text" id="url" class="bg-white text-black">
              </div>
          </div>
          <div class="w-full h-1/7 flex flex-row">
              <div class="w-1/2 flex items-center justify-center">
                  <label for="username">Name:</label>
              </div>
              <div class="w-1/2 flex items-center justify-center">
                  <input type="text" id="name" class="bg-white text-black">
              </div>
          </div>
          <div class="w-full h-1/7 flex flex-row">
              <div class="w-1/2 flex items-center justify-center">
                  <label for="username">Passwort:</label>
              </div>
              <div class="w-1/2 flex items-center justify-center">
                  <input type="text" id="passwort" class="bg-white text-black">
              </div>
          </div>
          <div class="w-full h-1/7 flex flex-row">
              <div class="w-1/2 flex items-center justify-center">
                  <label for="username">Farbe:</label>
              </div>
              <div class="w-1/2 flex items-center justify-center">
                  <input type="text" id="farbe" class="bg-white text-black">
              </div>
          </div>
          <div class="w-full h-1/7 flex flex-row">
              <div class="w-1/2 flex items-center justify-center">
                  <label for="username">Erstellt am:</label>
              </div>
              <div class="w-1/2 flex items-center justify-center">
                  <input type="text" id="created" class="bg-white text-black">
              </div>
          </div>
          <div class="w-full h-1/7 flex flex-row">
            <div class="w-1/2 h-full flex items-center justify-center">
              <button id="save" class="h-1/2 w-1/3 bg-gray-500 rounded-xl transition-all hover:scale-110 hover:cursor-pointer">
                Speichern
              </button>
            </div>
            <div class="w-1/2 h-full flex items-center justify-center">
              <button id="closeDialog" class="h-1/2 w-1/3 bg-gray-500 rounded-xl transition-all hover:scale-110 hover:cursor-pointer">
                Abbrechen
              </button>
            </div>
          </div>
      </div>
      </dialog>
      <button id="showDialog" class="bg-gray-400 p-2 mt-2 rounded-lg text-black w-[500px] transition-all hover:scale-110 hover:cursor-pointer">
        Neuer Eintrag
      </button>
    </div>
  </div>
</template>

<script setup>
  import grid from '~/components/grid.vue'
  
  let itemList = ref(null)
  let showButton = null
  let closeButton = null
  let dialog = null
  let save = null;

  async function saveNew() {
        const fields = document.getElementsByTagName("input")
        const data = {}

        Array.from(fields).forEach(input => {
            // Use the input's ID as the key, value as the value
            if (input.id) {
                data[input.id] = input.value
            }
        })
        data['ownerId'] = parseInt(window.localStorage.getItem("user"));

        try {
            const response = await fetch(`http://localhost:5000/entry`, {
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
    };

  onMounted(async () => {
    try {
            let tokenUser = window.localStorage.getItem("user");
            let tokenAdmin = window.localStorage.getItem("admin")

            if(!tokenUser || !tokenAdmin) {
              window.location.href="http://localhost:3001/login"
            }

            showButton = document.querySelector("dialog + button")
            dialog = document.querySelector("dialog")
            closeButton = document.getElementById("closeDialog")
            save = document.getElementById("save")

            const response = await fetch(`http://localhost:5000/entry`)
            
            if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`)
            }
            
            itemList.value = await response.json()  // Hier wird die JSON-Antwort verarbeitet
        } catch (err) {
            error.value = err
            console.error(err)  // Fehler auch in der Konsole ausgeben
        } finally {
            showButton.addEventListener("click", () => {
              dialog.showModal();
            });

            closeButton.addEventListener("click", () => {
              dialog.close();
            });

            save.addEventListener("click", () => {
              saveNew();
            })
        }
  });


  </script>

<style scoped>
  .centered-dialog {
    
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    z-index: 1000; /* Ensure it's above other content */
  }
  </style>