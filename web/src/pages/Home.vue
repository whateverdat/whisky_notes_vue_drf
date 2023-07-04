<script>
import axios from 'axios';

export default {
    data () {
        return{
            data: null,
        };
    },
    created() {
    axios
      .get(`http://127.0.0.1:8000/load-homepage`)
      .then((response) => {
        this.data = response.data;
      })
  }
}
</script>
<template>
  <div class="flex flex-wrap landscape:w-2/3">
    <h1 class="loading-text" v-if="!data">Loading...</h1>
    <Card v-else v-for="item in data" :data="item"></Card>
  </div>
</template>
