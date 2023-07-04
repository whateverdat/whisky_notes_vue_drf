import { createRouter, createWebHistory } from 'vue-router';
import Home from './pages/Home.vue';
import Note from './pages/Note.vue';
import All from './pages/All.vue';
import Filtered from './pages/Filtered.vue';

const router = createRouter({
  history: createWebHistory(),
  mode: 'history',
  // routes: [{ path: '/', component: Home }],
  // routes: [{ path: '/:slug', component: Note }],
  // router.addRoute({ path: '/', component: Home });
  routes: [
    { path: '/', component: Home },
    { path: '/all', component: All },
    { path: '/scotch', component: Filtered },
    { path: '/irish', component: Filtered },
    { path: '/american', component: Filtered },
    { path: '/other', component: Filtered },
    { path: '/daily', component: Filtered },
    { path: '/value', component: Filtered },
    { path: '/gift', component: Filtered },
    { path: '/occasion', component: Filtered },
    { path: '/:slug', component: Note },
  ],
});
// document.title += document.title + ' ' + window.location.href.split('/')[3];
let currentURL = window.location.href.split('/');
if (currentURL.length > 4) {
  window.location.href = `http://localhost:5173/${currentURL[3]}`;
}
// console.log(currentURL);
// router.addRoute({ path: '/:slug', component: Note });
// router.replace(router.currentRoute.value.fullPath);
// router.replace(router.currentRoute.value.fullPath);

export default router;
