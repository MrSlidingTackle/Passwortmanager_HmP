<template>
    <a href="/" class="absolute pl-5 pt-3"><-Zurück</a>
    <div class="w-full h-1/12 text-4xl items-center justify-center flex">
        <p>Youtube</p>
    </div>

        <!-- Show loading spinner while fetching data -->
    <div v-if="isLoading" class="text-center">
        <p>Loading...</p>
    </div>

    <!-- Show error message if there’s an error -->
    <div v-if="error" class="text-center text-red-500">
        <p>Error loading data: {{ error.message }}</p>
    </div>

    <!-- Show the data once it's fetched -->
    <div v-if="item" class="w-full h-9/12 flex items-center justify-center">
        <div class="h-full w-1/2 bg-[#00026B] rounded-xl p-6 text-xl">
            <div class="w-full h-1/6 flex flex-row">
                <div class="w-1/2 flex items-center justify-center">
                    <label for="username">Username:</label>
                </div>
                <div class="w-1/2 flex items-center justify-center">
                    <input type="text" readonly id="username" v-model="item.username" class="bg-white text-black">
                </div>
            </div>
            <div class="w-full h-1/6 flex flex-row">
                <div class="w-1/2 flex items-center justify-center">
                    <label for="username">URL:</label>
                </div>
                <div class="w-1/2 flex items-center justify-center">
                    <input type="text" readonly id="url" v-model="item.url" class="bg-white text-black">
                </div>
            </div>
            <div class="w-full h-1/6 flex flex-row">
                <div class="w-1/2 flex items-center justify-center">
                    <label for="username">Name:</label>
                </div>
                <div class="w-1/2 flex items-center justify-center">
                    <input type="text" readonly id="name" v-model="item.name" class="bg-white text-black">
                </div>
            </div>
            <div class="w-full h-1/6 flex flex-row">
                <div class="w-1/2 flex items-center justify-center">
                    <label for="username">Passwort:</label>
                </div>
                <div class="w-1/2 flex items-center justify-center">
                    <input type="text" readonly id="passwort" v-model="item.passwort" class="bg-white text-black">
                </div>
            </div>
            <div class="w-full h-1/6 flex flex-row">
                <div class="w-1/2 flex items-center justify-center">
                    <label for="username">Farbe:</label>
                </div>
                <div class="w-1/2 flex items-center justify-center">
                    <input type="text" readonly id="farbe" v-model="item.farbe" class="bg-white text-black">
                </div>
            </div>
            <div class="w-full h-1/6 flex flex-row">
                <div class="w-1/2 flex items-center justify-center">
                    <label for="username">Erstellt am:</label>
                </div>
                <div class="w-1/2 flex items-center justify-center">
                    <input type="text" readonly id="created" v-model="item.created" class="bg-white text-black">
                </div>
            </div>
        </div>
    </div>

    <div class="w-full h-2/12 flex items-center justify-center">
        <div class="w-1/2 h-full flex items-center justify-center">
            <button class="w-3/4 h-1/3 bg-gray-500 rounded-xl transition-all hover:cursor-pointer hover:scale-110">Bearbeiten</button>
        </div>
        <div class="w-1/2 h-full flex items-center justify-center">
            <button class="w-3/4 h-1/3 bg-gray-500 rounded-xl transition-all hover:cursor-pointer hover:scale-110">Löschen</button>
        </div>
    </div>
</template>

<script setup>
    // Import necessary hooks
    import { useRoute } from 'vue-router'
    import { ref, onMounted } from 'vue'
    
    // Access the current route to get the dynamic "id" from the URL
    const route = useRoute()
    let item = ref(null)
    const error = ref(null)  // This will store any error
    const isLoading = ref(true)  // This will show the loading state
    
    // Fetch data when the component is mounted
    onMounted(async () => {
        const id = route.params.id
        try {
            const response = await fetch(`http://localhost:5000/entry/${id}`)
            
            if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`)
            }
            
            item = await response.json()  // Hier wird die JSON-Antwort verarbeitet
        } catch (err) {
            error.value = err
            console.error(err)  // Fehler auch in der Konsole ausgeben
        } finally {
            isLoading.value = false
            console.log(item)
        }
    })
    </script>