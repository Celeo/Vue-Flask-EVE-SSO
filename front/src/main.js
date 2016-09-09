import Vue from 'vue'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'

import App from './App.vue'
import Login from './Login.vue'


Vue.use(VueResource)
Vue.http.options.root = '/'
Vue.http.options.emulateJSON = true

Vue.use(VueRouter)
let router = new VueRouter({
  hashbang: false,
  history: true
})

router.map({
  '/': {
    component: App,
    name: 'app'
  },
  '/login': {
    component: Login,
    name: 'login'
  },
  '/sso_callback': {
    component: Login,
    name: 'eve_sso_callback'
  }
})
router.redirect({
  '/*': '/',
})
router.beforeEach(function(transition) {
  if (!transition.to.path.startsWith('/login')) {
    let name = localStorage.getItem('character_name')
    if (!name || name == undefined) {
      transition.redirect('/login')
      return
    }
  }
  transition.next()
})

let Root = Vue.extend({})
router.start(Root, '#app')
