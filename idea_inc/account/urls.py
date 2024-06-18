from django.urls import include, path
from rest_framework import routers

from .views import CustomUserViewSet

router = routers.DefaultRouter()
router.register(r"users", CustomUserViewSet, "User")

urlpatterns = [
    path("", include(router.urls)),
]
