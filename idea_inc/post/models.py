from core.models import Skill
from django.contrib.auth.models import User
from django.db import models
from utils.upload_path import post_img_upload_path


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover_photo = models.ImageField(
        upload_to=post_img_upload_path, null=True, blank=True
    )  # TODO add default photo
    skill = models.ManyToManyField(Skill, related_name="post_skill")
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
