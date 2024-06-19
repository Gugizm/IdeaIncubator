from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone


class Notification(models.Model):
    COMMENT = "comment"
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    actor_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    actor_object_id = models.PositiveIntegerField()
    actor = GenericForeignKey("actor_content_type", "actor_object_id")
    timestamp = models.DateTimeField(default=timezone.now())

    ACTION_CHOICES = [
        (COMMENT, "Commented on your post"),
    ]
    action_type = models.CharField(max_length=20, choices=ACTION_CHOICES)
    is_read = models.BooleanField(default=False)
    read_timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.recipient} - {self.verb}"
