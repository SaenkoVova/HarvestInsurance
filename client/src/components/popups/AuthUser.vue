<template>
    <v-dialog
            transition="dialog-top-transition"
            max-width="600"
    >
        <template v-slot:activator="{ on, attrs }">
            <v-btn
                    color="primary"
                    v-bind="attrs"
                    v-on="on"
            >{{title}}</v-btn>
        </template>
        <template v-slot:default="dialog">
            <v-card>
                <v-toolbar
                        dark
                >{{title}}</v-toolbar>
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-text-field
                                    label="Ім'я користувача"
                                    required
                            ></v-text-field>
                        </v-row>
                        <v-row>
                            <v-text-field
                                    label="Пароль"
                                    required
                            ></v-text-field>
                        </v-row>
                        <v-row>
                            Ще не маєте обліковго запису:
                        </v-row>
                    </v-container>
                </v-card-text>
                <v-card-actions class="justify-end">
                    <v-btn
                            text
                            @click="dialog.value = false"
                    >Закрити</v-btn>
                    <v-btn
                            text
                            color="primary"
                            @click="dialog.value = false"
                    >
                        {{title}}
                    </v-btn>
                </v-card-actions>
            </v-card>
        </template>
    </v-dialog>
</template>

<script>
    export default {
        props: {
            title: {
                type: String,
                required: true
            }
        }
    }
</script>
