<script>
import axios from 'axios';
// import router from '../routes';

export default {
    data () {
        return{
            now: new Date(),
            notFound: false,
            data: null,
            comments: null,
            commentSection: false,
            newComment: {
              name: '',
              comment: '',
              slug: '',
            },
        };
    },
    // watch: {
    //   commentSection() {

    //   }
    // },
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
      toggleComments() {
          this.commentSection = !this.commentSection;
      },
      submitComment() {
        this.newComment.slug = this.data.slug;
        axios
        .post(`http://127.0.0.1:8000/make-comment`, this.newComment)
        .then((response) => {
          this.comments.unshift(response.data);
        })
        this.newComment.name = '';
        this.newComment.comment = '';
      },
    },
    created() {
      console.log(this.$route.params)
      axios
      .get(`http://127.0.0.1:8000/load-note/${this.$route.params['slug']}`)
      .then((response) => {
        this.data = response.data;
      })
      .catch((error) => {
        this.notFound = true;
        console.log(error);
      })
      axios
      .get(`http://127.0.0.1:8000/load-comments/${this.$route.params['slug']}`)
      .then((response) => {
        this.comments = response.data;
      })
    },
}
</script>
<template>
  <div
    v-if="data && comments"
    class="flex portrait:flex-col h-screen font-light text-slate-700 landscape:p-10 portrait:py-10 text-center"
  >
    <div class="flex flex-col">
      <h1 class="m-auto font-black portrait:mb-5" v-text="data.name"></h1>
      <img
        class="m-auto w-[500px]"
        :src="`http://localhost:8000${data.image}`"
        :alt="`${data.slug}.jpg`"
      />
      <h2 class="m-auto font-bold" v-text="data.wtype + ' ' + data.region"></h2>
    </div>
    <div class="flex flex-col portrait:grid portrait:h-1/2 landscape:my-2">
      <h6 class="portrait:mt-5" v-text="timeStamp(data.date)"></h6>
      <h6 v-text="data.tag"></h6>
      <h3 class="m-auto text-justify p-5" v-html="data.content"></h3>
      <router-link
        class="underline hover:text-gray-500 my-2 portrait:pb-10"
        @click="toggleComments()"
        to=""
        v-text="commentSection ? 'Hide Comments' : `Comments(${comments.length})`"
      ></router-link>
      <div
        v-if="commentSection"
        class="flex portrait:flex-col-reverse text-slate-700 text-justify border-t-2 portrait:border-t landscape:overflow-y-auto"
      >
        <div class="flex flex-col mx-auto overflow-y-auto w-full portrait:my-5">
          <h2 v-if="comments.length === 0" class="text-center my-2">
            No comments.
          </h2>
          <div v-else class="comment-card" v-for="comment in comments">
            <p class="mb-1 text-gray-500" v-text="timeStamp(comment.date)"></p>
            <p class="font-semibold">{{ comment.name  }} says:</p>
            <p class="ml-1" v-text="comment.comment"></p>
          </div>
        </div>
        <div
          class="flex flex-col text-center landscape:p-10 portrait:pt-5 m-auto p-1 landscape:w-1/2"
        >
          <form class="flex flex-col">
            <input
              v-model="newComment.name"
              name="name"
              class="border mb-1 p-1 rounded-t"
              placeholder="Name"
              type="text"
            />
            <textarea
              v-model="newComment.comment"
              name="comment"
              class="border p-1 rounded-b"
              placeholder="Comment"
              cols="30"
              rows="5"
            ></textarea>
            <button
              class="disabled:text-gray-400 hover:text-gray-400"
              :disabled="!newComment.name || !newComment.comment"
              @click.prevent="submitComment"
            >
              Send
            </button>
          </form>
        </div>
      </div>
      <!-- <div v-if="!commentSection" class="w-full ml-1 p-10"></div> -->
    </div>
    <!-- <div class="w-full"></div> -->
  </div>
  <h1 v-else-if="!notFound" class="loading-text">Loading...</h1>
  <h1 class="loading-text" v-else>404</h1>
</template>
