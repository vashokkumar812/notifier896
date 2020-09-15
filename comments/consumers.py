import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from channels.consumer import AsyncConsumer
from django.contrib.auth import authenticate, login
from .models import post,comment
import channels.layers
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.dispatch import receiver


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = {'message' : text_data_json['message'] , 'typing' : text_data_json['typing'],'me':text_data_json['me']}
        print(text_data)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )
        
        

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
        
        
        

class notConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        
        self.room_group_name = 'not_%s' % self.room_name
        global cus
        cus= self.room_name
        print(self.scope["user"])
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print("rg %s" % self.room_group_name)
        print("cn %s" % self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = {'message' : text_data_json['data']}
        print( 'this is received one' + text_data)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'comment_added',
                'message': message,
               
            }
        )
    def comment_added(self, event):
        # Send message to WebSocket
        
        self.send(text_data=json.dumps({
            'message': event
        }))
       