from rest_framework import serializers

from idea_inc.serializer import UserCreateSerializer

from .models import AccountUser


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = ["id", "user", "bio", "profile_picture", "skill"]
        read_only_fields = ["id", "user"]
