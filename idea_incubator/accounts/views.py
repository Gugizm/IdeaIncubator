from rest_framework import viewsets
from rest_framework.response import Response

from .models import Profile
from .serializer import ProfileSerializer


class ProfileListViewSet(viewsets.ViewSet):
    queryset = Profile.objects.all()

    def list(self, request):
        