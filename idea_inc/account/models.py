from core.models import Skill
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import get_object_or_404
from utils.upload_path import profile_picture_upload_path


class AccountUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_account"
    )
    bio = models.TextField(max_length=500, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to=profile_picture_upload_path, null=True, blank=True
    )  # TODO add default photo
    skill = models.ManyToManyField(Skill, related_name="user_skill")

    def save(self, *args, **kwargs):
        if self.id:
            existing = get_object_or_404(AccountUser, id=self.id)
            if existing.profile_picture != self.profile_picture:
                existing.profile_picture.delete(save=False)
        super(AccountUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username
