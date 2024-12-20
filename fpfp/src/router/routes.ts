import type { RouteRecordRaw } from 'vue-router';
import UserRegister from 'src/components/UserRegister.vue';

const routes: RouteRecordRaw[] = [
  {path: '/', component: UserRegister},
];

export default routes;
