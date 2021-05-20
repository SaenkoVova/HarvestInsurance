<template>
  <v-container>
    <v-tabs class="mb-1">
      <v-tab>Активні поліси</v-tab>
      <v-tab>Архів</v-tab>
    </v-tabs>
    <div>
      <v-card class="mb-5 pa-5 d-flex align-center"
              elevation="24"
              v-for="item in orders.filter(i => i.status === 0)" :key="item.id"
      >

        <div>
          <router-link style="color: #fff; text-decoration: none" :to="`field-state/${item.id}`" class="display-1">Страховий поліс ({{ item.cadastralNumber }})</router-link>
          <p class="subtitle-2">{{item.startDate}} - {{getLastDate(item.startDate, item.term)}}</p>
          <p>Стан страховки: активна</p>
        </div>
        <v-spacer></v-spacer>
        <div>
          <v-btn large block color="primary" class="mb-2" :to="`/field-state/${item.id}`">Переглянути стан поля</v-btn>
          <v-btn large block color="primary">Переглянути договір</v-btn>
        </div>
      </v-card>
    </div>

  </v-container>
</template>

<script>
import http from "../util/http";

export default {
  name: 'Dashboard',
  data: () => ({
    orders: []
  }),
  methods: {
    loadOrders() {
      http.get('loadUserOrders/', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`
        }
      })
        .then(res => {
          this.orders = res.data
        })
    },
    getLastDate(startDate, term) {
      startDate = new Date(startDate)
      startDate.setDate(startDate.getDate() + term)
      return `${startDate.getFullYear()}-${startDate.getMonth()}-${startDate.getDay()}`
    }
  },
  mounted() {
    this.loadOrders();
  }
}
</script>
