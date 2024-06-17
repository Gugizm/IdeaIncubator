from django.contrib.auth.models import User
from django.db import models

from idea_incubator.utils.upload_path import profile_picture_upload_path


class Skills(models.Model):
    skills = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.skills


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to=profile_picture_upload_path, null=True, blank=True
    )
    about = models.TextField(null=True, blank=True)
    skills = models.ManyToManyField(Skills, related_name="user_skills")
    other_skills = models.CharField(
        max_length=100,
        help_text="comma-seperated list of other skills.",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user.username
