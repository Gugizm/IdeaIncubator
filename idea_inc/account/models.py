from core.models import Skill
from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.upload_path import profile_picture_upload_path


class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to=profile_picture_upload_path, null=True, blank=True
    )
    skill = models.ManyToManyField(Skill, related_name="user_skill")
