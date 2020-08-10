import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  { path: '/', component: 'Carousel' },
  { path: '/animation', component: 'Animation' },
  { path: '/article', component: 'Article' },
  { path: '/bottomguider', component: 'BottomGuider' },
  { path: '/carousel', component: 'Carousel' },
  { path: '/guider', component: 'Guider' },
  { path: '/pagedemo', component: 'PageDemo' },
  { path: '/login', component: 'Login' },
  { path: '/regi', component: 'Regi' },
  { path:'/plaintext_new', component:'PlainText_new'},
  { path:'/showplaintext_new', component:'ShowPlainText_new'},
  { path:'/team', component:'Team'},
  { path: '*', component: 'NotFound' },
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})
