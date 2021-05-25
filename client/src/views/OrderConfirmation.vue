<template>
  <v-container>
    <h1 class="display-1 text-center font-weight-light mb-2">Перевірте дані та перейдіть до оплати</h1>
    <v-card
        :elevation="2"
        class="pa-5"
    >
      <v-simple-table>
        <template v-slot:default>
          <tbody>
          <tr>
            <td class="font-weight-bold">
              Страхувальник
            </td>
            <td></td>
          </tr>
          <tr>
            <td>Повне ім'я</td>
            <td>{{getOrder.secondName}} {{getOrder.firstName}} {{getOrder.thirdName}}</td>
          </tr>
          <tr>
            <td>Дата рождения</td>
            <td>{{getOrder.date}}</td>
          </tr>
          <tr>
            <td>Телефон</td>
            <td>{{ getOrder.phone }}</td>
          </tr>
          <tr>
            <td>Електронна пошта</td>
            <td>{{getOrder.email}}</td>
          </tr>
          <tr>
            <td class="font-weight-bold">Документ</td>
            <td></td>
          </tr>
          <tr>
            <td>ID карта</td>
            <td>000089376</td>
          </tr>
          <tr>
            <td>Дата видачі</td>
            <td>18.06.2016</td>
          </tr>
          <tr>
            <td>Ким виданий</td>
            <td>6812</td>
          </tr>
          </tbody>
        </template>
      </v-simple-table>
      <div>
        <p>
          <span class="display-1">До сплати: </span>
          <span class="display-2">{{ getOrder.price }} грн</span>
        </p>
      </div>
      <div>
        <v-checkbox
            v-model="checkbox"
            :label="`Згодний з обробкою персональних даних і користувацьким договором`"
        ></v-checkbox>
      </div>
      <div>
        <v-btn @click="getPaymentPage">Перейти до оплати</v-btn>
      </div>
    </v-card>
  </v-container>
</template>

<script>
  import http from "../util/http";
  import {mapGetters} from "vuex";

  export default {
    name: 'OrderConfirmation',
    data: () => ({
      checkbox: true
    }),
    computed: {
      ...mapGetters({
        getOrder: 'order/getOrder'
      })
    },
    methods: {
      getPaymentPage() {
        http.post('https://pay.fondy.eu/api/checkout/redirect/', {
          response_url: "https://pay.fondy.eu/responsepage/",
          order_id: "test8037875286",
          order_desc: "Test payment",
          currency: "RUB",
          amount: "100",
          signature: "07bc309047a56275f8d89ae222e2af0ceb94fe79",
          merchant_id: "1"
        })
      }
      // createOrder() {
      //   let data = {
      //     order: this.getOrder
      //   }
      //   http.post('createPolice/', data, {
      //     headers: {
      //       Authorization: `Bearer ${localStorage.getItem('token')}`
      //     }
      //   })
      //     .then(res => {
      //       console.log(res)
      //     })
      // }
    }
  }
</script>

<style>
 td {
   padding: 10px!important;
 }
</style>
