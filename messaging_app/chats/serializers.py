from rest_framework import serializers
from .models import CustomUser, Conversation, Message

class UserSeializer(serializers.ModelSerializer):
    class meta:
        model = CustomUser
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'phone_number']

class ConversationSerializer(serializers.ModelSerializer):
    class meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    class meta:
        model = Message
        fields = ['message_id', 'conversation', 'sender', 'message_body', 'sent_at']