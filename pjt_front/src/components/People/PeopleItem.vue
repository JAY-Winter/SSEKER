<template>
    <div>
        <div class="user-profile-container d-flex flex-row justify-content-around">
            <div class="user-profile-image-container">
                <div>{{ this.people.username }}</div>
                <div>Uni: {{ this.people.university.name }}</div>
                <div>
                    Speciality: <span v-for="skill in this.people.skill" :key="skill.id">{{ skill.title }} | </span>
                </div>
            </div>
            <div class="user-introduce-container">
                <div class="profile-introduce my-5">{{ this.people.introduce }}</div>
                Availability :<span v-for="availability in this.people.availability" :key="availability.id">{{availability.day}} | </span>
                <div class="my-3" v-if="this.people.onoffline.id === 3">{{ this.people.onoffline.title }}</div>
                <div class="my-3" v-else>{{ this.people.onoffline.title }} Only</div>
                <div>Experiences in platform: </div>
                Interests: 
                <span v-if="this.people.interest.length > 0">
                    <span v-for="interest in this.people.interest" :key="interest.id">{{ interest.name }} | </span>
                </span>
                <span v-else>None</span>
            </div>
        </div>
        <div class="d-flex justify-content-sm-around">
            <button class="btn btn-primary">Contact User {{ this.people.username }}</button>
            <button class="btn btn-primary">View Resume/Portfolio</button>
        </div>
        <div class="silmilar-skill-people-container mt-5">
            <SimilarSkillPeopleListVue/>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import SimilarSkillPeopleListVue from '@/components/People/SimilarSkillPeopleList'

export default {
    data() {
        return {
            people: null
        }
    },
    created() {
        this.getPeopleInfo()
    },
    methods: {
        getPeopleInfo() {
            console.log('getPeopleInfo')
            const username = this.$route.params.username
            axios({
                method: 'get',
                url: `${this.$store.state.API_URL}/accounts/people/${username}`
            })
            .then((res => {
                this.people = res.data
            }))
            .catch(err => console.log(err))
        }
    },
    components: {
        SimilarSkillPeopleListVue,
    }
}
</script>

<style>

</style>