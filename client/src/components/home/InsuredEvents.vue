<template>
  <v-container class="text-center">
    <h1 class="display-1 ma-8">Що покриває страховка</h1>
    <v-row>
      <v-col>
        <v-card
            elevation="24"
            outlined
            tile
            class="pa-5"
        >
          <div>
            <v-icon :size="100">mdi-snowflake</v-icon>
          </div>
          <div>
            <p class="subtitle-2">Заморозки, ожеледь, вимерзання</p>
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
            <v-icon :size="100">mdi-weather-hail</v-icon>
          </div>
          <div>
            <p class="subtitle-2">Град</p>
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
            <v-icon :size="100">mdi-earth</v-icon>
          </div>
          <div>
            <p class="subtitle-2">Землетрус</p>
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
            <v-icon :size="100">mdi-fire</v-icon>
          </div>
          <div>
            <p class="subtitle-2">пожежа, крім лісових пожеж</p>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
