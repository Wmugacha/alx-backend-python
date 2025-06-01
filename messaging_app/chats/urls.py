from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .view import UserViewSet, ConversationViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'conversations', ConversationViewSet, basename='conversation')

urlpatterns = [
    path('api/', include(router.urls)),
]