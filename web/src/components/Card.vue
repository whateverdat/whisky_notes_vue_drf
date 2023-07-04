<script>
export default {
  data () {
    return {
      convertedDate: null,
      now: new Date(),
    }
  },
  props: ['data'],
  methods: {
    timeStamp(time) {
        let date = new Date(time)
        let diffInMs = this.now - date;
        if (diffInMs < 86400000) {
          let diffInHours = Math.floor(diffInMs / 3600000)
          if (diffInHours <= 0)
          {
            return `Less than an hour ago.`
          }
          return `${diffInHours} hour${diffInHours == 1 ? '' : 's'} ago.`
        }
        return `${date.toDateString()} ${date.toTimeString().split(' ')[0]}`
      },
  }
}
</script>
<template>
  <div class="items-stretch w-1/2 portrait:w-full text-gray-700 p-2">
    <div class="rounded-lg relative shadow font-thin text-center py-2 h-full">
      <div>
        <h2 v-text="data.name"></h2>
        <h5 v-text="data.wtype"></h5>
        <h3 v-text="data.region"></h3>
        <h6 v-text="timeStamp(data.date)"></h6>
      </div>
      <router-link class="card-link" :to="data.slug"><span></span></router-link>
      <img
        :src="`http://localhost:8000${data.image}`"
        :alt="`${data.slug}.jpg`"
        class="card-image object-scale-down object-right py-0.5"
      />
    </div>
  </div>
</template>
