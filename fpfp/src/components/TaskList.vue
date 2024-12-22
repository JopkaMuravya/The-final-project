<template>
    <div class="task-list">
      <ul class="task-container">
        <li v-for="task in tasks" :key="task.id" class="task-item">
          <div class="task-content">
            <h3 class="task-title">{{ task.title }}</h3>
            <p class="task-description">{{ task.description }}</p>
          </div>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'TaskList',
    props: ['searchQuery'],
    data() {
      return {
        tasks: [],
        socket: null,
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
          this.tasks = response.data;
        } catch (error) {
          console.error('Ошибка при загрузке задач:', error);
        }
      },
      setupWebSocket() {
        this.socket = new WebSocket('ws://localhost:8000/ws/tasks/');
        this.socket.onmessage = (event) => {
          const data = JSON.parse(event.data);
          this.tasks.push(data);
        };
        this.socket.onclose = () => {
          console.error('WebSocket закрыт');
        };
      },
    },
  };
  </script>
  
  <style scoped>
  .task-list {
    margin-top: 20px; 
  }
  
  .task-container {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .task-item {
    background: #ffffff;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 15px;
    margin-bottom: 15px; 
  }
  
  .task-content {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  
  .task-title {
    margin: 0;
    font-size: 16px;
    font-weight: bold;
    color: #1b263b;
  }
  
  .task-description {
    margin: 0;
    font-size: 14px;
    color: #555;
  }
  </style>
  