from core.models import Skill
from django.conf import settings
from django.db import models
from utils.upload_path import post_img_upload_path


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owner"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover_photo = models.ImageField(
        upload_to=post_img_upload_path, null=True, blank=True
    )  # should add default photo
    skill = models.ManyToManyField(Skill, related_name="post_skill")
