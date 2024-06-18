from django.urls import include, path
from rest_framework import routers

from .views import CommentModelViewSet

router = routers.DefaultRouter()
router.register(r"", CommentModelViewSet, "comment")

urlpatterns = [path("", include(router.urls))]
