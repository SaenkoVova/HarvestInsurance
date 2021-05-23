<template>
    <v-container fluid>
      <v-form v-model="valid">
        <h1 class="display-1 mb-5">Оформлення страхового полісу</h1>
          <v-row>
              <v-col>
                <p>Оберіть дату початку дії страхового полісу</p>
                <v-date-picker
                    v-model="startDate"
                    full-width
                    class="mt-4"
                ></v-date-picker>
              </v-col>
              <v-col>
                <p>Вкажіть кадастровий номер</p>
                <v-text-field
                    label="Кадастровий номер"
                    outlined
                    v-model="cadastralNumber"
                    :rules="[rules.required, rules.cadastralNumber]"
                    maxlength="22"
                    counter
                ></v-text-field>
                <p>Вкажіть строк страхування</p>
                <v-text-field
                    :rules="[rules.required, rules.term]"
                    label="Строк страхування"
                    outlined
                    v-model="insuranceTerm"
                ></v-text-field>
                <p>Вкажіть суму покриття страхового випадку</p>
                <v-text-field
                    label="Сума покриття страхового випадку"
                    :rules="[rules.required, rules.coverageAmount]"
                    outlined
                    v-model="coverageAmount"
                ></v-text-field>
              </v-col>
          </v-row>
          <div>
              <p>Особисті дані</p>
              <v-row>
                  <v-col :cols="6">
                      <v-text-field
                          :rules="[rules.required]"
                          label="Прізвище"
                          outlined
                          v-model="secondName"
                      ></v-text-field>
                  </v-col>
                  <v-col :cols="6">
                      <v-text-field
                          :rules="[rules.required]"
                            label="Ім'я"
                            outlined
                            v-model="firstName"
                      ></v-text-field>
                  </v-col>
                  <v-col :cols="6">
                      <v-text-field
                          :rules="[rules.required]"
                          label="Побатькові"
                          outlined
                          v-model="thirdName"
                      ></v-text-field>
                  </v-col>
                  <v-col :cols="6">
                      <v-menu
                              ref="menu"
                              v-model="menu"
                              :close-on-content-click="false"
                              :return-value.sync="date"
                              transition="scale-transition"
                              offset-y
                              min-width="auto"
                      >
                          <template v-slot:activator="{ on, attrs }">
                              <v-text-field
                                      v-model="date"
                                      label="Дата народження"
                                      prepend-icon="mdi-calendar"
                                      readonly
                                      v-bind="attrs"
                                      v-on="on"
                              ></v-text-field>
                          </template>
                          <v-date-picker
                                  v-model="date"
                                  no-title
                                  scrollable
                          >
                              <v-spacer></v-spacer>
                              <v-btn
                                      text
                                      color="primary"
                                      @click="menu = false"
                              >
                                  Cancel
                              </v-btn>
                              <v-btn
                                      text
                                      color="primary"
                                      @click="$refs.menu.save(date)"
                              >
                                  OK
                              </v-btn>
                          </v-date-picker>
                      </v-menu>
                  </v-col>
              </v-row>
              <v-row>
                <v-col v-if="getAuthState">
                  <p>Оберіть документ</p>
                  <v-select v-if="getDocs"
                      class="mt-7"
                      :items="docsToString"
                      label="Оберіть документ"
                      outlined
                      @change="selectDoc"
                  ></v-select>
                </v-col>
                <v-col v-if="!docId">
                  <p>Додайте новий документ</p>
                  <doc-tabs></doc-tabs>
                </v-col>
              </v-row>
              <div>
                  <p>Контактні дані</p>
                  <v-row>
                      <v-col>
                          <v-text-field
                              :rules="[rules.required]"
                              label="Телефон"
                              outlined
                              v-model="phone"
                          ></v-text-field>
                      </v-col>
                      <v-col>
                          <v-text-field
                              :rules="[rules.required, rules.email]"
                              label="E-mail"
                              outlined
                              v-model="email"
                          ></v-text-field>
                      </v-col>
                  </v-row>
              </div>
          </div>
          <v-container>
            <p>Обведіть земельну ділянку маркерами</p>
            <control-map></control-map>
          </v-container>
          <div>
            <v-btn color="primary" :disabled="!valid" class="mt-5 mb-5" large block @click="checkout" v-if="getAuthState">
                Продовжити
            </v-btn>
            <v-btn color="primary" class="mt-5 mb-5" @click="makeOrderAfterLogin" large block  v-else>
              Увійдіть щоб продовжити
            </v-btn>
          </div>
      </v-form>
    </v-container>
</template>

<script>
    import ControlMap from "../components/order/ControlMap";
    import DocTabs from "@/components/order/DocTabs";
    import {mapGetters, mapMutations} from "vuex";
    import http from "../util/http";


    export default {
        name: 'Order',
        data: () => ({
          valid: false,
          date: new Date().toISOString().substr(0, 10),
          startDate: new Date().toISOString().substr(0, 10),
          cadastralNumber: '',
          insuranceTerm: null,
          coverageAmount: null,
          firstName: null,
          secondName: null,
          thirdName: null,
          doc: null,
          phone: null,
          email: null,
          menu: false,
          currentTab: 1,
          selectedDocId: null,
          loading: false,
          docId: null,
          docType: null,
          rules: {
            required: value => !!value || 'Це поле обов\'язкове.',
            cadastralNumber: value => value.length === 22 || 'Довжина кадастрового номера 22 символи',
            coverageAmount: value => (isFinite(value) && value >= 1000 && value <= 100000) || 'Сума покриття має бути в межах від 1000 до 100000',
            term: value => (isFinite(value) && value >= 365) || 'Мінімальний термін страхування 365 днів',
            email: value => {
              const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
              return pattern.test(value) || 'Неправильний e-mail.'
            },
          },
        }),
        watch: {
          docId(val) {
            if(val) {
              this.valid = true
            }
          },
          getUser() {
            this.initialize()
          }
        },
        computed: {
          ...mapGetters({
            getDocs: 'user/getDocs',
            getUser: 'user/getUser',
            getConvertedCoords: 'map/getConvertedCoords',
            getAuthState: 'user/getAuthState',
            getOrder: 'order/getOrder'
          }),
          docsToString() {
            let docs = []
            const ukrainePassport = this.getDocs.find(i => i.type === 'ukraine_passport');
            if(ukrainePassport) {
              docs.push(`1. Серія і номер: ${ukrainePassport.series_and_number} Дати видачі: ${ukrainePassport.passport_issue} Ким виданий: ${ukrainePassport.issued_by}`)
            }
            const foreignPassport = this.getDocs.find(i => i.type === 'foreign_passport');
            if(foreignPassport) {
              docs.push(`2. Серія і номер: ${ukrainePassport.series_and_number} Коли виданий: ${ukrainePassport.passport_issue}`)
            }
            const idCard = this.getDocs.find(i => i.type === 'id_card');
            if(idCard) {
              docs.push(`3. Ким виданий: ${idCard.issued_by} Коли виданий: ${idCard.passport_issue} Номер: ${idCard.number} Примітки: ${idCard.notation}`)
            }
            return docs
          }
        },
        methods: {
          ...mapMutations({
            setOrder: 'order/setOrder',
            togglePopup: 'general/togglePopup',
            setNotRegisteredUser: 'general/setNotRegisteredUser'
          }),
          initOrderFields() {
            this.startDate = this.getOrder.startDate;
            this.insuranceTerm = this.getOrder.term;
            this.coverageAmount = this.getOrder.coating;
            this.cadastralNumber = this.getOrder.cadastralNumber;
          },
          makeOrderAfterLogin() {
            this.togglePopup();
            this.setNotRegisteredUser(true);
            this.setOrder({
              cadastralNumber: this.cadastralNumber,
              term: this.insuranceTerm,
              coating: this.coverageAmount,
              startDate: this.startDate,
            });
          },
          initialize() {
            this.firstName = this.getUser.firstName;
            this.secondName = this.getUser.secondName;
            this.thirdName = this.getUser.thirdName;
            this.date = this.getUser.birthDate;
            this.phone = this.getUser.phone;
            this.email = this.getUser.email;
          },
          selectDoc(val) {
            this.selectedDocId = val.split('.')[0]
            if(Number(this.selectedDocId) === 1) {
              const ukrainePassport = this.getDocs.find(i => i.type === 'ukraine_passport');
              this.docId = ukrainePassport.id
              this.docType = 'ukr'
            }
            if(Number(this.selectedDocId) === 2) {
              const foreignPassport = this.getDocs.find(i => i.type === 'foreign_passport');
              this.docId = foreignPassport.id
              this.docType = 'foreign'
            }
            if(Number(this.selectedDocId) === 3) {
              const idCard = this.getDocs.find(i => i.type === 'id_card');
              this.docId = idCard.id
              this.docType = 'id'
            }
          },
          checkout() {
            let geoJson = `{ "type": "Polygon","coordinates": [[ [${this.getConvertedCoords[0]}], [${this.getConvertedCoords[1]}], [${this.getConvertedCoords[2]}], [${this.getConvertedCoords[3]}], [${this.getConvertedCoords[0]}] ]]}`
            let data = {
              checkout: {
                geoJson,
                term: this.insuranceTerm,
                coating: this.coverageAmount
              }
            }
            http.post('getPrice/', data, {
              headers: {
                Authorization: `Bearer_${localStorage.getItem('token')}`
              }
            })
              .then(res => {
                this.setOrder({
                  firstName: this.firstName,
                  secondName: this.secondName,
                  thirdName: this.thirdName,
                  date: this.date,
                  phone: this.phone,
                  email: this.email,
                  cadastralNumber: this.cadastralNumber,
                  price: res.data,
                  term: this.insuranceTerm,
                  coating: this.coverageAmount,
                  startDate: this.startDate,
                  docType: this.docType,
                  docId: this.docId,
                  status: 0,
                  geoJson
                })
                this.$router.push('/checkout')
              })
          }
        },
        mounted() {
          if(this.getUser) {
            this.initialize()
          }
          if(this.getOrder) {
            this.initOrderFields()
          }
        },
      components: {DocTabs, ControlMap}
    }
</script>
