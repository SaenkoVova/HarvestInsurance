<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <h1 class="title mx-5">Змінити дані</h1>
        <v-form v-model="valid" @submit.prevent="changeUserInfo">
          <v-container>
            <v-text-field
                v-model="name"
                :rules="[rules.required, rules.counter]"
                label="Ім'я"
                counter
                maxlength="20"
            ></v-text-field>

            <v-text-field
                v-model="secondName"
                :rules="[rules.required, rules.counter]"
                label="Прізвище"
                counter
                maxlength="20"
            ></v-text-field>
            <v-text-field
                v-model="thirdName"
                :rules="[rules.required, rules.counter]"
                label="По батькові"
                counter
                maxlength="20"
            ></v-text-field>
            <v-text-field
                v-model="phone"
                :rules="[rules.required, rules.counter]"
                label="Телефон"
                counter
                maxlength="10"
            ></v-text-field>
            <v-menu
                ref="menu"
                v-model="menu"
                :close-on-content-click="false"
                transition="scale-transition"
                offset-y
                min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                    v-model="birthDate"
                    label="Дата народження"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                    :rules="[rules.required]"
                ></v-text-field>
              </template>
              <v-date-picker
                  ref="picker"
                  v-model="birthDate"
                  :max="new Date().toISOString().substr(0, 10)"
                  min="1950-01-01"
                  @change="save"
              ></v-date-picker>
            </v-menu>
            <v-text-field
                type="password"
                v-model="newPassword"
                :rules="repeatPassword ? [rules.required] : []"
                label="Новий пароль"
            ></v-text-field>
            <v-text-field
                type="password"
                v-model="repeatPassword"
                :rules="newPassword ? [rules.required] : []"
                label="Повторіть новий пароль"
            ></v-text-field>
            <v-text-field
                v-model="password"
                type="password"
                :rules="[rules.required]"
                label="Пароль"
            ></v-text-field>
            <v-btn type="submit" block color="primary" large :disabled="!valid">Змінити данні</v-btn>
            <v-snackbar
                v-model="snackbar"
                :timeout="timeout"
            >
              {{ error }}

              <template v-slot:action="{ attrs }">
                <v-btn
                    color="blue"
                    text
                    v-bind="attrs"
                    @click="snackbar = false"
                >
                  Закрити
                </v-btn>
              </template>
            </v-snackbar>
          </v-container>
        </v-form>
      </v-col>
      <v-col>
        <h1 class="title mx-5 mb-5">Додати документи</h1>
        <doc-tabs ref="docTabs"></doc-tabs>
        <v-btn
            large
            block
            color="primary"
            dark
            @click="uploadDocument"
        >
          Додати документ
          <v-icon
              right
              dark
          >
            mdi-cloud-upload
          </v-icon>
        </v-btn>
        <h1 class="title mx-5 mb-5 mt-5">Ваші документи</h1>
        <docs-list></docs-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import {mapActions, mapGetters} from "vuex";
import http from "../util/http";
import DocTabs from "../components/order/DocTabs";
import DocsList from "../components/profile/DocsList";

export default {
  name: 'Profile',
  components: {DocsList, DocTabs},
  data: () => ({
    valid: false,
    secondName: '',
    thirdName: '',
    birthDate: '',
    password: '',
    repeatPassword: '',
    newPassword: '',
    name: '',
    phone: '',
    menu: false,
    snackbar: false,
    error: null,
    timeout: 2000,
    rules: {
      required: value => !!value || 'Це поле обов\'язкове.',
      counter: value => value.length <= 20 || 'Максимальна довжина 20 символів'
    },
  }),
  watch: {
    menu (val) {
      val && setTimeout(() => (this.$refs.picker.activePicker = 'YEAR'))
    },
    getUser() {
      this.initialize()
    }
  },
  computed: {
    ...mapGetters({
      getUser: 'user/getUser'
    })
  },
  methods: {
    ...mapActions({
      loadUserInfo: 'user/loadUserInfo',
      loadUserDocs: 'user/loadUserDocs'
    }),
    save (date) {
      this.$refs.menu.save(date)
    },
    uploadDocument() {
      const doc = {
        doc: {
          passport_issue: this.$refs.docTabs.issueDate,
          series_and_number: this.$refs.docTabs.seriesAndNumber,
          issued_by: this.$refs.docTabs.issuedBy,
          number: this.$refs.docTabs.number,
          note: this.$refs.docTabs.note
        },
        tab: this.$refs.docTabs.currentTab
      }
      http.post('uploadDocument/', doc, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`
        }
      })
        .then(() => {
          this.loadUserDocs();
        })
    },
    changeUserInfo() {
      if(this.newPassword !== this.repeatPassword) {
        this.snackbar = true;
        this.error = 'Паролі не співпадають'
        return
      }
      const user = {
        user: {
          first_name: this.name,
          second_name: this.secondName,
          third_name: this.thirdName,
          phone: this.phone,
          birth_date: this.birthDate,
          password: this.password,
          new_password: this.newPassword
        }
      }
      http.patch(`user`, user, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`
        }
      })
        .then(() => {
          this.loadUserInfo()
        })
    },
    initialize() {
      this.name = this.getUser.firstName
      this.secondName = this.getUser.secondName
      this.thirdName = this.getUser.thirdName
      this.birthDate = this.getUser.birthDate
      this.phone = this.getUser.phone
    },
    isEmpty(obj) {
      for(let prop in obj) {
        return false;
      }
      return true
    }
  },
  mounted() {
    this.loadUserInfo()
  }
}
</script>
