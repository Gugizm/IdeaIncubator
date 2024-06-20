from comment.serializer import CommentSerializer
from core.models import Skill
from core.serializer import SkillSerializer
from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # skill = SkillSerializer(many=True)
    # owner = UserPublicSerializer()
    post_comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "owner",
            "title",
            "description",
            "cover_photo",
            "skill",
            "created_date",
            "updated_date",
            "post_comment",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        skills = instance.skill.all()
        representation["skill"] = [skill.name for skill in skills]
        return representation
