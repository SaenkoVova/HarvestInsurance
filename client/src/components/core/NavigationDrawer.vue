<template>
  <v-navigation-drawer
      :mini-variant="getDrawerMiniVariant"
      :clipped="true"
      fixed
      app
  >
    <v-list v-if="getAuthState">
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


    <v-list v-else>
      <v-list-item
          v-for="(item, i) in items.filter(i => i.requireAuth === false)"
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
</template>


<script>
  import {mapGetters} from "vuex";

  export default {
    data: () => ({
      items: [
        {
          icon: 'mdi-apps',
          title: 'Головна',
          to: '/',
          requireAuth: false
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Оформити поліс',
          to: '/order',
          requireAuth: false
        },
        {
          icon: 'mdi-desktop-mac-dashboard',
          title: 'Панель керування',
          to: '/dashboard',
          requireAuth: true
        }
      ],

    }),
    computed: {
      ...mapGetters({
        getDrawerMiniVariant: 'general/getDrawerMiniVariant',
        getAuthState: 'user/getAuthState',
      })
    }
  }
</script>
