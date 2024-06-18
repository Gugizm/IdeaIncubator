from rest_framework import viewsets

from .models import Skill
from .serializer import SkillSerializer


class SkillModelViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
