<template>
    <div class="main-page">
      <SidebarMenu />
      <div class="content">
        <h1 class="title">Создать задание</h1>
        <form class="task-form" @submit.prevent="createTask">
          <div class="form-group">
            <label for="title" class="form-label">Заголовок</label>
            <input
              type="text"
              id="title"
              class="form-control"
              v-model="title"
              placeholder="Введите заголовок"
              required
            />
          </div>
  
          <div class="form-group">
            <label for="description" class="form-label">Описание</label>
            <div class="icon-buttons">
              <button type="button" class="icon-button">
                <img :src="BoldIcon" alt="Bold" />
              </button>
              <button type="button" class="icon-button">
                <img :src="ItalicIcon" alt="Italic" />
              </button>
              <button type="button" class="icon-button">
                <img :src="UnderlineIcon" alt="Underline" />
              </button>
            </div>
            <textarea
              id="description"
              class="form-control"
              v-model="description"
              placeholder="Опишите задание"
              required
            ></textarea>
          </div>
  
          <div class="form-row">
            <div class="form-group wider-width">
              <label for="category" class="form-label">Категория</label>
              <select
                id="category"
                class="form-control same-height"
                v-model="category"
                required
              >
                <option value="" disabled selected>Выберите категорию</option>
                <option value="design">Дизайн</option>
                <option value="development">Разработка</option>
                <option value="writing">Написание текста</option>
                <option value="other">Другое</option>
              </select>
            </div>
  
            <div class="form-group compact-width">
              <label for="reward" class="form-label">Вознаграждение</label>
              <div class="reward-wrapper">
                <input
                  type="number"
                  id="reward"
                  class="reward-input form-control same-height"
                  v-model="reward"
                  placeholder="0"
                  min="0"
                />
                <img class="coin-icon" :src="CoinIcon" alt="Монеты" />
              </div>
            </div>
          </div>
  
          <div class="form-group">
            <label for="tags" class="form-label">Теги</label>
            <input
              type="text"
              id="tags"
              class="form-control"
              v-model="tags"
              placeholder="Введите теги через запятую"
            />
          </div>
  
          <div class="form-group">
            <label for="files" class="form-label">Прикрепить файлы</label>
            <input
              type="file"
              id="files"
              class="form-control"
              multiple
              @change="handleFileUpload"
            />
          </div>
  
          <div class="form-buttons">
            <button type="button" class="btn btn-secondary" @click="goBack">
              Назад
            </button>
            <button type="submit" class="btn btn-primary">
              Создать
            </button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import axios from 'axios';
  import SidebarMenu from './SidebarMenu.vue';
  import CoinIcon from '../assets/icons/coin.png';
  import BoldIcon from '../assets/icons/bold.png';
  import ItalicIcon from '../assets/icons/italic.png';
  import UnderlineIcon from '../assets/icons/underlined.png';
  
  export default defineComponent({
    name: 'CreateTask',
    components: {
      SidebarMenu,
    },
    data() {
      return {
        CoinIcon,
        BoldIcon,
        ItalicIcon,
        UnderlineIcon,
        title: '',
        description: '',
        category: '',
        reward: 0,
        tags: '',
        files: [] as File[],
      };
    },
    methods: {
      handleFileUpload(event: Event) {
        const target = event.target as HTMLInputElement;
        if (target.files) {
          this.files = Array.from(target.files);
        }
      },
      async createTask() {
        try {
          const token = localStorage.getItem('authToken');
          if (!token) throw new Error('Вы не авторизованы.');
  
          const formData = new FormData();
          formData.append('title', this.title);
          formData.append('description', this.description);
          formData.append('category', this.category);
          formData.append('reward', this.reward.toString());
          formData.append('tags', this.tags);
          this.files.forEach((file) => formData.append('files', file));
  
          const response = await axios.post('http://localhost:8000/api/tasks/', formData, {
            headers: {
              Authorization: `Token ${token}`,
              'Content-Type': 'multipart/form-data',
            },
          });
          alert('Задание успешно создано!');
          console.log(response.data);
        } catch (error) {
          console.error('Ошибка при создании задания:', error);
          alert('Ошибка при создании задания.');
        }
      },
      goBack() {
        window.history.back();
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
    gap: 25px; 
  }
  
  .form-group {
    margin-top: -10px;
    display: flex;
    flex-direction: column;
    gap: 3px;
  }
  
  .form-label {
    font-size: 18px;
    font-weight: bold;
  }
  
  .icon-buttons {
    display: flex;
    gap: 10px;
    margin-bottom: 10px;
  }
  
  .icon-button {
    background: white;
    border: 1px solid #ccc;
    border-radius: 5px;
    cursor: pointer;
    width: 30px;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background-color 0.3s ease;
  }
  
  .icon-button:hover {
    background-color: #f0f0f0;
  }
  
  .icon-button img {
    width: 20px;
    height: 20px;
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
    gap: 25px; 
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