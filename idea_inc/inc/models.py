from django.contrib.auth.models import User
from django.db import models
from post.models import Post


class Inc(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="inced_post")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="incer")
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.user.username} - {self.post.title}
