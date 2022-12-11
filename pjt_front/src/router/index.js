import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '@/views/MainView'
import ProjectItemView from '@/views/Project/ProjectItmeView'
import ProjectListView from '@/views/Project/ProjectListView'
import PeopleListView from '@/views/People/PeopleListView'
import PeopleItemView from '@/views/People/PeopleView'


Vue.use(VueRouter)

const routes = [
  {
    path: '',
    name: 'main',
    component: MainView
  },
  {
    path: '/projects',
    name: 'projects',
    component: ProjectListView
  },
  {
    path: '/project/:projectId',
    name : 'project',
    component: ProjectItemView
  },
  {
    path: '/peoples',
    name: 'peoples',
    component: PeopleListView
  },
  {
    path: '/people/:username',
    name: 'people',
    component: PeopleItemView,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
