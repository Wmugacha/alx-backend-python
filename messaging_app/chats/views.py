from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import CustomUser, Message, Conversation
from .serializers import UserSerializer, MessageSerializer, ConversationSerializer, UserRegisterSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsMessageOwner, ConversationOwner


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('last_name', 'first_name')
    serializer_class = UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sender', 'conversation']
    permission_classes = [IsMessageOwner]


    def create(self, request, *args, **kwargs):
        conversation_id = request.data.get("conversation")
        message_body = request.data.get("message_body")

        if not conversation_id or not message_body:
            return Response({"error": "conversation and message_body are required"}, status=status.HTTP_400_BAD_REQUEST)
            
        conversation = get_object_or_404(Conversation, conversation_id=conversation_id)
        sender = request.user

        message = Message.objects.create(
            conversation=conversation,
            sender=sender,
            message_body=message_body
        )

        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['participants']
    permission_classes = [ConversationOwner]

    def create(self, request, *args, **kwargs):
        user_ids = request.data.get("participants")
        if not user_ids or not isinstance(user_ids, list):
            return Response({"error": "participants must be a list of user_ids"}, status=status.HTTP_400_BAD_REQUEST)

        conversation= Conversation.objects.create()
        conversation.participants.set(user_ids)
        conversation.save()

        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)