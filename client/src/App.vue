<template>
    <v-app dark>
        <v-navigation-drawer
                v-model="drawer"
                :mini-variant="miniVariant"
                :clipped="clipped"
                fixed
                app
        >
            <v-list>
                <v-list-item
                        v-for="(item, i) in items"
                        :key="i"
                        :to="item.to"
                        router
                        exact
                >
                    <v-list-item-action>
                        <v-icon>{{ item.icon }}</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title v-text="item.title" />
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
        <v-app-bar
                :clipped-left="clipped"
                fixed
                app
        >
            <v-app-bar-nav-icon @click.stop="miniVariant = !miniVariant" />
            <v-toolbar-title v-text="title" />
            <v-spacer />
            <v-btn-toggle

            >
                <auth-user :title="'Увійти'" />
                <v-btn
                    color="primary"
                    :to="'/profile'"
                >
                  Особистий кабінет
                  <v-icon
                      right
                      color="white"
                  >
                    mdi-account-circle
                  </v-icon>
                </v-btn>
                <v-btn color="primary" :to="'/order'">Оформити поліс</v-btn>
                <v-btn
                        dark
                        color="primary"
                        @click="$vuetify.theme.dark = !$vuetify.theme.dark"
                >
                    <v-icon dark>
                        mdi-weather-night
                    </v-icon>
                </v-btn>
            </v-btn-toggle>
        </v-app-bar>
        <v-main>
            <v-container fluid style="padding: 0">
                <router-view />
            </v-container>
        </v-main>
        <v-footer
                :absolute="!fixed"
                app
        >
            <span>&copy; {{ new Date().getFullYear() }}</span>
        </v-footer>
    </v-app>
</template>

<script>
    import AuthUser from "./components/popups/AuthUser";
    export default {
        data () {
            return {
                clipped: true,
                drawer: true,
                fixed: true,
                items: [
                    {
                        icon: 'mdi-apps',
                        title: 'Головна',
                        to: '/'
                    },
                    {
                        icon: 'mdi-chart-bubble',
                        title: 'Оформити поліс',
                        to: '/order'
                    },
                    {
                        icon: 'mdi-police-badge-outline',
                        title: 'Страхові поліси',
                        to: '/polices'
                    }
                ],
                miniVariant: false,
                title: 'Страхування врожаю'
            }
        },
        components: {
            AuthUser
        }
    }
</script>

<style>
    ::-webkit-scrollbar {
        width: 10px;
        background: #363636;
    }

    /* Track */
    ::-webkit-scrollbar-track {
        background: #121212;
        border-radius: 2px;
    }
    ::-webkit-scrollbar-thumb {
        background: #363636;
        border-radius: 10px;
    }
</style>
