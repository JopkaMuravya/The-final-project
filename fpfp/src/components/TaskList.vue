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
            <div class="circle-placeholder"></div>
            <p class="task-category">{{ task.category }}</p>
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
          this.tasks = response.data.map(task => ({
            ...task,
            tags: task.tags ? task.tags.split(',').map(tag => tag.trim()) : [],
          }));
        } catch (error) {
          console.error('Ошибка при загрузке задач:', error);
        }
      },
      setupWebSocket() {
        this.socket = new WebSocket('ws://localhost:8000/ws/tasks/');
        this.socket.onmessage = (event) => {
          const data = JSON.parse(event.data);
          if (data.tags) {
            data.tags = data.tags.split(',').map(tag => tag.trim());
          }
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
  }
  
  .circle-placeholder {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: #ddd;
    margin-bottom: 5px;
  }
  
  .task-category {
    font-size: 14px;
    color: #555;
    margin: 0;
    text-align: center;
  }
  </style>  