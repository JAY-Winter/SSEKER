<template>
    <div>
        <ProjectItemVue/>
    </div>
</template>

<script>
import ProjectItemVue from '@/components/Project/ProjectItem'

export default {
    name: 'ProjectItemView',
    components: {
        ProjectItemVue
    },
    data() {
        return {
            project: Object,
        }
    }
}
</script>

<style>

</style>