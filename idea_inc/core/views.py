from rest_framework import viewsets

from .models import Skill
from .schema import core_list_docs
from .serializer import SkillSerializer


@core_list_docs
class SkillModelViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
