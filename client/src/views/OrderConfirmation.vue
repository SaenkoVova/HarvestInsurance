<template>
  <v-container>
    <h1 class="display-1 text-center font-weight-light mb-2">Перевірте дані та перейдіть до оплати</h1>
    <v-card
        :elevation="2"
        class="pa-5"
    >
      <p class="font-weight-bold">Страхувальник</p>
      <v-simple-table>
        <template v-slot:default>
          <tbody>
          <tr>
            <td>Повне ім'я</td>
            <td>Саєнко Володимир Володимирович</td>
          </tr>
          <tr>
            <td>Дата рождения</td>
            <td>08.05.2000</td>
          </tr>
          <tr>
            <td>Телефон</td>
            <td>0674470622</td>
          </tr>
          <tr>
            <td>Електронна пошта</td>
            <td>vova080520@gmail.com</td>
          </tr>
          </tbody>
        </template>
      </v-simple-table>
      <p class="font-weight-bold">Документ</p>
      <v-simple-table>
        <template v-slot:default>
          <tbody>
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
          <span class="display-2">1000 грн</span>
        </p>
      </div>
      <div>
        <v-checkbox
            v-model="checkbox"
            :label="`Згодний з обробкою персональних даних і користувацьким договором`"
        ></v-checkbox>
      </div>
      <div>
        <v-btn @click="createOrder">Перейти до оплати</v-btn>
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
      createOrder() {
        let data = {
          order: this.getOrder
        }
        http.post('createPolice/', data, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
          }
        })
          .then(res => {
            console.log(res)
          })
      }
    }
  }
</script>
