from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile, Skills


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "email")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ["skills"]


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    skills = SkillsSerializer(many=True)

    class Meta:
        model = Profile
        fields = ["username", "profile_picture", "about", "skills"]
