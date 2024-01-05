from django.urls import path, include

from rest_framework import routers

from .views import CertificationViewSet

router = routers.DefaultRouter()
router.register(r'certifications', CertificationViewSet, 'certifications')


urlpatterns = [ 
    path('', include(router.urls))
]