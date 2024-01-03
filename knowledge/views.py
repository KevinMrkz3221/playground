from rest_framework import viewsets

from .serializers import Knowledge, KnowledgeSerializer
# Create your views here.

class KnowledgeViewSet(viewsets.ModelViewSet):
    serializer_class = KnowledgeSerializer
    queryset = Knowledge.objects.all()