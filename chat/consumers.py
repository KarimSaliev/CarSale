import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from chat.models import Message


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['type'] == 'fetch_initial_messages':
            # Handle request for initial messages
            initial_messages = self.fetch_initial_messages()
            self.send(text_data=json.dumps({
                'type': 'initial_messages',
                'messages': initial_messages
            }))
        else:
            sender = self.scope['user']  # Assuming sender information is available in the WebSocket scope
            username = sender.username
            message_content = username + ': ' + text_data_json['message']
            # Create a new Message object and save it to the database
            message = Message.objects.create(sender=sender, content=message_content, thread_name=self.room_group_name)
            message.save()

            # Broadcast the message to other users in the same room
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name, {"type": "chat.message", "message": message_content}
            )


    # Receive message from room group
    def chat_message(self, event):
        username = self.scope['user'].username
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message, 'username':username}))

    def fetch_initial_messages(self):
        # Retrieve the last, let's say, 10 messages for the current chat room
        last_messages = Message.objects.filter(thread_name=self.room_group_name)
        # Serialize messages to a list of strings
        initial_messages = [message.content for message in last_messages]
        return initial_messages