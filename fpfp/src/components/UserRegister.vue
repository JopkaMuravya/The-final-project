<template>
  <div>
    <h2>Регистрация</h2>
    <form @submit.prevent="register">
      <div>
        <label for="username">Имя пользователя:</label>
        <input type="text" v-model="username" required />
      </div>
      <div>
        <label for="password">Пароль:</label>
        <input type="password" v-model="password" required />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" v-model="email" required />
      </div>
      <div>
        <label for="avatar">Аватар:</label>
        <input type="file" @change="onFileChange" />
      </div>
      <button type="submit">Зарегистрироваться</button>
    </form>
    <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
    <div v-if="successMessage" class="success">{{ successMessage }}</div>
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
      email: '',
      avatar: null,
      errorMessage: '',
      successMessage: '',
    };
  },
  setup() {
    const router = useRouter(); 
    return { router };
  },
  methods: {
    onFileChange(event) {
      this.avatar = event.target.files[0];
    },
    async register() {
      const formData = new FormData();
      formData.append('username', this.username);
      formData.append('password', this.password);
      formData.append('email', this.email);
      if (this.avatar) {
        formData.append('avatar', this.avatar);
      }

      try {
        const response = await axios.post('http://localhost:8000/api/users/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        this.successMessage = 'Регистрация успешна!';
        this.errorMessage = '';
        console.log('Регистрация успешна:', response.data);
        this.router.push('/main');
      } catch (error) {
        this.errorMessage = 'Ошибка регистрации: ' + (error.response?.data?.detail || 'Неизвестная ошибка');
        this.successMessage = '';
        console.error('Ошибка регистрации:', error.response?.data);
      }
    },
  },
};
</script>

<style scoped>
.error {
  color: red;
}
.success {
  color: green;
}
</style>