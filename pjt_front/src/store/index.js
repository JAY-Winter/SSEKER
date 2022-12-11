import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    projects: [],
    project: [],
    people: [],
    API_URL: 'http://127.0.0.1:8000',
  },
  getters: {
  },
  mutations: {
    GET_PROJECTS(state, projects) {
      state.projects = projects
    },
    GET_PROJECT(state, project) {
      state.project = project
    },
    GET_PEOPLE(state, people) {
      state.people = people
    }
  },
  actions: {
    getProjects(context) {
      axios({
        method: 'get',
        url: `${this.state.API_URL}/projects`
      })
      .then((res) => {
        context.commit('GET_PROJECTS', res.data)
      })
      .catch((err => {
        console.log(err)
      }))
    },
    getProject(context, projectId) {
      axios({
          method: 'get',
          url: `${this.state.API_URL}/projects/project/${projectId}`
      })
      .then((res => {
          context.commit('GET_PROJECT', res.data)
      }))
      .catch((err => {
          console.log(err)
      }))
    },
    getPeople(context) {
      axios({
        method: 'get',
        url: `${this.state.API_URL}/accounts/people`
      })
      .then((res => {
        context.commit('GET_PEOPLE', res.data)
      }))
      .catch((err => {
        console.log(err)
      }))
    }
  },
  modules: {
  }
})
