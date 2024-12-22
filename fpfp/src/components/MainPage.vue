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
          <span class="task-column">Тема</span>
          <span class="task-column">Категория</span>
          <span class="task-column">Автор</span>
          <span class="task-column">Ответы</span>
        </div>
  
        <TaskList :searchQuery="searchQuery" /> 
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
  }
  
  .task-header {
    display: flex;
    justify-content: space-between;
    padding: 10px 0;
    color: white;
    font-weight: bold;
    margin-bottom: 10px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.3); 
  }
  
  .task-column {
    flex: 1;
    text-align: left;
    font-size: 16px; 
  }
  
  .top-menu {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    background: #0d1b2a;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    margin-top: -10px;
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