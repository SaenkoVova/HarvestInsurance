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
            <doc-tabs></doc-tabs>
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
    import DocTabs from "@/components/order/DocTabs";
    export default {
        name: 'Order',
        data: () => ({
          date: new Date().toISOString().substr(0, 10),
          menu: false,
          currentTab: 1
        }),
        components: {DocTabs, DatePicker, InsuredEventSelector, ControlMap}
    }
</script>
