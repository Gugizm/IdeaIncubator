from django.urls import include, path
from rest_framework import routers

from .views import PostModelViewSet

router = routers.DefaultRouter()
router.register(r"", PostModelViewSet, "post")

urlpatterns = [path("", include(router.urls))]
