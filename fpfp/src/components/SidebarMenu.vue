<template>
    <aside class="sidebar">
      <div class="profile">
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
        <li
          v-for="(item, index) in menuItems"
          :key="index"
          @click="navigateTo(item.route)"
        >
          {{ item.label }}
        </li>
        <li class="logout" @click="logout">Выйти</li>
      </ul>
    </aside>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import axios from 'axios';
  import CoinIcon from '../assets/icons/coin.png';
  
  export default defineComponent({
    name: 'SidebarMenu',
    data() {
      return {
        username: '',
        userAvatar: 'https://via.placeholder.com/70',
        userLevel: 1,
        userRank: 'Новичок',
        userCoins: 0,
        menuItems: [
          { label: 'Главная', route: '/main' },
          { label: 'Профиль', route: '/profile' },
          { label: 'Мои задания', route: '/tasks' },
          { label: 'Рейтинг', route: '/rating' },
          { label: 'Поддержка', route: '/support' },
        ],
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
  
        this.username = '';
        this.userAvatar = 'https://via.placeholder.com/70';
        this.userLevel = 1;
        this.userRank = 'Новичок';
        this.userCoins = 0;
  
        this.$router.replace('/').then(() => {
          window.location.reload();
        });
      },
      navigateTo(route: string) {
        this.$router.push(route);
      },
    },
  });
  </script>
  
  <style scoped>
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
    position: relative;
    width: 100%;
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
  .menu li.logout {
    margin-top: 20px;
    background: #d9534f;
    color: white;
  }
  .menu li.logout:hover {
    background: #c9302c;
  }
  </style>  