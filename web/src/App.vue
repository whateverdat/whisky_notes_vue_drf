<script>
import router from './routes';
// import Home from './pages/Home.vue';
// import All from './pages/All.vue';
// import Filtered from './pages/Filtered.vue';
// import Note from './pages/Note.vue';

export default {
  data() {
    return{
      data: null,
    };
  },
  created() {
    // console.log(this.$route.fullPath)
    // router.addRoute({ path: '/', component: Home });
    // router.addRoute({ path: '/all', component: All });
    // router.addRoute({ path: '/scotch', component: Filtered});
    // router.addRoute({ path: '/irish', component: Filtered});
    // router.addRoute({ path: '/american', component: Filtered});
    // router.addRoute({ path: '/other', component: Filtered});
    // router.addRoute({ path: '/daily', component: Filtered});
    // router.addRoute({ path: '/value', component: Filtered});
    // router.addRoute({ path: '/gift', component: Filtered});
    // router.addRoute({ path: '/occasion', component: Filtered});
    // router.addRoute({ path: '/:slug', component: Note});

    // router.replace(router.currentRoute.value.fullPath)
  }

}
</script>

<template>
  <div class="flex portrait:flex-col">
    <Nav></Nav>
    <router-view :key="$route.fullPath"></router-view>
  </div>
</template>
