from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import AccountUser


@receiver(post_save, sender=User)
def create_account_for_user(sender, instance, created, **kwargs):
    if created:
        AccountUser.objects.create(user=instance)


# TODO
# Getting RecursionError need to handle this
# @receiver(pre_delete, sender=AccountUser)
# def delete_user_with_account(sender, instance, **kwargs):
#     instance.user.delete()


@receiver(pre_delete, sender=AccountUser)
def category_delete_files(sender, instance, **kwargs):
    for field in instance._meta.fields:
        if field.name == "profile_picture":
            file = getattr(instance, field.name)
            if file:
                file.delete(save=False)
