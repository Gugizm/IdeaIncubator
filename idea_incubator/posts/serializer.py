from comments.serializer import CommentSerializer
from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"
