<template>
    <div class="single-task-page">
        <SidebarMenu />
        <div class="content">
            <div class="task-container">
                <div class="scrollable-content">
                    <h2 class="task-title">{{ task.title }}</h2>
                    <p class="task-description">{{ task.description }}</p>

                    <div v-if="task.image" class="task-image-wrapper">
                        <img 
                            :src="task.image" 
                            alt="Изображение задания" 
                            class="task-image" 
                            @click="showImageModal = true"
                        />
                    </div>

                    <div class="task-details">
                        <div class="task-info">
                            <span class="info-label">Категория: </span>
                            <span class="category-value" :style="{ color: getCategoryColor(task.category) }">
                                {{ task.category }}
                            </span>
                        </div>
                        <div class="task-info">
                            <span class="info-label">Дата создания: </span>
                            {{ formatDate(task.created_at) }}
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

                <template v-if="task.user?.username === currentUser.username">
                    <div class="task-status">
                        <p><strong>Вы автор этого задания.</strong></p>
                        <p>
                            Статус:
                            <span v-if="task.executor">
                                Задание взято исполнителем {{ task.executor.username }}
                                <button class="complete-task-button" @click="markAsCompleted">
                                    Задание выполнено
                                </button>
                            </span>
                            <span v-else>Задание пока никем не взято</span>
                        </p>
                    </div>
                </template>

                <template v-else>
                    <button v-if="task.executor" class="take-task-button" disabled>
                        {{ task.executor.username === currentUser.username ? 'Ваше задание' : 'Задание уже взято' }}
                    </button>
                    <button v-else class="take-task-button" @click="takeTask">
                        Взять задание
                    </button>
                </template>
            </div>

            <!-- Модальное окно -->
            <div v-if="showImageModal" class="modal-overlay" @click="closeModal">
                <div class="modal-content" @click.stop>
                    <button class="close-button" @click="closeModal">×</button>
                    <img :src="task.image" alt="Изображение задания" class="modal-image" />
                </div>
            </div>

            <div class="chat-container" v-if="isChatAccessible">
              <div class="scrollable-content">
                <h3 class="chat-title">
                  {{ task.user?.username === currentUser ?.username ? "Чат с исполнителем" : "Чат с заказчиком" }}
                </h3>
                <div class="chat-messages">
                  <div v-for="(msg, index) in messages" :key="index" class="chat-message">
                    <strong>{{ msg.sender }}:</strong> {{ msg.message }}
                  </div>
                </div>
              </div>
              <div class="chat-input-container">
                <input
                  type="text"
                  class="chat-input"
                  v-model="newMessage"
                  placeholder="Напишите сообщение..."
                  :disabled="!isChatAccessible"
                />
                <button
                  class="send-button"
                  :disabled="!isChatAccessible || !newMessage"
                  @click="sendMessage"
                >
                  Отправить
                </button>
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
      currentUser: null,
      isChatAccessible: false,
      showImageModal: false,
      messages: [],
      newMessage: '',
      socket: null,
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
      // Получение данных задания
      const response = await axios.get(`http://localhost:8000/api/tasks/${taskId}/`, {
        headers: {
          Authorization: `Token ${token}`,
        },
      });
      this.task = response.data;

      // Получение текущего пользователя
      const userResponse = await axios.get('http://localhost:8000/api/users/me/', {
        headers: {
          Authorization: `Token ${token}`,
        },
      });
      this.currentUser  = userResponse.data;

      // Проверка доступа к чату
      if (this.task.executor || this.task.user.username === this.currentUser .username) {
        this.isChatAccessible = true;
      }

      // Подключение к WebSocket
      this.connectToWebSocket(taskId);
    } catch (error) {
      console.error('Ошибка загрузки данных:', error);
    }
  },
  methods: {
    getCategoryColor(categoryName) {
      const category = this.categories.find((cat) => cat.name === categoryName);
      return category ? category.color : '#ffffff';
    },
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('ru-RU', options);
    },
    closeModal() {
      this.showImageModal = false;
    },
    async takeTask() {
      const taskId = this.$route.params.id;
      const token = localStorage.getItem('authToken');
      try {
        const response = await axios.post(
          `http://localhost:8000/api/tasks/${taskId}/take/`,
          {},
          {
            headers: {
              Authorization: `Token ${token}`,
            },
          }
        );
        this.task = response.data;
        alert('Задание успешно взято!');
        this.isChatAccessible = true;
      } catch (error) {
        const errorMessage = error.response?.data?.error || 'Ошибка при взятии задания';
        alert(errorMessage);
        console.error('Ошибка:', errorMessage);
      }
    },
    async markAsCompleted() {
      const taskId = this.$route.params.id;
      const token = localStorage.getItem('authToken');
      try {
        await axios.post(
          `http://localhost:8000/api/tasks/${taskId}/complete/`,
          {},
          {
            headers: {
              Authorization: `Token ${token}`,
            },
          }
        );
        alert('Задание успешно помечено как выполненное!');
        this.task.executor = null;
      } catch (error) {
        console.error('Ошибка при завершении задания:', error);
      }
    },
    connectToWebSocket(taskId) {
    this.socket = new WebSocket(`ws://localhost:8000/ws/chat/${taskId}/`);

    this.socket.onopen = () => {
      console.log('WebSocket подключен');
    };

    this.socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.sender && data.message) {
        this.messages.push(data);
      } else {
        console.error('Получено пустое сообщение:', data);
      }
    };

    this.socket.onclose = () => {
      console.log('WebSocket закрыт');
      // Попробуйте переподключиться через некоторое время
      setTimeout(() => {
        this.connectToWebSocket(taskId);
      }, 5000); // 5 секунд
    };

    this.socket.onerror = (error) => {
      console.error('WebSocket ошибка:', error);
    };
  },
    sendMessage() {
      if (this.newMessage.trim() !== '') {
        const messageData = {
          sender: this.currentUser .username,
          message: this.newMessage,
        };
        console.log(this.newMessage)
        console.log(this.currentUser.username)
        this.socket.send(JSON.stringify(messageData));
        this.newMessage = '';
      }
    },
  },
};
</script>
 
  
<style scoped>
  .complete-task-button {
    margin-left: 10px;
    padding: 8px 12px;
    background: #ffc107;
    color: #1b263b;
    font-size: 14px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s ease;
}

.complete-task-button:hover {
    background: #e0a800;
}

.task-image-wrapper {
    margin-top: 20px;
    text-align: left;
}

.task-image {
    max-width: 200px;
    max-height: 150px;
    border-radius: 5px;
    cursor: pointer;
    transition: transform 0.3s;
    margin-bottom: 10px;
    margin-top: -5px;
}

.task-image:hover {
    transform: scale(1.05);
}

.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.9);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.modal-content {
    position: relative;
    background: #222;
    padding: 10px;
    border-radius: 10px;
    max-width: 80%;
    max-height: 80%;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal-image {
    max-width: 100%;
    max-height: 100%;
    border-radius: 5px;
}

.close-button {
    position: absolute;
    top: 10px;
    right: 10px;
    background: #ff5555;
    border: none;
    font-size: 18px;
    cursor: pointer;
    color: white;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: background 0.3s;
}

.close-button:hover {
    background: #ff2222;
}

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

.task-status {
    font-size: 16px;
    margin-top: 10px;
    color: #ffffff;
}

.task-status p {
    margin: 5px 0;
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