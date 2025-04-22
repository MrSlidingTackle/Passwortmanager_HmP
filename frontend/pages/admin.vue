<template>
    <div v-if="users" class="w-full h-full">
        <a href="/" class="pl-5 pt-3"><-Zurück</a>
        <CustomTable :headers="['id', 'user', 'passwort', 'isAdmin']" :entries="users" />
        <CustomTable class="mt-5" :headers="['id', 'name', 'url', 'username', 'passwort', 'farbe', 'created', 'ownerId']" :entries="items" />
    </div>
</template>

<script setup>
    let users = ref(null)
    let items = ref(null)

    onMounted(async () => {
        try {
            const response = await fetch(`http://localhost:5000/login`)
            
            if (!response.ok) {
                throw new Error(`Error: ${response.statusText}`)
            }
            
            users.value = await response.json()  // Hier wird die JSON-Antwort verarbeitet

            const otherResponse = await fetch(`http://localhost:5000/entry`)
            
            if (!otherResponse.ok) {
                throw new Error(`Error: ${otherResponse.statusText}`)
            }
            
            items.value = await otherResponse.json()  // Hier wird die JSON-Antwort verarbeitet
            console.log(items)
        }
        catch (err) {
            console.error("Failed to save data:", err)
        }
    })
</script>