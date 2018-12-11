import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/Annotations'
import Books from '@/components/Books'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'books',
      component: Books,
      meta: {
        title: "Books",
      }
    },
    {
      path: '/annotations',
      name: 'annotations',
      component: HelloWorld,
      meta: {
        title: "Annotations",
      }
    }
  ]
})
