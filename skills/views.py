from rest_framework import viewsets

from .serializers import Skill, SkillSerializer
# Create your views here.


class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()