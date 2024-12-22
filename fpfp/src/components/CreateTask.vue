<template>
    <div class="main-page">
      <aside class="sidebar">
        <div class="profile">
          <img class="avatar" :src="userAvatar" alt="Avatar" />
          <div class="profile-info">
            <p class="username">{{ username }}</p>
          </div>
        </div>
        <ul class="menu">
          <li>Главная</li>
          <li>Профиль</li>
          <li>Мои задания</li>
          <li>Рейтинг</li>
          <li>Поддержка</li>
        </ul>
      </aside>
      <div class="content">
        <h1 class="title">Создать задачу</h1>
        <!-- Дополнительное содержимое можно будет добавить сюда -->
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'CreateTask',
    data() {
      return {
        username: 'Пользователь',
        userAvatar: 'https://via.placeholder.com/60',
      };
    },
  });
  </script>
  
  <style scoped>
  .main-page {
    display: flex;
    height: 100vh;
    background: #1b263b;
  }
  
  .sidebar {
    width: 250px;
    background: #0d1b2a;
    padding: 20px;
    display: flex;
    flex-direction: column;
  }
  
  .profile {
    display: flex;
    align-items: center;
    background: #ffffff;
    padding: 10px;
    margin-bottom: 20px;
    border-radius: 8px;
  }
  
  .avatar {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    margin-right: 10px;
  }
  
  .profile-info {
    display: flex;
    flex-direction: column;
  }
  
  .username {
    font-weight: bold;
    color: #0d1b2a;
  }
  
  .menu {
    list-style: none;
    padding: 0;
  }
  
  .menu li {
    background: #ffffff;
    padding: 10px;
    margin-bottom: 10px;
    text-align: center;
    border-radius: 5px;
    font-weight: bold;
    color: #0d1b2a;
    cursor: pointer;
    transition: background 0.3s ease;
  }
  
  .menu li:hover {
    background: rgba(255, 255, 255, 0.9);
  }
  
  .content {
    flex: 1;
    padding: 20px;
    color: white;
  }
  
  .title {
    font-size: 24px;
    margin-bottom: 20px;
  }
  </style>  