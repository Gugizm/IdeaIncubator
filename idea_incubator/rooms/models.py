from django.db import models
from django.conf import settings
from posts.models import Post


class Room(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
