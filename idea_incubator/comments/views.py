from rest_framework.exceptions import AuthenticationFailed
from rest_framework import viewsets

from .models import Comment
from .serializer import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset =  super().get_queryset()
        

