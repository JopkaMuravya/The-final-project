<template>
    <div class="main-page">
      <SidebarMenu />
      <div class="content">
        <h1 class="title">Создать задачу</h1>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import SidebarMenu from './SidebarMenu.vue'; // Импортируем компонент бокового меню
  
  export default defineComponent({
    name: 'CreateTask',
    components: {
      SidebarMenu, // Регистрируем компонент
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
    color: white;
  }
  .title {
    font-size: 24px;
    margin-bottom: 20px;
  }
  </style>  