from django.db import models
from django.contrib.auth.models import User
from idea_incubator.utils.upload_path import profile_picture_upload_path

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Profile_picture = models.ImageField(upload_to=profile_picture_upload_path, null=True, blank=True)
    about = models.TextField()

    def __str__(self):
        return self.user.username


