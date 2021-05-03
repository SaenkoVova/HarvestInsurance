import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home'
import Order from '../views/Order'
import OrderConfirmation from '../views/OrderConfirmation'
import Profile from '../views/Profile'
import FieldState from '../views/FieldState'
import Register from '../views/Register'
import PageNotFound from '../views/404'
import Store from '@/store'
import Dashboard from "../views/Dashboard";

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
    component: Order,
    meta: {
      requiredAuth: true
    }
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      requiredAuth: true
    }
  },
  {
    path: '/checkout',
    name: 'OrderConfirmation',
    component: OrderConfirmation,
    meta: {
      requiredAuth: true
    }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: {
      requiredAuth: true
    }
  },
  {
    path: '/field-state/:id',
    name: 'FieldState',
    props: true,
    component: FieldState,
    meta: {
      requiredAuth: true
    }
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
    beforeEnter(to, from, next) {
      if(Store.getters['user/getAuthState']) {
        next({
          path: '/'
        })
      }
      else {
        next()
      }
    }
  },
  {
    path: '*',
    name: 'NotFound',
    component: PageNotFound
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiredAuth)) {
    if(!Store.getters["user/getAuthState"]) {
      next({
        path: '/'
      })
    }
    else {
      next()
    }
  }
  else {
    next();
  }
})

export default router
