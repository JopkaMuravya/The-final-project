<template>
  <div class="userlogin">
    <div class="login-link-container">
      <p>Уже есть аккаунт?</p>
      <button @click="goToLogin">Войти</button>
    </div>
    <div class="main-page">
      <h1 class="main-menu-title">From people for people</h1>
      <h2 class="login-title">Создайте новую учётную запись</h2>
      <p class="description">Готовы изменить мир, зарабатывая при этом вознаграждения? Наше инновационное приложение позволяет вам помогать другим и получать помощь, когда это необходимо!</p>
      <form @submit.prevent="register">
        <div class="avatar-upload">
          <label for="avatar" class="avatar-label">
            <span v-if="avatar">Изменить аватар</span>
            <span v-else>Выберите аватар</span>
          </label>
          <input type="file" id="avatar" @change="onFileChange" accept="image/*" />
          <div v-if="avatarPreview" class="avatar-preview">
            <img :src="avatarPreview" alt="Avatar Preview" />
          </div>
        </div>
        <input type="text" v-model="username" placeholder="Имя пользователя" required />
        <input type="password" v-model="password" placeholder="Пароль" required />
        <input type="email" v-model="email" placeholder="Email" required />

        <button type="submit">Зарегистрироваться</button>
      </form>
      <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
      <div v-if="successMessage" class="success">{{ successMessage }}</div>
    </div>
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
      avatarPreview: null, 
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
      if (this.avatar) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.avatarPreview = e.target.result; 
        };
        reader.readAsDataURL(this.avatar);
      }
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
        const registrationResponse = await axios.post(
          'http://localhost:8000/api/users/',
          formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          }
        );
        console.log('Регистрация успешна:', registrationResponse.data);

        const loginResponse = await axios.post('http://localhost:8000/api/login/', {
          username: this.username,
          password: this.password,
        });

        const { token } = loginResponse.data;
        localStorage.setItem('authToken', token);

        this.successMessage = 'Регистрация и вход успешны!';
        this.errorMessage = '';
        this.router.push('/main'); 
      } catch (error) {
        this.errorMessage = 'Ошибка регистрации или входа: ' + (error.response?.data?.detail || 'Неизвестная ошибка');
        this.successMessage = '';
        console.error('Ошибка регистрации или входа:', error.response?.data);
      }
    },
    goToLogin() {
      this.router.push('/login');
    },
  },
};
</script>

<style scoped>
.userlogin {
  display: flex;
  height: 100vh;
  background: linear-gradient(to right, #5c341e, #8b5a2b); 
  font-family: 'Arial', sans-serif;
  position: relative;
  padding: 20px;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.main-menu-title {
  text-align: center; 
  position: relative;
  font-size: 40px;
  font-weight: bold;
  color: #5c341e;
  margin-top: -10px;
}

.main-menu-title::after {
  content: ''; 
  display: block;
  width: 60%; 
  height: 2px;
  background: #008cff; 
  margin: 5px auto 0; 
}

.login-title {
  color: #5c341e; 
  font-size: 28px; 
  font-weight: bold; 
  padding-bottom: 10px;
  margin-bottom: 10px;
  margin-top: -10px; 
  text-align: center;
}

.description {
  font-size: 16px; 
  color: #666; 
  text-align: center;
  margin-bottom: 20px;
  margin-left: 50px;
  width: 90%;
}

.main-page {
  display: flex;
  border-radius: 20px;
  width: 60%;
  background-color: rgba(255, 255, 255, 0.9);
  font-family: 'Arial', sans-serif;
  overflow: hidden;
  flex-direction: column;
  justify-content: center;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  transition: background 0.3s ease;
  margin: 20px 50px;
  padding: 20px;
}

.avatar-upload {
  display: flex;
  flex-direction: row;
  align-items: center;
/*  margin-right: 20px;*/
}

.avatar-label {
  background-color: #008cff;
  color: white;
  padding: 10px 20px;
  border-radius: 10px;
  cursor: pointer; 
  transition: background-color 0.3s ease;
  margin-right: 70px;

}

.avatar-label:hover {
  background-color: #005f99; /* Цвет фона при наведении */
}

input[type="file"] {
  display: none; /* Скрываем стандартное поле выбора файла */
}

.avatar-preview {
  margin-top: 10px; /* Отступ сверху */
  width: 100px; /* Ширина предварительного просмотра */
  height: 100px; /* Высота предварительного просмотра */
  border-radius: 50%; /* Закругленные углы для аватара */
  overflow: hidden; /* Скрываем лишнее */
  border: 2px solid #008cff; /* Граница для предварительного просмотра */
  display: flex; /* Используем flex для центрирования изображения */
  align-items: center; /* Центрирование по вертикали */
  justify-content: center; /* Центрирование по горизонтали */
}

.avatar-preview img {
  width: 100%; /* Ширина изображения */
  height: auto; /* Автоматическая высота */
}

.login-link-container {
  position: absolute;
  top: 30px; 
  right: 30px;
  display: flex;
  align-items: center;
  gap: 8px; 
}

.login-link-container p {
  color: white;
  font-size: 14px;
  font-family: 'Arial', sans-serif;
  margin: 0;
}

.login-link-container button {
  padding: 6px 12px;
  font-size: 12px;
  font-family: 'Arial', sans-serif;
  border: 2px solid rgba(255, 165, 0, 0.8);
  border-radius: 8px;
  background-color: rgba(255, 165, 0, 0.85);
  color: black;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.login-link-container button:hover {
  background-color: rgba(255, 140, 0, 0.9);
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  width: 320px;
  margin: 0 auto;
}

input {
  padding: 15px;
  width: 100%;
  border: 2px solid rgba(255, 255, 255, 0.8);
  border-radius: 10px;
  font-size: 16px;
  font-family: 'Arial', sans-serif;
  background-color: rgba(255, 255, 255, 0.85);
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  transition: border-color 0.3s ease, background-color 0.3s ease;
}

input:focus {
  outline: none;
  border-color: #008cff;
  background-color: rgba(255, 255, 255, 1); 
}

button {
  padding: 12px; 
  font-size: 14px;
  font-family: 'Arial', sans-serif;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  background-color: #333;
  color: white;
  text-transform: uppercase;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

button:hover {
  background-color: #555;
  transform: scale(1.05);
}

button[type="submit"] {
  background-color: #008cff;
  color: white;
  width: 100%;
  margin-bottom: 10px;
}

button[type="submit"]:hover {
  background-color: #005f99; 
}

.error {
  margin-top: 10px;
  color: red;
  font-size: 12px;
  font-family: 'Arial', sans-serif;
  text-align: center; 
}
.success {
  margin-top: 10px;
  color: green;
  font-size: 12px;
  font-family: 'Arial', sans-serif;
  text-align: center; 
}
</style>
