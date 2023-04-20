import { createRouter, createWebHashHistory } from 'vue-router'
import Ping from '../components/Ping.vue';

const routes = [
  {
    path: '/ping',
    name: 'ping',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component:Ping
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
