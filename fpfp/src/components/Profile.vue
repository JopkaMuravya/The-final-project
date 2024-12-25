<template>
  <div class="bg">
    <div class="params">
      <p class="level">Уровень: {{ userLevel }}</p>
      <p class="rank">Ранг: {{ userRank }}</p>
      <div class="coins">
        <span>Баланс: {{ userCoins }}</span>
        <img class="coin-icon" :src="CoinIcon" alt="Coins" />
      </div>
    </div>
    <button class="back-button" @click="Backtomain">
      <img :src="BackIcon" alt="Назад" />
    </button>
    <div class="main-page">
      <img class="avatar" :src="userAvatar" alt="Avatar" />
      <div class="content">
        <div class="info">
          <div class="profile-info">
            <p class="username">{{ username }}</p>
            <p class="description">Всем привет! Меня зовут Ира! Я люблю помогать другим людям, так что смело можите обращаться ко мне:)</p>
            <button class="edit-button" @click="Edit">Редактировать</button>
          </div>
        </div>
        <div class="Ansvers">
          <h3>Отзывы</h3>
          <div class="reviews-scrollable">
            <ul class="review-list">
              <li v-for="(review, index) in reviews" :key="index" class="review-item">
                <img class="review-avatar" :src="review.avatar" alt="Avatar" />
                <div class="review-content">
                  <p class="review-text">{{ review.text }}</p>
                  <p class="review-author">— {{ review.author }}</p>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import axios from 'axios';
  import CoinIcon from '../assets/icons/coin.png';
  import BackIcon from '../assets/icons/back.png';
  
  export default defineComponent({
    name: 'YourProfile',
    components: {
    },
    data() {
      return {
        BackIcon,
        username: '',
        userAvatar: 'https://via.placeholder.com/70',
        userLevel: 1,
        userRank: 'Новичок',
        userCoins: 0,
        CoinIcon,
        reviews: [
          { text: 'Отличный сервис! ', author: 'Алексей', avatar: 'https://via.placeholder.com/70' },
          { text: 'Очень помогли, спасибо!', author: 'Мария', avatar: 'https://via.placeholder.com/70' },
          { text: 'Рекомендую всем!', author: 'Иван', avatar: 'https://via.placeholder.com/70' },
        ],
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
      Backtomain() {
        this.$router.push('/main');
      },
      Edit() {
        this.$router.push('/edit');
      },
    },
  });
  </script>
  
  <style scoped>
    .bg {
      display: flex;
      height: 100vh;
      background: #5c341e;
      font-family: 'Arial', sans-serif;
      position: relative;
      padding: 20px;
    }

    .params {
      display: flex;
      width: 250px;
      height: 20%;
      font-family: 'Arial', sans-serif;
      align-items: center;
      flex-direction: column;
      background: #fbceb1;
      border: none;
      border-radius: 20px;
      padding: 10px;
    }

    .back-button {
      height: 40px;
      background: #fbceb1;
      border: none;
      border-radius: 5px;
      padding: 10px;
      cursor: pointer;
      margin-left: -130px;
      margin-top: 21vh;
      transition: background 0.3s ease;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .back-button img {
      width: 24px;
      height: 24px;
    }

    .back-button:hover {
      background: rgba(255, 255, 255, 0.9);
    }

    .edit-button {
      background: #e66c28;
      color: papayawhip;
      border: none;
      border-radius: 5px;
      text-align: center;
      cursor: pointer;
      transition: background 0.3s ease;
      font-weight: bold;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .edit-button:hover {
      background: #c9302c;
    }

    .main-page {
      display: flex;
      border-radius: 20px;
      width: 100%;
      background-image: url("../assets/bg6.jpg");
      font-family: 'Arial', sans-serif;
      position: relative;
      overflow: hidden;
      flex-direction: column;
      justify-content: flex-end;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      transition: background 0.3s ease;
      margin-left: 110px;
    }

    .content {
      padding: 10px 20px;
      display: flex;
      flex-direction: row;
      overflow: hidden;
      background: #fbceb1;
      height: 65%;
      margin-top: auto;
      align-items: flex-start;
    }

    .info {
      text-align: left;
      width: 100%;
      font-size: 17px;
      margin-top: 8vh;
      margin-right: 20px;
      border-radius: 8px;
      padding: 15px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      transition: background 0.3s ease;
      width: 50%;
      background-color: papayawhip;
    }


    .avatar {
      width: 150px;
      height: 150px;
      border-radius: 50%;
      top: 25%;
      margin-left: 50px;
      border: 7px solid #fbceb1;
      position: absolute;
      z-index: 2;
    }


  .username {
    color: #5c341e;
    font-weight: bold;
    font-size: 40px;
    margin-bottom: -5px;
  }

  .level,
  .rank {
    color: #5c341e;
    font-size: 20px;
    margin: 2px 0;
  }

  .coin-icon {
    width: 25px;
    height: 25px;
    margin-left: 5px;
  }

    .coins {
      align-items: center;
      justify-content: flex-start;
      font-size: 20px;
      color: #5c341e;
      margin-bottom: 10px;
    }

    .Ansvers {
      font-size: 10px;
      margin-top: 1vh;
      margin-right: 20px;
      border: none;
      padding: 15px;
      width: 50%;
      max-width: 50%;
      
    }

    .Ansvers h3 {
      margin-left: 35%;
      color: #5c341e;
      font-weight: bold;
      font-size: 40px;
      margin-top: -5px;
    }

    .reviews-scrollable {
      margin-top: -30px;
      max-height: 300px; /* Максимальная высота для прокрутки */
      overflow-y: auto; /* Включаем вертикальную прокрутку */
      padding: 10px; /* Внутренние отступы */
    }

    .reviews-scrollable::-webkit-scrollbar {
      width: 8px; /* Ширина полосы прокрутки */
    }

    .reviews-scrollable::-webkit-scrollbar-track {
      background: #f1f1f1; /* Цвет фона полосы прокрутки */
      border-radius: 10px; /* Закругленные углы для трека */
    }

    .reviews-scrollable::-webkit-scrollbar-thumb {
      background: #5c341e; /* Цвет ползунка */
      border-radius: 10px; /* Закругленные углы для ползунка */
    }

    .review-list {
      list-style: none; /* Убираем маркеры списка */
      padding: 0; /* Убираем отступы */
      margin: 0; /* Убираем внешние отступы */
    }

    .review-item {
      display: flex; /* Используем flex для выравнивания аватарки и текста */
      align-items: flex-start; /* Выравнивание по верхнему краю */
      background: papayawhip; /* Цвет фона для отзыва */
      border-radius: 8px; /* Закругленные углы */
      padding: 10px; /* Внутренние отступы */
      margin-bottom: 10px; /* Отступ между отзывами */
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1); /* Тень для эффекта */
    }

    .review-avatar {
      width: 40px; /* Ширина аватарки */
      height: 40px; /* Высота аватарки */
      border-radius: 50%; /* Закругленные углы для аватарки */
      margin-right: 10px; /* Отступ справа от аватарки */
    }

    .review-content {
      flex: 1; /* Позволяет тексту занимать оставшееся пространство */
    }

    .review-text {
      font-size: 17px; /* Размер шрифта для текста отзыва */
      color: #333; /* Цвет текста */
    }

    .review-author {
      font-size: 14px; /* Размер шрифта для имени автора */
      color: #777; /* Цвет текста для имени автора */
      text-align: right; /* Выравнивание по правому краю */
      margin-top: 5px; /* Отступ сверху для имени автора */
    }

 
  </style>  
