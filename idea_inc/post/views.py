from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .filters import PostFilter
from .models import Post
from .pagination import PostPagination
from .schema import post_list_docs
from .serializer import PostSerializer


@post_list_docs
class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    filterset_class = PostFilter


# should change for post
