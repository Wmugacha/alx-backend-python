from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory
from .serializers import UserSerializer, MessageSerializer, NotificationSerializer, MessageHistorySerializer
from rest_framework.response import Response
from django.http import JsonResponse
from django.db import models

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['delete'], url_path='custom-delete')
    def delete_user(self, request, pk=None):
        user = self.get_object()
        user.delete()
        return Response({"message": "User deleted"}, status=status.HTTP_204_NO_CONTENT)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user)

    @action(detail=False, methods=['get'])
    def unread(self, request):
        messages = Message.unread.for_user(request.user).only('sender_id', 'content', 'timestamp').select_related('sender')
        serializer = self.get_serializer(messages, many=True)
        return Response(serializer.data)

@action(detail=False, methods=['get'])
def inbox(request):
        messages = Message.objects.filter(sender=request.user).select_related('sender', 'receiver').prefetch_related('replies')
        serializer = MessageSerializer(messages, many=True)
        return JsonResponse(serializer.data, safe=False)

class UnreadMessagesManager(models.Manager):
    def for_user(self, user):
        return self.filter(receiver=user, is_read=False)


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer

    def get_queryset(self):
    return Notification.objects.filter(recipient=self.request.user)


class MessageHistoryViewSet(viewsets.ModelViewSet):
    queryset = MessageHistory.objects.all()
    serializer_class = MessageHistorySerializer