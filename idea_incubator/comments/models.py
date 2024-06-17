from accounts.models import Profile
from django.db import models
from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comment"
    )
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="user_comment"
    )
    text = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.text[:90]}"
