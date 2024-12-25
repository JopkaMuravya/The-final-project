import type { RouteRecordRaw } from 'vue-router';
import UserRegister from 'src/components/UserRegister.vue';
import UserLogin from 'src/components/UserLogin.vue'; 
import MainPage from 'src/components/MainPage.vue';
import SingleTask from 'src/components/SingleTask.vue';
import CreateTask from 'src/components/CreateTask.vue';
import MyTasksPage from 'src/components/MyTasksPage.vue';
import YourProfile from 'src/components/Profile.vue';
import EditProfile from 'src/components/Edit.vue';

const routes: RouteRecordRaw[] = [
  { path: '/', component: UserRegister },
  { path: '/login', component: UserLogin },
  { path: '/main', component: MainPage },
  { path: '/create-task', component: CreateTask },
  { path: '/tasks', component: MyTasksPage },
  { path: '/task/:id', component: SingleTask }, 
  { path: '/profile', component: YourProfile },
  { path: '/edit', component: EditProfile },
];

export default routes;
