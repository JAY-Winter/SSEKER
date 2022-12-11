<template>
    <div>
        <div class="input-group d-flex justify-content-center container-sm my-5">
            <input type="search" class="form-control rounded mx-3" placeholder="Search" aria-label="Search" aria-describedby="search-addon"/>
            <button type="button" class="btn btn-outline-primary rounded">search</button>
        </div>
        <div class="project-container d-flex flex-row flex-wrap">
            <div class="col-md-4 border border-light rounded" v-for="project in this.$store.state.projects" :key="project.id">
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

export default {
    name: 'ProjectList',
    created() {
        this.$store.dispatch('getProjects')
    },
}
</script>

<style>

</style>