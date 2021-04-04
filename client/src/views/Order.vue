<template>
    <v-container fluid>
        <v-row>
            <v-col>
                <v-text-field
                        label="Строк страхування"
                        outlined
                ></v-text-field>
            </v-col>
            <v-col>
                <v-text-field
                        label="Сума покриття страхового випадку"
                        outlined
                ></v-text-field>
            </v-col>
        </v-row>
        <div>
            <insured-event-selector></insured-event-selector>
        </div>
        <div>
            <p>Оберіть дату початку дії страхового полісу</p>
            <date-picker></date-picker>
        </div>
        <div>
            <p>Особисті дані</p>
            <v-row>
                <v-col :cols="6">
                    <v-text-field
                            label="Прізвище"
                            outlined
                    ></v-text-field>
                </v-col>
                <v-col :cols="6">
                    <v-text-field
                            label="Ім'я"
                            outlined
                    ></v-text-field>
                </v-col>
                <v-col :cols="6">
                    <v-text-field
                            label="Побатькові"
                            outlined
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
                    ></v-text-field>
                </v-col>
                <v-col>
                    <v-text-field
                            label="Коли виданий"
                            outlined
                    ></v-text-field>
                </v-col>
                <v-col v-if="currentTab === 0 || currentTab === 1">
                    <v-text-field
                            label="Ким виданий"
                            outlined
                    ></v-text-field>
                </v-col>
                <v-col v-if="currentTab === 1">
                    <v-text-field
                            label="Номер"
                            outlined
                    ></v-text-field>
                </v-col>
                <v-col v-if="currentTab === 1">
                    <v-text-field
                            label="Запис"
                            outlined
                    ></v-text-field>
                </v-col>
            </v-row>
            <div>
                <p>Контактні дані</p>
                <v-row>
                    <v-col>
                        <v-text-field
                                label="Телефон"
                                outlined
                        ></v-text-field>
                    </v-col>
                    <v-col>
                        <v-text-field
                                label="E-mail"
                                outlined
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
            <v-btn color="primary" large block :to="'/checkout'">
                Продовжити
            </v-btn>
        </div>
    </v-container>
</template>

<script>
    import ControlMap from "../components/order/ControlMap";
    import InsuredEventSelector from "../components/order/InsuredEventSelector";
    import DatePicker from "../components/order/DatePicker";
    export default {
        name: 'Order',
        data: () => ({
            date: new Date().toISOString().substr(0, 10),
            menu: false,
            modal: false,
            menu2: false,
            currentTab: 1
        }),
        methods: {
            tabChanged(tab) {
                this.currentTab = tab;
            }
        },
        components: {DatePicker, InsuredEventSelector, ControlMap}
    }
</script>
