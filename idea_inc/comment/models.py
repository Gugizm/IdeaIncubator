from django.contrib.auth.models import User
from django.db import models
from post.models import Post


class Comment(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_owner"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comment"
    )
    comment = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.post} - {self.owner} - {self.comment}"
