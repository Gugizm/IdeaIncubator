from django.conf import settings
from django.db import models
from posts.models import Post


class Room(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
