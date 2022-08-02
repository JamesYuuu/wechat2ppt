import { createRouter, createWebHashHistory } from 'vue-router'
import Home from './components/Home.vue'
import Select from './components/Select.vue'
import Download from './components/Download.vue'

const routes = [
  {
    path: '/select',
    name: 'select',
    component: Select
  },
  {
    path: '/download',
    name:'download',
    component: Download
  },
  {
    path: '/',
    name: 'home',
    component: Home
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
