<template>
    <v-date-picker
            v-model="date"
            full-width
            class="mt-4"
    ></v-date-picker>
</template>

<script>
    export default {
        data: () => ({
            date: new Date().toISOString().substr(0, 10),
        }),
    }
</script>
