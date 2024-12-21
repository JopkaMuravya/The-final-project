import type { RouteRecordRaw } from 'vue-router';
import UserRegister from 'src/components/UserRegister.vue';
import MainPage from 'src/components/MainPage.vue'; 

const routes: RouteRecordRaw[] = [
  { path: '/', component: UserRegister },
  { path: '/main', component: MainPage }, 
];

export default routes;