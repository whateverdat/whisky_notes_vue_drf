import { createApp } from 'vue';
import './style.css';
import router from './routes';
// Components
import Nav from './components/Nav.vue';
import Card from './components/Card.vue';
import DarkMode from './components/DarkMode.vue';
// Pages
import App from './App.vue';
import Home from './pages/Home.vue';
import Note from './pages/Note.vue';
import All from './pages/All.vue';
import Filtered from './pages/Filtered.vue';

const app = createApp(App);

app.use(router);
// Components
app.component('Nav', Nav);
app.component('Card', Card);
app.component('DarkMode', DarkMode);
// Pages
app.component('Home', Home);
app.component('Note', Note);
app.component('All', All);
app.component('Filtered', Filtered);

const mountedApp = app.mount('#app');
