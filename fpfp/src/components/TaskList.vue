<template>
    <div class="task-list">
      <ul class="task-container">
        <li v-for="task in tasks" :key="task.id" class="task-item">
          <div class="task-content">
            <h3 class="task-title">{{ task.title }}</h3>
            <p class="task-description">{{ task.description }}</p>
            <div class="task-tags">
              <span v-for="tag in task.tags" :key="tag" class="tag">
                {{ tag }}
              </span>
            </div>
          </div>
          <div class="task-meta">
            <div class="user-section">
              <img
                v-if="task.user && task.user.avatar"
                class="user-avatar"
                :src="task.user.avatar"
                alt="Avatar"
              />
              <img
                v-else
                class="user-avatar"
                src="https://via.placeholder.com/40"
                alt="Default Avatar"
              />
              <p class="user-name">
                {{ task.user && task.user.username ? task.user.username : 'Анонимус' }}
              </p>
            </div>
            <div class="task-category">
              <span class="category-dot" :style="{ backgroundColor: task.categoryColor }"></span>
              {{ task.category }}
            </div>
            <div class="task-reward">
              <img class="reward-icon" :src="rewardIcon" alt="Монеты" />
              <span class="reward-amount">{{ task.reward }}</span>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import rewardIcon from '../assets/icons/coin.png';
  
  export default {
    name: 'TaskList',
    props: ['searchQuery'],
    data() {
      return {
        tasks: [],
        socket: null,
        rewardIcon,
      };
    },
    watch: {
      searchQuery() {
        this.loadTasks();
      },
    },
    async created() {
      await this.loadTasks();
      this.setupWebSocket();
    },
    beforeUnmount() {
      if (this.socket) {
        this.socket.close();
      }
    },
    methods: {
      async loadTasks() {
        try {
          const token = localStorage.getItem('authToken');
          const response = await axios.get('http://localhost:8000/api/tasks/', {
            headers: {
              Authorization: `Token ${token}`,
            },
            params: {
              search: this.searchQuery,
            },
          });
          this.tasks = response.data.map((task) => ({
            ...task,
            tags: task.tags ? task.tags.split(',').map((tag) => tag.trim()) : [],
            categoryColor: this.getCategoryColor(task.category),
          }));
        } catch (error) {
          console.error('Ошибка при загрузке задач:', error);
        }
      },
      setupWebSocket() {
        this.socket = new WebSocket('ws://localhost:8000/ws/tasks/');
        this.socket.onmessage = (event) => {
          const data = JSON.parse(event.data);
          data.tags = data.tags ? data.tags.split(',').map((tag) => tag.trim()) : [];
          data.categoryColor = this.getCategoryColor(data.category);
          this.tasks.push(data);
        };
        this.socket.onclose = () => {
          console.error('WebSocket закрыт');
        };
      },
      getCategoryColor(category) {
        const categoryColors = {
          Животные: '#FF5733',
          Здоровье: '#33FF57',
          Доставка: '#5733FF',
          Образование: '#FFC300',
          Ремонт: '#C70039',
          Садоводство: '#900C3F',
          Спорт: '#581845',
          Технологии: '#33FFF6',
          Транспорт: '#A569BD',
          Другое: '#7DCEA0',
        };
        return categoryColors[category] || '#555';
      },
    },
  };
  </script>
  
  <style scoped>
  .task-list {
    margin-top: 15px;
  }
  
  .task-container {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .task-item {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    background: #ffffff;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 5px 20px;
    margin-bottom: 15px;
  }
  
  .task-content {
    max-width: 50%;
  }
  
  .task-title {
    margin: 0 0 -10px;
    font-size: 18px;
    font-weight: bold;
    color: #1b263b;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  .task-description {
    margin: 0 0 10px;
    font-size: 14px;
    color: #555;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    line-clamp: 3;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  .task-tags {
    margin: 0 0 10px;
  }
  
  .tag {
    display: inline-block;
    background: #e0e0e0;
    color: #333;
    font-size: 12px;
    padding: 5px 10px;
    border-radius: 5px;
    margin-right: 5px;
  }
  
  .task-meta {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 10px;
  }
  
  .user-section {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  
  .user-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: #ddd;
    object-fit: cover;
  }
  
  .user-name {
    font-size: 14px;
    font-weight: bold;
    color: #333;
  }
  
  .task-category {
    font-size: 14px;
    color: #555;
    margin: 0;
    display: flex;
    align-items: center;
  }
  
  .category-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    margin-right: 5px;
  }
  
  .task-reward {
    display: flex;
    align-items: center;
    gap: 5px;
  }
  
  .reward-icon {
    width: 16px;
    height: 16px;
  }
  
  .reward-amount {
    font-size: 14px;
    color: #555;
  }
  </style>  