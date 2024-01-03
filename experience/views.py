from rest_framework import viewsets

from .serializers import ExperienceSerializer, Experience
# Create your views here


class ExperienceViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienceSerializer
    queryset =  Experience.objects.all()