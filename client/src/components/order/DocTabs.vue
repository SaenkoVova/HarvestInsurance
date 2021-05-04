<template>
  <v-container fluid>
    <v-tabs @change="tabChanged" class="mb-5" centered>
      <v-tab v-if="!getDocs.filter(i => i.type === 'ukraine_passport').length">Паспорт України</v-tab>
      <v-tab v-if="!getDocs.filter(i => i.type === 'id_card').length">ID карта</v-tab>
      <v-tab v-if="!getDocs.filter(i => i.type === 'foreign_passport').length">Закордонний паспорт</v-tab>
    </v-tabs>
    <v-row>
      <v-col v-if="currentTab === 0 || currentTab === 2">
        <v-text-field
            label="Серія і номер"
            outlined
            v-model="seriesAndNumber"
            :rules="[rules.required, rules.counter]"
            counter
            maxlength="8"
        ></v-text-field>
      </v-col>
      <v-col>
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
                outlined
                v-model="issueDate"
                label="Коли виданий"
                readonly
                v-bind="attrs"
                v-on="on"
                :rules="[rules.required]"
                counter
                maxlength="10"
            ></v-text-field>
          </template>
          <v-date-picker
              ref="picker"
              v-model="issueDate"
              :max="new Date().toISOString().substr(0, 10)"
              min="1950-01-01"
              @change="save"
          ></v-date-picker>
        </v-menu>
      </v-col>
      <v-col v-if="currentTab === 0 || currentTab === 1">
        <v-text-field
            label="Ким виданий"
            :rules="[rules.required, rules.counter]"
            counter
            maxlength="8"
            outlined
            v-model="issuedBy"
        ></v-text-field>
      </v-col>
      <v-col v-if="currentTab === 1">
        <v-text-field
            label="Номер"
            outlined
            v-model="number"
        ></v-text-field>
      </v-col>
      <v-col v-if="currentTab === 1">
        <v-text-field
            label="Запис"
            outlined
            v-model="note"
        ></v-text-field>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import {mapGetters} from "vuex";

export default {
  data: () => ({
    currentTab: 1,
    seriesAndNumber: '',
    issueDate: '',
    issuedBy: '',
    number: '',
    note: '',
    menu: false,
    rules: {
      required: value => !!value || 'Це поле обов\'язкове.',
      counter: value => value.length <= 8 || 'Максимальна довжина 20 символів'
    },
  }),
  computed: {
    ...mapGetters({
      getDocs: 'user/getDocs'
    })
  },
  methods: {
    tabChanged(tab) {
      this.currentTab = tab;
    },
    save (date) {
      this.$refs.menu.save(date)
    },
  },
  watch: {
    menu (val) {
      val && setTimeout(() => (this.$refs.picker.activePicker = 'YEAR'))
    },
  }
}
</script>
