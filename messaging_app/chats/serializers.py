from rest_framework import serializers
from .models import CustomUser, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    phone_number = serializers.CharField()


    class Meta:
        model = CustomUser
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'full_name']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def validate_phone_number(self, value):
        if not value.startswith('+'):
            raise serializers.ValidationError("Phone number must start with '+'.")
        return value

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ['message_id', 'conversation', 'sender', 'message_body', 'sent_at']


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at']