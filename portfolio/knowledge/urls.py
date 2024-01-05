from django.urls import path, include
from rest_framework import routers

from  .views import KnowledgeViewSet

router = routers.DefaultRouter()
router.register(r'knowledges', KnowledgeViewSet, 'knowledges')


urlpatterns = [
    path('', include(router.urls))
]