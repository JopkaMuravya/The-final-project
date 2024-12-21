<template>
    <div class="main-page">
      <aside class="sidebar">
        <div class="profile" @click="logout">
          <img class="avatar" :src="userAvatar" alt="Avatar" />
          <p class="username">{{ username }}</p>
        </div>
        <ul class="menu">
          <li>Главная</li>
          <li>Задания</li>
          <li>Профиль</li>
        </ul>
      </aside>
      <div class="content">
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'MainPage',
    data() {
      return {
        username: '',
        userAvatar: 'https://via.placeholder.com/60', 
      };
    },
    async created() {
      const token = localStorage.getItem('authToken');
      if (!token) {
        this.$router.push('/'); 
        return;
      }
      try {
        const response = await axios.get('http://localhost:8000/api/users/me/', {
          headers: { Authorization: `Token ${token}` },
        });
        this.username = response.data.username;
        this.userAvatar = `http://localhost:8000/${response.data.avatar}`; 
      } catch (error) {
        console.error('Ошибка загрузки данных пользователя:', error);
        this.$router.push('/');
      }
    },
    methods: {
      logout() {
        localStorage.removeItem('authToken');
        this.$router.push('/');
      },
    },
  };
  </script>  

<style scoped>
.main-page {
  display: flex;
  height: 100vh;
  background: linear-gradient(45deg, #f0f8ff, #e6ffe6); 
  font-family: 'Arial', sans-serif;
}

.sidebar {
  width: 250px;
  background: #0d1b2a; 
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}

.profile {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 15px;
  padding: 10px;
  background: #ffffff; 
  border-radius: 8px;
  width: 100%; 
  height: 110px; 
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: background 0.3s ease;
}

.profile:hover {
  background: rgba(255, 255, 255, 0.9); 
}

.avatar {
  width: 60px; 
  height: 60px;
  border-radius: 50%;
  margin-bottom: 5px;
  border: 2px solid #0d1b2a;
}

.username {
  color: #0d1b2a; 
  font-weight: bold;
  font-size: 16px;
  text-align: center;
}

.menu {
  list-style: none;
  padding: 0;
  margin: 0;
  width: 100%;
}

.menu li {
  margin: 10px 0;
  padding: 10px;
  background: #ffffff;
  color: #0d1b2a; 
  border: none;
  border-radius: 5px;
  text-align: center;
  cursor: pointer;
  transition: background 0.3s ease;
  font-weight: bold;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.menu li:hover {
  background: rgba(255, 255, 255, 0.9); 
}

.content {
  flex: 1;
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 24px;
  background: #1b263b; 
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.05);
}
</style>