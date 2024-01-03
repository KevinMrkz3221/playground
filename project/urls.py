from django.urls import path, include
from rest_framework import routers

from .views import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'projects',ProjectViewSet, 'projects')

urlpatterns = [
    path('api/v1/', include(router.urls))
]