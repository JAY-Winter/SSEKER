<template>
    <div>
        <h1>Work With Us</h1>
        <div class="project-container d-flex flex-row justify-content-around flex-wrap container-sm my-5">
        <div class="col-md-4 border border-light rounded" v-for="project in this.ADProjects" :key="project.id">
            <router-link :to="{ name: 'project', params: { projectId: project.id }}">
                <div class="container">
                    <div class="card-header">Project {{ project.title }}</div>
                    <div class="b-flex card-body">
                    <p>{{ project.onoffline.title }}</p>
                    <div v-if="project.location.length <= 3">
                        <span v-for="location in project.location" :key="location.id">
                            <span>{{location.city}}</span> |
                        </span>
                    </div>
                    <div v-else>
                        Anywhere
                    </div>
                    <div>Needed Skills 
                        <span v-for="need_skill in project.need_skill" :key="need_skill.id">
                            <span>{{ need_skill.title }}</span> |
                        </span>
                    </div>
                    <p>Duration {{ project.start_date.substr(0,10) }} - {{ project.end_date.substr(0,10) }}</p>
                </div>
                </div>
            </router-link>
        </div>
    </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            ADProjects: [],
        }
    },
    methods: {
        getADProjects() {
            axios({
                method: 'get',
                url: `${this.$store.state.API_URL}/projects/adprojects`
            })
            .then((res => {
                this.ADProjects = res.data
            }))
            .catch(err => console.log(err))
        },
    },
    created() {
        this.getADProjects()
    }
}
</script>

<style>

</style>