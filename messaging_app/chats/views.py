from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser, Message, Conversation
from .serializers import UserSerializer, MessageSerializer, ConversationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('last_name', 'first_name')
    serializer_class = UserSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer