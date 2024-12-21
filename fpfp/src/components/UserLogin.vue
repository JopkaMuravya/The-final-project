<template>
    <div>
      <h2>Вход</h2>
      <form @submit.prevent="login">
        <div>
          <label for="username">Имя пользователя:</label>
          <input type="text" v-model="username" required />
        </div>
        <div>
          <label for="password">Пароль:</label>
          <input type="password" v-model="password" required />
        </div>
        <button type="submit">Войти</button>
      </form>
      <button @click="goToRegister">Зарегистрироваться</button>
      <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        errorMessage: '',
      };
    },
    setup() {
      const router = useRouter();
      return { router };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('http://localhost:8000/api/login/', {
            username: this.username,
            password: this.password,
          });
          const { token } = response.data;
          localStorage.setItem('authToken', token);
          this.errorMessage = '';
          this.router.push('/main');
        } catch (error) {
          this.errorMessage = 'Ошибка входа: Неверный логин или пароль';
          console.error('Ошибка входа:', error.response?.data);
        }
      },
      goToRegister() {
        this.router.push('/'); 
      },
    },
  };
  </script>
  
  <style scoped>
  .error {
    color: red;
  }
  </style>  