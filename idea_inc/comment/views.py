from rest_framework import viewsets

from .models import Comment
from .serializer import CommentSerializer


class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
