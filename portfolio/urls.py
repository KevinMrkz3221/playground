from django.urls import path, include

from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('certifications/', include('portfolio.certification.urls')),
    path('experiences/', include('portfolio.experience.urls')),
    path('knowledges/', include('portfolio.knowledge.urls')),
    path('projects/', include('portfolio.project.urls')),
    path('skills/', include('portfolio.skills.urls')),
    path('docs/', include_docs_urls(title='Portfolio'))
]