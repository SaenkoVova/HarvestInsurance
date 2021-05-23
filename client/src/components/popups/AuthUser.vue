<template>
    <v-dialog
            transition="dialog-top-transition"
            max-width="600"
            v-model="show"
    >
        <template v-slot:activator="{ on, attrs }">
            <v-btn
                @click="togglePopup(on)"
                    color="primary"
                    v-bind="attrs"
                    v-on="on"
            >{{title}}</v-btn>
        </template>
        <template v-slot:default="dialog">
            <v-card>
              <v-form v-model="valid">
                <v-toolbar
                        dark
                >{{title}}</v-toolbar>
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-text-field
                                    v-model="email"
                                    label="Ім'я користувача"
                                    required
                                    :rules="[rules.email]"
                            ></v-text-field>
                        </v-row>
                        <v-row>
                            <v-text-field
                                    label="Пароль"
                                    v-model="password"
                                    required
                                    type="password"
                                    :rules="[rules.required]"
                            ></v-text-field>
                        </v-row>
                        <v-row>
                            <span>Ще не маєте обліковго запису: </span>
                            <span @click="show = false; $router.push('/register')" style="color: cornflowerblue; cursor: pointer"> зареєструйтесь</span>
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
                      @click="signIn"
                      :disabled="!valid"
                    >
                        {{title}}
                    </v-btn>
                </v-card-actions>
              </v-form>
            </v-card>
        </template>
    </v-dialog>
</template>

<script>
import {mapActions, mapGetters, mapMutations} from "vuex";

    export default {
      props: {
          title: {
              type: String,
              required: true
          }
      },
      data: () => ({
        show: false,
        email: null,
        password: null,
        valid: false,
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
          getAuthPopupActive: 'general/getAuthPopupActive'
        })
      },
      watch: {
        getAuthPopupActive() {
          this.show = true;
        }
      },
      methods: {
        ...mapActions({
          logIn: 'user/logIn',
          loadUserInfo: 'user/loadUserInfo',
          loadUserDocs: 'user/loadUserDocs'
        }),
        ...mapMutations({
          togglePopup: 'general/togglePopup'
        }),
        signIn() {
          let user = {
            user: {
              email: this.email,
              password: this.password
            }
          }
          this.logIn(user)
            .then( async () => {
              await this.loadUserInfo();
              await this.loadUserDocs();
              this.show = false;
            })
        }
      }
    }
</script>
