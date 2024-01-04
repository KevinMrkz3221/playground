from rest_framework import viewsets
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import ExperienceSerializer, Experience


# Create your views here

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class ExperienceViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienceSerializer
    queryset =  Experience.objects.all()