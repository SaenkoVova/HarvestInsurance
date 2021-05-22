<template>
    <v-app dark>
      <navigation-drawer></navigation-drawer>
      <tool-bar></tool-bar>
        <v-main>
            <div>
              <router-view />
            </div>
        </v-main>
      <app-footer></app-footer>
    </v-app>
</template>

<script>
    import NavigationDrawer from "./components/core/NavigationDrawer";
    import ToolBar from "./components/core/ToolBar";
    import AppFooter from "./components/core/AppFooter";
    export default {

      components: {
        AppFooter,
        ToolBar,
        NavigationDrawer
        }
    }
</script>

<style lang="scss">
    @import "assets/scss/style";
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

    .toolbar-title {
      color: #fff!important;
      text-decoration: none!important;
    }
    .unread {
      background: #2ecc71;
      transition: 3s;
    }
</style>
