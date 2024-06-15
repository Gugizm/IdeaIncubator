from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('username', 'profile_picture', 'about')

    def get_username(self, obj):
        return obj.user.username if obj.user else None
