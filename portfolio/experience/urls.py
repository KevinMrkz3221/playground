from django.urls import path, include
from rest_framework import routers

from .views import ExperienceViewSet

router = routers.DefaultRouter()
router.register(r'experiences', ExperienceViewSet, 'experiences')

urlpatterns = [ 
    path('api/v1/', include(router.urls))
]