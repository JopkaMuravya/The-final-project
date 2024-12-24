<template>
    <div class="single-task-page">
      <SidebarMenu />
      <div class="content">
        <div class="task-container">
          <div class="scrollable-content">
            <h2 class="task-title">{{ task.title }}</h2>
            <p class="task-description">{{ task.description }}</p>
            <div class="task-details">
              <div class="task-info">
                <span class="info-label">Категория: </span>
                <span
                  class="category-value"
                  :style="{ color: getCategoryColor(task.category) }"
                >
                  {{ task.category }}
                </span>
              </div>
              <div class="task-info">
                <span class="info-label">Вознаграждение: </span>
                {{ task.reward }}
                <img class="coin-icon" :src="CoinIcon" alt="Монеты" />
              </div>
              <div class="task-info">
                <span class="info-label">Автор: </span>
                {{ task.user?.username || 'Анонимус' }}
              </div>
            </div>
          </div>
          <button class="take-task-button" @click="takeTask">Взять задание</button>
        </div>
  
        <div class="chat-container">
          <div class="scrollable-content">
            <h3 class="chat-title">Чат с заказчиком</h3>
            <div class="chat-messages">
              <p class="chat-message"><strong>Заказчик:</strong> Добрый день, уточните, сможете ли выполнить до конца недели?</p>
              <p class="chat-message"><strong>Вы:</strong> Да, я смогу выполнить задание в указанный срок.</p>
            </div>
          </div>
          <div class="chat-input-container">
            <input
              type="text"
              class="chat-input"
              placeholder="Напишите сообщение..."
            />
            <button class="send-button">Отправить</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import SidebarMenu from './SidebarMenu.vue';
  import CoinIcon from '../assets/icons/coin.png';
  
  export default {
    name: 'SingleTask',
    components: {
      SidebarMenu,
    },
    data() {
      return {
        task: null,
        categories: [
          { name: 'Животные', color: '#FF5733' },
          { name: 'Здоровье', color: '#33FF57' },
          { name: 'Доставка', color: '#5733FF' },
          { name: 'Образование', color: '#FFC300' },
          { name: 'Ремонт', color: '#C70039' },
          { name: 'Садоводство', color: '#900C3F' },
          { name: 'Спорт', color: '#581845' },
          { name: 'Технологии', color: '#33FFF6' },
          { name: 'Транспорт', color: '#A569BD' },
          { name: 'Другое', color: '#7DCEA0' },
        ],
        CoinIcon,
      };
    },
    async created() {
      const taskId = this.$route.params.id;
      const token = localStorage.getItem('authToken');
      try {
        const response = await axios.get(`http://localhost:8000/api/tasks/${taskId}/`, {
          headers: {
            Authorization: `Token ${token}`,
          },
        });
        this.task = response.data;
      } catch (error) {
        console.error('Ошибка загрузки задачи:', error);
      }
    },
    methods: {
      getCategoryColor(categoryName) {
        const category = this.categories.find((cat) => cat.name === categoryName);
        return category ? category.color : '#ffffff';
      },
      async takeTask() {
        const taskId = this.$route.params.id;
        const token = localStorage.getItem('authToken');
        try {
          await axios.post(
            `http://localhost:8000/api/tasks/${taskId}/take/`,
            {},
            {
              headers: {
                Authorization: `Token ${token}`,
              },
            }
          );
          alert('Задание успешно взято!');
        } catch (error) {
          console.error('Ошибка при взятии задания:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .single-task-page {
    display: flex;
    height: 100vh;
    background: #1b263b;
    font-family: 'Arial', sans-serif;
    color: white;
  }
  
  .content {
    flex: 1;
    padding: 40px 20px;
    display: flex;
    gap: 20px;
  }
  
  .task-container,
  .chat-container {
    flex: 1;
    padding: 20px;
    background: #0d1b2a;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    display: flex;
    flex-direction: column;
  }
  
  .scrollable-content {
    flex: 1;
    overflow-y: auto;
    max-height: calc(100vh - 200px);
    margin-bottom: 20px;
  }
  
  .scrollable-content::-webkit-scrollbar {
    width: 8px;
  }
  
  .scrollable-content::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.3);
    border-radius: 4px;
  }
  
  .scrollable-content::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.5);
  }
  
  .task-title {
    font-size: 28px;
    margin-top: -5px;
    font-weight: bold;
    color: #ffffff;
    margin-bottom: 5px;
  }
  
  .task-description {
    font-size: 18px;
    line-height: 1.6;
    color: #cccccc;
    margin-bottom: 10px;
    text-align: justify;
  }
  
  .task-details {
    font-size: 16px;
    color: #e0e0e0;
  }
  
  .task-info {
    margin-bottom: 15px;
  }
  
  .info-label {
    font-weight: bold;
    color: #ffffff;
  }
  
  .category-value {
    font-weight: bold;
  }
  
  .coin-icon {
    width: 16px;
    height: 16px;
    margin-left: 5px;
  }
  
  .take-task-button {
    margin-top: 20px;
    padding: 15px 20px;
    background: #28a745;
    color: white;
    font-size: 18px;
    font-weight: bold;
    text-align: center;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s ease;
  }
  
  .take-task-button:hover {
    background: #218838;
  }
  
  .chat-title {
    margin-top: -5px;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 15px;
  }
  
  .chat-messages {
    flex: 1;
    overflow-y: auto;
    max-height: 200px;
    border: 1px solid #ddd;
    padding: 10px;
    border-radius: 5px;
    background: #1b263b;
  }
  
  .chat-message {
    margin-bottom: 10px;
    font-size: 14px;
    color: #ffffff;
  }
  
  .chat-input-container {
    margin-top: 100px;
    display: flex;
    gap: 10px;
    align-items: center;
  }
  
  .chat-input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 14px;
    height: 40px; 
  }
  
  .send-button {
    height: 40px; 
    padding: 0 20px; 
    background: #28a745;
    color: white;
    font-size: 14px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s ease;
  }
  
  .send-button:hover {
    background: #218838;
  }
  </style>
  