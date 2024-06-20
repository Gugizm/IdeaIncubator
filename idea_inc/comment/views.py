from rest_framework import viewsets

from .models import Comment
from .schema import comment_list_docs
from .serializer import CommentSerializer


@comment_list_docs
class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
