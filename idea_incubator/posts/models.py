from accounts.models import Profile
from django.db import models

from idea_incubator.utils.upload_path import post_img_upload_path


class Post(models.Model):
    title = models.CharField(max_length=200)
    cover_photo = models.ImageField(
        upload_to=post_img_upload_path, null=True, blank=True
    )
    description = models.TextField()
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="post_owner"
    )
    # applied_users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="applied_users", null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
