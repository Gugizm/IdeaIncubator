from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import Post


@receiver(pre_delete, sender=Post)
def category_delete_files(sender, instance, **kwargs):
    for field in instance._meta.fields:
        if field.name == "cover_photo":
            file = getattr(instance, field.name)
            if file:
                file.delete(save=False)
