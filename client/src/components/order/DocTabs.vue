<template>
  <v-container fluid>
    <v-tabs @change="tabChanged" class="mb-5">
      <v-tab>Паспорт України</v-tab>
      <v-tab>ID карта</v-tab>
      <v-tab>Закордонний паспорт</v-tab>
    </v-tabs>
    <v-row>
      <v-col v-if="currentTab === 0 || currentTab === 2">
        <v-text-field
            label="Серія і номер"
            outlined
            v-model="seriesAndNumber"
        ></v-text-field>
      </v-col>
      <v-col>
        <v-text-field
            label="Коли виданий"
            outlined
            v-model="issueDate"
        ></v-text-field>
      </v-col>
      <v-col v-if="currentTab === 0 || currentTab === 1">
        <v-text-field
            label="Ким виданий"
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

export default {
  data: () => ({
    currentTab: 1,
    seriesAndNumber: null,
    issueDate: null,
    issuedBy: null,
    number: null,
    note: null
  }),
  methods: {
    tabChanged(tab) {
      this.currentTab = tab;
    }
  }
}
</script>
