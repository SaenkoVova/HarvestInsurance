<template>
  <v-container>
    <v-tabs class="mb-1">
      <v-tab>Активні поліси</v-tab>
      <v-tab>Архів</v-tab>
    </v-tabs>
    <v-card class="mb-5 pa-5 d-flex align-center"
            elevation="24"
    >

      <div>
        <h1 class="display-1">Страховий поліс (6810500000:02:003:1385)</h1>
        <p class="subtitle-2">28.04.2021 - 28.04.2022</p>
        <p>Стан страховки: активна</p>
      </div>
      <v-spacer></v-spacer>
      <div>
        <v-btn large block color="primary" class="mb-2" :to="`/field-state/${1}`">Переглянути стан поля</v-btn>
        <v-btn large block color="primary">Переглянути договір</v-btn>
      </div>
    </v-card>

  </v-container>
</template>

<script>
export default {
  name: 'Dashboard'
}
</script>
