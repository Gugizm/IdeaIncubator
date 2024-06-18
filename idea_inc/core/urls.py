from django.urls import include, path
from rest_framework import routers

from .views import SkillModelViewSet

router = routers.DefaultRouter()
router.register(r"skill", SkillModelViewSet, "skill")

urlpatterns = [
    path("", include(router.urls)),
]
