from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, Skills

admin.site.register(Profile)
admin.site.register(Skills)
