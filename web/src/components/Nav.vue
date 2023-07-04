<script>
import axios from 'axios';
import router from '../routes';

export default {
  data () {
    return {
      mobile: true,
      path: this.$route.path,
    };
  },
  mounted() {
      document.addEventListener('click', () => {
        this.delay(100).then(() => {
          this.path = this.$route.path;
        })
      })
  },
  methods: {
    mobileNav() {
      this.mobile = !this.mobile;
      window.scrollTo(0, 0);
    },
    random() {
      axios
        .get('http://localhost:8000/load-random')
        .then((response) => {
          router.push(`${response.data.slug}`)
        })
    },
    delay(time) {
      return new Promise(resolve => setTimeout(resolve, time));
    }
  }
}
</script>
<template>
  <!-- <div class="landscape:hidden h-0.5 w-full bg-gray-400"></div> -->
  <div
    :class="`top-0 p-10 portrait:p-0 h-screen min-h-max shadow-lg bg-black bg-opacity-5 dark:bg-white dark:bg-opacity-5 flex flex-col portrait:flex-${mobile ? 'row' : 'col'} portrait:h-fit justify-between portrait:justify-around`"
  >
    <DarkMode></DarkMode>
    <ul
      :class="`flex flex-col portrait:flex-row portrait:${mobile ? 'flex-row' : 'hidden'}`"
    >
      <router-link
        :class="`nav-link landscape:border-b-4 portrait:p-3  ${ path === '/' ? 'portrait:underline landscape:translate-x-1' : ''}`"
        to="/"
        >Latest</router-link
      >
      <router-link
        :class="`nav-link landscape:border-b-4 portrait:p-3 ${ path === '/all' ? 'portrait:underline landscape:translate-x-1' : ''}`"
        to="/all"
        >A-Z</router-link
      >
      <router-link
        class="nav-link landscape:border-b-4 portrait:p-3"
        to=""
        @click="random"
        >Random</router-link
      >
    </ul>
    <ul
      :class="`flex flex-col portrait:grid grid-cols-2 portrait:${mobile ? 'hidden' : 'flex-col'} portrait:text-center portrait:my-2`"
      @click="mobileNav()"
    >
      <div class="flex flex-col">
        <router-link
          :class="`nav-link portrait:border-x landscape:border-b-4 ${ path === '/scotch' ? 'portrait:underline landscape:translate-x-1' : ''}`"
          to="/scotch"
          >Scotch</router-link
        >
        <router-link
          :class="`nav-link portrait:border-x landscape:border-b-4 ${ path === '/irish' ? 'portrait:underline landscape:translate-x-1' : ''}`"
          to="/irish"
          >Irish</router-link
        >
        <router-link
          :class="`nav-link portrait:border-x landscape:border-b-4 ${ path === '/american' ? 'portrait:underline landscape:translate-x-1' : ''}`"
          to="/american"
          >American</router-link
        >
        <router-link
          :class="`nav-link portrait:border-x landscape:border-b-4 ${ path === '/other' ? 'portrait:underline landscape:translate-x-1' : ''}`"
          to="/other"
          >Other</router-link
        >
      </div>
      <div class="flex flex-col">
        <router-link
          :class="`nav-link portrait:border-x landscape:border-b-4 ${ path === '/daily' ? 'portrait:underline landscape:translate-x-1' : ''}`"
          to="/daily"
          >Daily</router-link
        >
        <router-link
          :class="`nav-link portrait:border-x landscape:border-b-4 ${ path === '/value' ? 'portrait:underline landscape:translate-x-1' : ''} landscape:border-t-2`"
          to="/value"
          >Value</router-link
        >
        <router-link
          :class="`nav-link portrait:border-x landscape:border-b-4 ${ path === '/gift' ? 'portrait:underline landscape:translate-x-1' : ''}`"
          to="/gift"
          >Gift</router-link
        >
        <router-link
          :class="`nav-link portrait:border-x landscape:border-b-4 ${ path === '/occasion' ? 'portrait:underline landscape:translate-x-1' : ''}`"
          to="/occasion"
          >Occasion</router-link
        >
      </div>
    </ul>
    <button
      @click="mobileNav()"
      :class="`nav-btn grid mt-3 landscape:hidden portrait:flex-col mb-${mobile ? 0 : 5}`"
      v-text="mobile ? 'More' : 'Close'"
    ></button>
    <div class="portrait:hidden">
      <a
        target="_blank"
        class="text-xs underline text-slate-400"
        href="https://www.github.com/whateverdat"
        >Github</a
      >
    </div>
  </div>
</template>
