from rest_framework import viewsets


from .serializers import CertificationSerializer, Certification
# Create your views here.


class CertificationViewSet(viewsets.ModelViewSet):
    serializer_class = CertificationSerializer
    queryset = Certification.objects.all()