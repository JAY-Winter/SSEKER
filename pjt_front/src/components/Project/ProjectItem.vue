<template>
    <div>
        <h1>{{ this.$store.state.project.title }}</h1>
        <div class="project-container d-flex">
            <div class="project-item-container container-lg">
                <div>{{ this.$store.state.project.content }}</div>
                <h3>Who is in a team</h3>
                <div v-for="participant in this.$store.state.project.participant" :key="participant.id">
                    {{ participant.username}}
                </div>
                <div>
                    Location<span v-for="location in this.$store.state.project.location" :key="location.id"> {{ location.city }} |</span>
                </div>
                <div>
                    Needed Skills<div v-for="skill in this.$store.state.project.need_skill" :key="skill.id"> {{ skill.title }}</div>
                </div>
                <div>
                    Duration Of Project {{ this.$store.state.project.start_date.substr(0,10) }} - {{ this.$store.state.project.end_date.substr(0,10) }}
                </div>
                <button class="btn btn-primary">
                    Apply Now
                </button>
            </div>
            <div class="project-user-container container-sm">
                <router-link :to="{ name: 'people', params: { username: this.$store.state.project.founder.username }}">
                <div>{{ this.$store.state.project.founder.username}}</div>
                <div>Uni: {{ this.$store.state.project.founder.university.name}}</div>
                <div>Skills: <span v-for="skill in this.$store.state.project.founder.skill" :key="skill.id">{{ skill.title}}</span></div> 
                <button class="btn btn-primary">Contact User <b>{{ this.$store.state.project.founder.username }}</b></button>
            </router-link>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'ProjectItem',
    created() {
        this.$store.dispatch('getProject', this.$route.params.projectId)
    },  
}
</script>

<style>

</style>