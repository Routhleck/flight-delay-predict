import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from "../views/Login";
import MAININTER from '../views/MAIN-INTER.vue'
import Register from "@/views/Register";
import Manager from "@/views/Manager";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/Register',
    name: 'Register',
    component: Register
  },
  {
    path: '/MAIN-INTER',
    name: 'MAIN-INTER',
    component: MAININTER
  },
  {
    path: '/Manager',
    name: 'Manager',
    component: Manager
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
