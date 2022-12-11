<template>
    <div>
        <div class="input-group d-flex justify-content-center container-sm my-5">
            <input type="search" class="form-control rounded mx-3" placeholder="Search" aria-label="Search" aria-describedby="search-addon"/>
            <button type="button" class="btn btn-outline-primary rounded">search</button>
        </div>
        <div class="people-container d-flex flex-row flex-wrap">
            <div class="col-md-4 border border-light rounded" v-for="people in this.$store.state.people" :key="people.id">
                <router-link :to="{ name: 'people', params: { username: people.username }}">
                <p clas="card-title">{{ people.username}}</p>
                <div>
                    <div>
                        Availability
                        <span v-for="availability in people.availability" :key="availability.id">
                            {{ availability.day }}
                        </span>
                    </div>
                    <div v-if="people.onoffline.id !== 3">
                        {{ people.onoffline.title }} Only
                    </div>
                    <div v-else>
                        {{ people.onoffline.title }}
                    </div>
                    <div>
                        Skills
                        <span v-for="skill in people.skill" :key="skill.id">
                            <span>{{ skill.title }}</span> |
                        </span>
                    </div>
                    <p>Location {{ people.location[0].city }} </p>
                </div>
            </router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'peopleList',
    created() {
        this.$store.dispatch('getPeople')
    }
}
</script>

<style>

</style>