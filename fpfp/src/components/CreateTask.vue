<template>
    <div class="main-page">
      <SidebarMenu />
      <div class="content">
        <h1 class="title">Создать задание</h1>
        <form class="task-form">
          <div class="form-group">
            <label for="title">Заголовок</label>
            <input type="text" id="title" class="form-control" placeholder="Введите заголовок" />
          </div>
  
          <div class="form-group">
            <label for="description">Описание</label>
            <textarea id="description" class="form-control" placeholder="Опишите задание"></textarea>
          </div>
  
          <div class="form-row">
            <div class="form-group wider-width">
              <label for="category">Категория</label>
              <select id="category" class="form-control same-height">
                <option value="" disabled selected>Выберите категорию</option>
                <option value="design">Дизайн</option>
                <option value="development">Разработка</option>
                <option value="writing">Написание текста</option>
                <option value="other">Другое</option>
              </select>
            </div>
  
            <div class="form-group compact-width">
              <label for="reward">Вознаграждение</label>
              <div class="reward-wrapper">
                <input
                  type="number"
                  id="reward"
                  class="reward-input form-control same-height"
                  placeholder="0"
                />
                <img class="coin-icon" :src="CoinIcon" alt="Монеты" />
              </div>
            </div>
          </div>
  
          <div class="form-group">
            <label for="tags">Теги</label>
            <input type="text" id="tags" class="form-control" placeholder="Введите теги через запятую" />
          </div>
  
          <div class="form-group">
            <label for="files">Прикрепить файлы</label>
            <input type="file" id="files" class="form-control" multiple />
          </div>
  
          <div class="form-buttons">
            <button type="button" class="btn btn-secondary">Назад</button>
            <button type="button" class="btn btn-primary">Создать</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import SidebarMenu from './SidebarMenu.vue';
  import CoinIcon from '../assets/icons/coin.png'; 
  
  export default defineComponent({
    name: 'CreateTask',
    components: {
      SidebarMenu,
    },
    data() {
      return {
        CoinIcon, 
      };
    },
  });
  </script>
  
  <style scoped>
  .main-page {
    display: flex;
    height: 100vh;
    background: #1b263b;
    font-family: 'Arial', sans-serif;
    overflow-y: auto; 
  }
  
  .content {
    flex: 1;
    padding: 20px;
    color: white;
  }
  
  .title {
    font-size: 40px;
    margin-top: -10px;
    text-align: left;
    font-weight: bold;
  }
  
  .task-form {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  
  .form-group {
    display: flex;
    flex-direction: column;
  }
  
  .form-group label {
    margin-bottom: 8px;
    font-size: 16px;
    font-weight: bold;
  }
  
  .form-control {
    padding: 10px;
    font-size: 14px;
    border-radius: 5px;
    border: 1px solid #ccc;
  }
  
  textarea.form-control {
    resize: vertical;
  }
  
  .form-row {
    display: flex;
    gap: 20px;
    justify-content: flex-start; 
  }
  
  .wider-width {
    flex: 0 0 350px; 
  }
  
  .compact-width {
    flex: 0 0 150px; 
  }
  
  .reward-wrapper {
    display: flex;
    align-items: center;
    gap: 15px; 
  }
  
  .reward-input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 14px;
    text-align: left; 
  }
  
  .same-height {
    height: 42px; 
  }
  
  .coin-icon {
    width: 24px;
    height: 24px;
  }
  
  .form-buttons {
    display: flex;
    justify-content: flex-end; 
    gap: 10px; 
  }
  
  .btn {
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 5px;
    border: none;
    cursor: pointer;
    transition: background 0.3s ease;
  }
  
  .btn-primary {
    background-color: #007bff;
    color: white;
  }
  
  .btn-primary:hover {
    background-color: #0056b3;
  }
  
  .btn-secondary {
    background-color: #6c757d;
    color: white;
  }
  
  .btn-secondary:hover {
    background-color: #5a6268;
  }
  </style>  