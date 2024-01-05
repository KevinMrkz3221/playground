from django.urls import path, include


urlpatterns=[
    path('', include('portfolio.certification.urls')),
    path('', include('portfolio.experience.urls')),
    path('', include('portfolio.knowledge.urls')),
    path('', include('portfolio.project.urls')),
    path('', include('portfolio.skills.urls')),
]