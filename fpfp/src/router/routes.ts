import type { RouteRecordRaw } from 'vue-router';
import UserRegister from 'src/components/UserRegister.vue';
import UserLogin from 'src/components/UserLogin.vue'; 
import MainPage from 'src/components/MainPage.vue';
import SingleTask from 'src/components/SingleTask.vue';
import CreateTask from 'src/components/CreateTask.vue';

const routes: RouteRecordRaw[] = [
  { path: '/', component: UserRegister },
  { path: '/login', component: UserLogin },
  { path: '/main', component: MainPage },
  { path: '/create-task', component: CreateTask },
  { path: '/task/:id', component: SingleTask }, 
];

export default routes;