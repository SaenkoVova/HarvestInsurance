<template>
  <v-container fluid>
    <v-form v-model="valid" @submit.prevent="register">
      <v-container>
        <v-row>
          <v-col
              cols="12"
              sm="6"
          >
            <v-text-field
                v-model="name"
                :rules="[rules.required, rules.counter]"
                label="Ім'я"
                counter
                maxlength="20"
            ></v-text-field>
          </v-col>

          <v-col
              cols="12"
              sm="6"
          >
            <v-text-field
                v-model="email"
                :rules="[rules.required, rules.email]"
                label="E-mail"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col
              cols="12"
              sm="6"
          >
            <v-text-field
                v-model="secondName"
                :rules="[rules.required, rules.counter]"
                label="Прізвище"
                counter
                maxlength="20"
            ></v-text-field>
          </v-col>

          <v-col
              cols="12"
              sm="6"
          >
            <v-text-field
                v-model="phone"
                :rules="[rules.required, rules.counter]"
                label="Телефон"
                counter
                maxlength="10"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col
              cols="12"
              sm="6"
          >
            <v-text-field
                v-model="thirdName"
                :rules="[rules.required, rules.counter]"
                label="По батькові"
                counter
                maxlength="20"
            ></v-text-field>
          </v-col>
          <v-col
              cols="12"
              sm="6"
          >
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
                    prepend-icon="mdi-calendar"
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
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-text-field
                v-model="password"
                type="password"
                :rules="[rules.required]"
                label="Пароль"
            ></v-text-field>
          </v-col>
          <v-col>
            <v-text-field
                type="password"
                v-model="repeatPassword"
                :rules="[rules.required]"
                label="Повторіть пароль"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-btn type="submit" block color="primary" large :disabled="!valid">Зареєструватися</v-btn>
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
  </v-container>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
export default {
  data: () => ({
    valid: false,
    secondName: '',
    thirdName: '',
    birthDate: '',
    password: '',
    repeatPassword: '',
    name: '',
    phone: '',
    email: '',
    menu: false,
    snackbar: false,
    error: null,
    timeout: 2000,
    rules: {
      required: value => !!value || 'Це поле обов\'язкове.',
      counter: value => value.length <= 20 || 'Максимальна довжина 20 символів',
      email: value => {
        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        return pattern.test(value) || 'Неправильний e-mail.'
      },
    },
  }),
  computed: {
    ...mapGetters({
      getNotRegisteredUser: 'general/getNotRegisteredUser'
    })
  },
  watch: {
    menu (val) {
      val && setTimeout(() => (this.$refs.picker.activePicker = 'YEAR'))
    },
  },
  methods: {
    ...mapActions({
      signUp: 'user/signUp'
    }),
    save (date) {
      this.$refs.menu.save(date)
    },
    async register() {
      if(this.password !== this.repeatPassword) {
        this.snackbar = true;
        this.error = 'Паролі не співпадають';
        return
      }
      let payload = {
        user: {
          second_name: this.secondName,
          third_name: this.thirdName,
          birth_date: this.birthDate,
          first_name: this.name,
          email: this.email,
          phone: this.phone,
          password: this.password,
          username: this.email
        }
      }
      await this.signUp(payload)
      if(this.getNotRegisteredUser) {
        await this.$router.push('/order')
        return
      }
      await this.$router.push('/')
    }
  }
}
</script>
