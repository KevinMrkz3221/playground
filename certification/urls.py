from django.urls import path, include

from rest_framework import routers

from .views import CertificationViewSet

router = routers.DefaultRouter()
router.register(r'certifications', CertificationViewSet, 'certification')


urlpatterns = [ 
    path('api/v1/', include(router.urls))
]