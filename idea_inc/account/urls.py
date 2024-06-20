from django.urls import include, path
from rest_framework import routers

from .views import AccountModelViewSet

router = routers.DefaultRouter()
router.register(r"", AccountModelViewSet, "account")

urlpatterns = [
    path("", include(router.urls)),
]
