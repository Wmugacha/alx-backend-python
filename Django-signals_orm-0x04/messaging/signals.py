from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, Notification

@receiver(post_save, sender=Message)
def new_message(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(message=instance)