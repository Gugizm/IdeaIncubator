from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import CustomUserViewSet, UserCreateAPIView

# router = routers.DefaultRouter()
# router.register(r"users", CustomUserViewSet, "User")

urlpatterns = [
    # path("", include(router.urls)),
    path("me", CustomUserViewSet.as_view(), name="current-user"),
    path("create", UserCreateAPIView.as_view(), name="user-create"),
    path("login", obtain_auth_token, name="login"),
]
