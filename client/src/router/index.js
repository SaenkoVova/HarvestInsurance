import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home'
import Order from '../views/Order'
import OrderConfirmation from '../views/OrderConfirmation'
import Profile from '../views/Profile'
import FieldState from '../views/FieldState'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/order',
    name: 'Order',
    component: Order
  },
  {
    path: '/checkout',
    name: 'OrderConfirmation',
    component: OrderConfirmation
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/field-state/:id',
    name: 'FieldState',
    props: true,
    component: FieldState
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
