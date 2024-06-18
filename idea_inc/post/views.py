from rest_framework import viewsets

from .filters import PostFilter
from .models import Post
from .pagination import PostPagination
from .serializer import PostSerializer


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    filterset_class = PostFilter
