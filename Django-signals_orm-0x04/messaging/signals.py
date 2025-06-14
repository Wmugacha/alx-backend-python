from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory

@receiver(post_save, sender=Message)
def new_message(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(message=instance)


@receiver(pre_save, sender=Message)
def edit_message(sender, instance, **kwargs):
    if instance.pk:
        old = Message.objects.get(pk=instance.pk)
        if old.content != instance.content:
            MessageHistory.objects.create(
                message = instance,
                content = old.content,
                edited_by = instance.sender
            )
            instance.edited = True