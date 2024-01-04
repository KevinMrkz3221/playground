from rest_framework import viewsets
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import Skill, SkillSerializer
# Create your views here.

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()