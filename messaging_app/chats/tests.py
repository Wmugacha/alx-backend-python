from django.test import TestCase
# chats/tests.py
import pytest
from django.utils import timezone
from .models import CustomUser, Conversation, Message

@pytest.mark.django_db
def test_create_message():
    # Create users
    user1 = CustomUser.objects.create_user(username='user1', email='user1@example.com', password='testpass123')
    user2 = CustomUser.objects.create_user(username='user2', email='user2@example.com', password='testpass123')

    # Create a conversation
    conversation = Conversation.objects.create()
    conversation.participants.add(user1, user2)

    # Create a message
    message = Message.objects.create(
        conversation=conversation,
        sender=user1,
        message_body="Hello there!",
        sent_at=timezone.now()
    )

    # Assertions
    assert message.message_id is not None
    assert message.sender == user1
    assert message.conversation == conversation
    assert message.message_body == "Hello there!"
    assert message in conversation.messages.all()
