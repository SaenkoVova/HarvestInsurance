import Vue from 'vue'
import Vuex from 'vuex'
import User from './modules/user'
import Map from './modules/map'
import Order from "./modules/order";
import General from './modules/general'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    user: User,
    map: Map,
    order: Order,
    general: General
  }
})
