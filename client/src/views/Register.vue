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
            <v-text-field
                v-model="birthDate"
                :rules="[rules.required]"
                label="Дата народження"
                counter
                maxlength="10"
            ></v-text-field>
          </v-col>
        </v-row>
        <doc-tabs ref="docTabs"></doc-tabs>
        <v-btn type="submit" block color="primary" large :disabled="!valid">Зареєструватися</v-btn>
      </v-container>
    </v-form>
  </v-container>
</template>

<script>
import DocTabs from "@/components/order/DocTabs";
import {mapActions} from "vuex";
export default {
  components: {DocTabs},
  data: () => ({
    valid: false,
    name: '',
    secondName: '',
    phone: '',
    email: '',
    thirdName: '',
    birthDate: '',
    rules: {
      required: value => !!value || 'Це поле обов\'язкове.',
      counter: value => value.length <= 20 || 'Max 20 characters',
      email: value => {
        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        return pattern.test(value) || 'Invalid e-mail.'
      },
    },
  }),
  methods: {
    ...mapActions({
      signUp: 'user/signUp'
    }),
    register() {
      let payload = {
        user: {
          firstName: this.name,
          secondName: this.secondName,
          thirdName: this.thirdName,
          email: this.email,
          phone: this.phone,
          birthDate: this.birthDate
        },
        doc: {
          seriesAndNumber: this.$refs.docTabs.seriesAndNumber,
          passportIssue: this.$refs.docTabs.issueDate,
          issuedBy: this.$refs.docTabs.issuedBy,
          number: this.$refs.docTabs.seriesAndNumber,
          note: this.$refs.docTabs.note
        },
        currentTab: this.$refs.docTabs.currentTab
      }
      this.signUp(payload);
    }
  }
}
</script>
