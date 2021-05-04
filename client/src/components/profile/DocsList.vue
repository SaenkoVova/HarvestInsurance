<template>
  <v-container>
    <v-card v-if="getUkrainePassport"
        outlined
        class="ma-5"
    >
      <v-list-item three-line>
        <v-list-item-content>
          <v-list-item-title class="headline mb-1">
            Паспорт громадянина України
          </v-list-item-title>
          <v-list-item-subtitle>Коли виданий: {{getUkrainePassport.passport_issue}}</v-list-item-subtitle>
          <v-list-item-subtitle>Серія і номер: {{getUkrainePassport.series_and_number}}</v-list-item-subtitle>
          <v-list-item-subtitle>Ким виданий: {{getUkrainePassport.issued_by}}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-card-actions>
        <v-btn
            @click="deleteDocument('ukraine_passport')"
            outlined
            rounded
            text
        >
          Видалити
        </v-btn>
      </v-card-actions>
    </v-card>


    <v-card v-if="getForeignPassport"
            outlined
            class="ma-5"
    >
      <v-list-item three-line>
        <v-list-item-content>
          <v-list-item-title class="headline mb-1">
            Закордонний паспорт громадянина України
          </v-list-item-title>
          <v-list-item-subtitle>Коли виданий: {{getUkrainePassport.passport_issue}}</v-list-item-subtitle>
          <v-list-item-subtitle>Серія і номер: {{getUkrainePassport.series_and_number}}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-card-actions>
        <v-btn
            @click="deleteDocument('foreign_passport')"
            outlined
            rounded
            text
        >
          Видалити
        </v-btn>
      </v-card-actions>
    </v-card>


    <v-card v-if="idCard"
            outlined
            class="ma-5"
    >
      <v-list-item three-line>
        <v-list-item-content>
          <v-list-item-title class="headline mb-1">
            ID картка
          </v-list-item-title>
          <v-list-item-subtitle>Коли виданий: {{getUkrainePassport.passport_issue}}</v-list-item-subtitle>
          <v-list-item-subtitle>Ким виданий: {{getUkrainePassport.issued_by}}</v-list-item-subtitle>
          <v-list-item-subtitle>Номер: {{getUkrainePassport.number}}</v-list-item-subtitle>
          <v-list-item-subtitle>Примітки: {{getUkrainePassport.notation}}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-card-actions>
        <v-btn
            outlined
            rounded
            text
            @click="deleteDocument('id_card')"
        >
          Видалити
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>


<script>
import {mapActions, mapGetters} from "vuex";
  import http from "../../util/http";

  export default {
    computed: {
      ...mapGetters({
        getDocs: 'user/getDocs'
      }),
      getUkrainePassport() {
        return this.getDocs.filter(i => i.type === 'ukraine_passport')[0]
      },
      getForeignPassport() {
        return this.getDocs.filter(i => i.type === 'foreign_passport')[0]
      },
      idCard() {
        return this.getDocs.filter(i => i.type === 'id_card')[0]
      }
    },
    methods: {
      ...mapActions({
        loadUserDocs: 'user/loadUserDocs'
      }),
      deleteDocument(type) {
        let token = localStorage.getItem('token')
        http.get('deleteDocument/', {
          headers: {
            Authorization: `Bearer ${token}`
          },
          params: {
            document: type
          }
        })
          .then(() => {
            this.loadUserDocs()
          })
      }
    }
  }
</script>
