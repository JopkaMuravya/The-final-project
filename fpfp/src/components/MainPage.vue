<template>
    <div class="main-page">
      <SidebarMenu />
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
  
        <div class="task-header">
          <span class="task-column task-title-column">Тема</span>
          <span class="task-column task-author-column">Автор</span>
          <span class="task-column task-category-column">Категория</span>
          <span class="task-column task-reward-column">Вознаграждение</span>
        </div>
  
        <div class="task-list-wrapper">
          <TaskList :searchQuery="searchQuery" />
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import SidebarMenu from './SidebarMenu.vue';
  import TaskList from './TaskList.vue';
  import FilterIcon from '../assets/icons/filter.png';
  import AddIcon from '../assets/icons/add.png';
  
  export default defineComponent({
    name: 'MainPage',
    components: {
      SidebarMenu,
      TaskList,
    },
    data() {
      return {
        searchQuery: '',
        FilterIcon,
        AddIcon,
      };
    },
    methods: {
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
  
  .content {
    flex: 1;
    padding: 20px;
    display: flex;
    flex-direction: column;
    overflow: hidden; 
  }
  
  .task-header {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr;
    padding: 10px 0;
    color: white;
    font-weight: bold;
    margin-bottom: 10px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.3);
  }
  
  .task-column {
    text-align: left;
    font-size: 16px;
  }
  
  .task-list-wrapper {
    flex: 1; 
    overflow-y: auto; 
    padding-right: 10px; 
    scrollbar-width: thin; 
  }
  
  .task-list-wrapper::-webkit-scrollbar {
    width: 8px; 
  }
  
  .task-list-wrapper::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.5); 
    border-radius: 4px;
  }
  
  .task-list-wrapper::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.8); 
  }
  
  .task-title-column {
    text-align: left;
    margin-left: 15px;
  }
  
  .task-author-column {
    text-align: left;
    margin-left: 200px;
  }
  
  .task-category-column {
    text-align: left;
    margin-left: 100px;
  }
  
  .task-reward-column {
    text-align: left;
    margin-left: 40px;
  }
  
  .top-menu {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    background: #0d1b2a;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    margin-bottom: 10px;
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