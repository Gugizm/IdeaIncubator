from comment.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone

from .models import Notification


@receiver(post_save, sender=Notification)
def update_read_timestaamp(sender, instance, created, **kwargs):
    if not created and instance.is_read and not instance.read_timestamp:
        instance.read_timestamp = timezone.now()
        instance.save()


@receiver(post_save, sender=Notification)
def delete_expired_notification(sender, instance, created, **kwargs):
    if not created and instance.is_read and instance.read_timestamp:
        expired_date = timezone.now() - timezone.timedelta(days=30)
        if instance.read_timestamp <= expired_date:
            instance.delete()


@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.post.owner,
            verb=Notification.COMMENT,
            actor_content_type=ContentType.objects.get_for_model(instance.owner),
            actor_object_id=instance.owner.id,
            action_type=Notification.COMMENT,
            timestamp=timezone.now(),
        )
