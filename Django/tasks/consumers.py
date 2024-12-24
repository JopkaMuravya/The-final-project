import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("tasks", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("tasks", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            "tasks",
            {
                "type": "task_message",
                "message": data,
            },
        )

    async def task_message(self, event):
        await self.send(text_data=json.dumps(event["message"]))


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # # Получаем историю чата асинхронно
        # messages = await self.get_chat_history()
        # for message in messages:
        #     await self.send(text_data=json.dumps({
        #         'sender': message.sender.username,
        #         'message': message.message,
        #     }))


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        from users.models import Message
        from users.models import CustomUser
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']

        custom_user = await database_sync_to_async(CustomUser.objects.get)(username=sender)
        chat_message = Message(sender=custom_user, room_name=self.room_group_name, message=message)
        await database_sync_to_async(chat_message.save)()

        # Отправка сообщения в группу
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': custom_user.username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Отправка сообщения обратно клиенту
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
        }))

    # @database_sync_to_async
    # def get_chat_history(self):
    #     from users.models import Message
    #     return list(Message.objects.filter(room_name=self.room_group_name).order_by('timestamp').all())
