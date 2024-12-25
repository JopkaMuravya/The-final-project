<template>
  <div class="bg">
    <div class="content">
      <h2 class="save-title">Редактирование аккаунта</h2>
      <div class="prevavatar">
        <img class="avatar" :src="userAvatar" alt="Avatar" />
        <button class="avatar-button" @click="newavatar">Изменить</button>
      </div>
      <div class="info">
        <div class="profile-info">
          <div class="labels">
            <label class="username_label">Имя:</label>
            <label class="email_label">Почта:</label>
            <label class="description_label">Краткая информация о вас:</label>
          </div>
          <div class="inputs">
            <p class="username">{{ username }}</p>
            <p class="email">ira.egorova.2005@bk.ru</p>
            <p class="description">Всем привет! Меня зовут Ира! Я люблю помогать другим людям, так что смело можите обращаться ко мне:)</p>

          </div>
        </div>
      </div>
      <button class="save-button" @click="Save">Сохранить изменения</button>
    </div>
   
  </div>
 
</template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import axios from 'axios';
  
  export default defineComponent({
    name: 'EditProfile',
    components: {
    },
    data() {
      return {
        username: '',
        userAvatar: 'https://via.placeholder.com/70', 
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
      } catch (error) {
        console.error('Ошибка загрузки данных пользователя:', error);
        this.$router.push('/');
      }
    },
    methods: {
      newavatar() {
        this.$router.push('/profile');
      },
      Save() {
        this.$router.push('/profile');
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

    .content {
      display: flex;
      border-radius: 20px;
      width: 100%;
      background: #fbceb1;
      font-family: 'Arial', sans-serif;
      position: relative;
      overflow: hidden;
      flex-direction: column;
/*      justify-content: center;*/
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      transition: background 0.3s ease;
      margin-left: 7vw;
      margin-right: 7vw;
      padding: 10px 20px;
      align-items: center;
    }

    .save-title {
      color: #5c341e;
      font-size: 55px;
      font-weight: bold;
      padding-bottom: 10px;
      margin-bottom: 10px;
      margin-top: 5px;
      text-align: center;
    }


    .prevavatar {
      display: flex;
      flex-direction: row;
      justify-content: center;
      width: 50%;
      font-size: 17px;
      align-items: center;
    }

    .avatar {
      width: 160px;
      height: 160px;
      border-radius: 50%;
      top: 50px;
      margin-left: 50px;
      border: 2px solid #5c341e;
      position: relative;
      margin-right: 30px;
    }

    .avatar-button {
      background: #e66c28;
      color: papayawhip;
      border: none;
      border-radius: 5px;
      text-align: center;
      cursor: pointer;
      transition: background 0.3s ease;
      font-weight: bold;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      margin-top: 12vh;
    }

    .profile-info {
      display: flex;
      flex-direction: row;
      justify-content: center;
      width: 100%;
      font-size: 20px;
      align-items: center;
      margin-left: 5vw;
    }

    .labels {

      display: flex;
      text-align: left;
      flex-direction: column;
     
     
      margin-right: 20px;
      padding: 15px;
      max-width: 30%;
      gap: 10px;
      
    }

    .inputs {
      display: flex;
      flex-direction: column;
      text-align: left;
      
      
      margin-top: 8vh;
      margin-right: 20px;
      padding: 15px;
      max-width: 30%;
      gap: 10px;
    }

/*    .username {
      font-size: 17px;
      margin-bottom: -5px;
    }*/


  .save-button {
    font-size: 17px;
    background: #e66c28;
    color: papayawhip;
    border: none;
    border-radius: 5px;
    text-align: center;
    cursor: pointer;
    transition: background 0.3s ease;
    font-weight: bold;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    margin-left: -50px;
  }

  .save-button:hover {
    background: #c9302c;
  }

 
  </style>  
