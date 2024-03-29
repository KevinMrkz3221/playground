from django.urls import path, include
from rest_framework import routers

from .views import SkillViewSet

router = routers.DefaultRouter()

router.register(r'skills', SkillViewSet, 'skills')

urlpatterns = [
    path('', include(router.urls))
]