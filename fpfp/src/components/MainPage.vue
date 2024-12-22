<template>
    <div class="main-page">
      <aside class="sidebar">
        <div class="profile" @click="logout">
          <img class="avatar" :src="userAvatar" alt="Avatar" />
          <div class="profile-info">
            <p class="username">{{ username }}</p>
            <p class="level">Уровень: {{ userLevel }}</p>
            <p class="rank">Ранг: {{ userRank }}</p>
          </div>
          <div class="coins">
            <img class="coin-icon" :src="CoinIcon" alt="Coins" />
            <span>{{ userCoins }}</span>
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
        <div class="top-menu">
          <button class="filter-button">
            <img :src="FilterIcon" alt="Фильтрация" />
          </button>
          <input
            type="text"
            class="search-input"
            v-model="searchQuery"
            placeholder="Поиск..."
          />
          <button class="add-button" @click="createTask">
            <img :src="AddIcon" alt="Создать задачу" />
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import axios from 'axios';
  import FilterIcon from '../assets/icons/filter.png';
  import AddIcon from '../assets/icons/add.png';
  import CoinIcon from '../assets/icons/coin.png';
  
  export default defineComponent({
    name: 'MainPage',
    data() {
      return {
        username: '',
        userAvatar: 'https://via.placeholder.com/70',
        userLevel: 1,
        userRank: 'Новичок',
        userCoins: 0,
        searchQuery: '',
        FilterIcon,
        AddIcon,
        CoinIcon,
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
        this.userAvatar = `http://localhost:8000${response.data.avatar}`;
        this.userLevel = response.data.level || 1;
        this.userRank = response.data.rank || 'Новичок';
        this.userCoins = response.data.balance || 0;
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
      createTask() {
        this.$router.push('/create-task');
      },
    },
  });
  </script>
  
  <style scoped>
  .main-page {
    display: flex;
    height: 100vh;
    background: #1b263b;
    font-family: 'Arial', sans-serif;
  }
  
  .sidebar {
    width: 250px;
    background: #0d1b2a;
    padding: 20px;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .profile {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: #ffffff;
    border-radius: 8px;
    padding: 15px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    transition: background 0.3s ease;
    cursor: pointer;
    position: relative;
    width: 100%;
  }
  
  .profile:hover {
    background: rgba(255, 255, 255, 0.9);
  }
  
  .avatar {
    width: 70px;
    height: 70px;
    border-radius: 50%;
    margin-bottom: 10px;
    border: 3px solid #0d1b2a;
  }
  
  .profile-info {
    text-align: center;
    margin-bottom: 15px;
  }
  
  .username {
    color: #0d1b2a;
    font-weight: bold;
    font-size: 18px;
    margin: 5px 0;
  }
  
  .level,
  .rank {
    color: #7a7a7a;
    font-size: 14px;
    margin: 2px 0;
  }
  
  .coins {
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    bottom: 10px;
    gap: 5px;
  }
  
  .coin-icon {
    width: 18px;
    height: 18px;
    margin-right: 5px;
  }
  
  .menu {
    list-style: none;
    padding: 0;
    margin: 20px 0 0;
    width: 100%;
  }
  
  .menu li {
    margin: 10px 0;
    padding: 10px;
    background: #ffffff;
    color: #0d1b2a;
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
  }
  
  .top-menu {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    background: #0d1b2a;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    margin-top: -10px;
  }
  
  .search-input {
    flex: 1;
    height: 40px;
    margin: 0 10px;
    padding: 10px;
    border: none;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    color: #1b263b;
    font-weight: bold;
  }
  
  .filter-button,
  .add-button {
    height: 40px;
    background: #ffffff;
    border: none;
    border-radius: 5px;
    padding: 10px;
    cursor: pointer;
    transition: background 0.3s ease;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .filter-button:hover,
  .add-button:hover {
    background: rgba(255, 255, 255, 0.9);
  }
  
  .filter-button img,
  .add-button img {
    width: 24px;
    height: 24px;
  }
  </style>  