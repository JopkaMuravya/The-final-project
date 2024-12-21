import type { RouteRecordRaw } from 'vue-router';
import UserRegister from 'src/components/UserRegister.vue';
import UserLogin from 'src/components/UserLogin.vue'; 
import MainPage from 'src/components/MainPage.vue'; 

const routes: RouteRecordRaw[] = [
  { path: '/', component: UserRegister },
  { path: '/login', component: UserLogin },
  { path: '/main', component: MainPage }, 
];

export default routes;