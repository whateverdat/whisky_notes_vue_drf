<script>
import axios from 'axios';

export default{
    data() {
        return{
            data: null,
        };
    },
    created() {
        axios
            .get(`http://localhost:8000/load-category${this.$route.path}`)
            .then((response) => {
                this.data = response.data;
            })
    }
}
</script>
<template>
  <div
    v-if="data"
    class="flex flex-wrap landscape:w-2/3 h-screen landscape:overflow-y-auto"
  >
    <Card v-for="item in data" :data="item"></Card>
    <h2 class="loading-text" v-if="data.length == 0">Nothing to show.</h2>
  </div>
  <h1 class="loading-text" v-else>Loading...</h1>
</template>
