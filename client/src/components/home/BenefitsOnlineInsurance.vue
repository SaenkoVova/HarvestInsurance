<template>
  <v-container class="text-center">
    <h1 class="display-1 ma-8">Переваги онлайн страхування</h1>
    <v-row>
      <v-col>
        <v-card
            elevation="24"
            outlined
            tile
            class="pa-5"
        >
          <div>
            <v-icon :size="100">mdi-account-alert</v-icon>
          </div>
          <div>
            <p class="subtitle-2">Без паперів і візитів до страхових агентів</p>
          </div>
        </v-card>
      </v-col>
      <v-col>
        <v-card
            elevation="24"
            outlined
            tile
            class="pa-5"
        >
          <div>
            <v-icon :size="100">mdi-email-newsletter</v-icon>
          </div>
          <div>
            <p class="subtitle-2">Готовий страховий поліс чурез 5 хвилин у вас на e-mail</p>
          </div>
        </v-card>
      </v-col>
      <v-col>
        <v-card
            elevation="24"
            outlined
            tile
            class="pa-5"
        >
          <div>
            <v-icon :size="100">mdi-police-badge</v-icon>
          </div>
          <div>
            <p class="subtitle-2">Електронний договір є офіційним документом</p>
          </div>
        </v-card>
      </v-col>
      <v-col>
        <v-card
            elevation="24"
            outlined
            tile
            class="pa-5"
        >
          <div>
            <v-icon :size="100">mdi-cash-refund</v-icon>
          </div>
          <div>
            <p class="subtitle-2">100% гарантія поворнення коштів до початку дії полісу</p>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
