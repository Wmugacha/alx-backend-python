from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory
from .serializers import UserSerializer, MessageSerializer, NotificationSerializer, MessageHistorySerializer
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, method=['delete'], url_path='custom-delete')
    def delete_user(self, request, pk=None):
        user = self.get_object()
        user.delete()
        return Response({"message": "User deleted"}, status=status.HTTP_204_NO_CONTENT)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
    return Message.objects.filter(sender=self.request.user)


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
    return Notification.objects.filter(recipient=self.request.user)


class MessageHistoryViewSet(viewsets.ModelViewSet):
    queryset = MessageHistory.objects.all()
    serializer_class = MessageHistorySerializer