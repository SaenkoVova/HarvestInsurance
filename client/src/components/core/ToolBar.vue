<template>
  <v-app-bar
      :clipped-left="clipped"
      fixed
      app
  >
    <v-app-bar-nav-icon @click.stop="setDrawerVariant(!getDrawerMiniVariant)" />
    <router-link :to="'/'" class="toolbar-title">
      <v-toolbar-title v-text="title" />
    </router-link>
    <v-spacer />
    <v-btn-toggle v-if="getAuthState">
      <v-menu offset-y left origin="center center"
              transition="scale-transition">
        <template v-slot:activator="{ on, attrs }">
          <v-badge
              overlap
              left
              color="green"
              :content="getNotifications.filter(i => i.state === 'unread').length.toString()">
            <v-btn
                v-bind="attrs"
                v-on="on"
                @click="toggleMenu(attrs)">
              <v-icon>mdi-bell-alert</v-icon>
            </v-btn>
          </v-badge>
        </template>
        <v-list v-if="getNotifications.length">
          <v-list-item
              v-for="(item, index) in getNotifications"
              :key="index"
              :class="{unread: item.state === 'unread'}"
          >
            <v-list-item-content>
              <v-list-item-title class="title">
                {{convertNotification(item.notes)}}
              </v-list-item-title>
              <v-list-item-subtitle>
                {{item.created}}
              </v-list-item-subtitle>
            </v-list-item-content>
            <v-list-item-action>
              <v-btn fab small color="error" @click.stop="deleteNotification(item.id)">
                <v-icon>mdi-close</v-icon>
              </v-btn>
            </v-list-item-action>
          </v-list-item>
        </v-list>
      </v-menu>
      <v-btn
          color="primary"
          :to="'/profile'"
      >
        {{getName}}
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
      <v-btn
          dark
          color="primary"
          @click="logOut"
      >
        <v-icon dark>
          mdi-exit-to-app
        </v-icon>
      </v-btn>
    </v-btn-toggle>
    <v-btn-toggle v-else>
      <auth-user :title="'Увійти'" />
      <v-btn
          color="primary"
          :to="'/register'"
      >
        Зареєструватися
        <v-icon
            right
            color="white"
        >
          mdi-account-circle
        </v-icon>
      </v-btn>
      <v-btn
          dark
          color="primary"
          @click="setTheme"
      >
        <v-icon dark>
          mdi-weather-night
        </v-icon>
      </v-btn>
    </v-btn-toggle>
  </v-app-bar>
</template>

<script>
import AuthUser from "@/components/popups/AuthUser";
import {mapActions, mapGetters, mapMutations} from "vuex";
import loadNotification from "../../util/loadNotification";

export default {
  data: () => ({
    clipped: true,
    fixed: true,
    title: 'Страхування врожаю'
  }),
  computed: {
    ...mapGetters({
      getAuthState: 'user/getAuthState',
      getName: 'user/getName',
      getNotifications: 'user/getNotifications',
      getDrawerMiniVariant: 'general/getDrawerMiniVariant'
    })
  },
  methods: {
    ...mapMutations({
      unsetUser: 'user/unsetUser',
      setDrawerVariant: 'general/setDrawerVariant'
    }),
    ...mapActions({
      loadUserInfo: 'user/loadUserInfo',
      loadUserDocs: 'user/loadUserDocs',
      loadNotifications: 'user/loadNotifications',
      readNotifications: 'user/readNotifications',
      deleteNotification: 'user/deleteNotification'
    }),
    toggleMenu(attrs) {
      if(attrs['aria-expanded'] === 'false') {
        setTimeout(() => {
          this.readNotifications();
        }, 1000)
      }
    },
    setTheme() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
      this.$vuetify.theme.dark === false ? localStorage.setItem('appTheme', true.toString()) : localStorage.removeItem('appTheme')
    },
    logOut() {
      this.unsetUser()
      this.$router.push('/')
    },
    convertNotification(type) {
      return loadNotification.loadNotification(type)
    }
  },
  async mounted() {
    await this.loadUserInfo()
    await this.loadUserDocs()
    await this.loadNotifications()
  },
  components: {
    AuthUser
  }
}
</script>
