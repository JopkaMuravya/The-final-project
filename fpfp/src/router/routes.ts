import type { RouteRecordRaw } from 'vue-router';
import UserRegister from 'src/components/UserRegister.vue';
import UserLogin from 'src/components/UserLogin.vue'; 
import MainPage from 'src/components/MainPage.vue';
import CreateTask from 'src/components/CreateTask.vue';

const routes: RouteRecordRaw[] = [
  { path: '/', component: UserRegister },
  { path: '/login', component: UserLogin },
  { path: '/main', component: MainPage },
  { path: '/create-task', component: CreateTask }, 
];

export default routes;