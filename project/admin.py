from django.contrib import admin
from .models import Project, ProjectTag, Technology, ProjectImage
# Register your models here.

admin.site.register(Project)
admin.site.register(ProjectTag)
admin.site.register(Technology)
admin.site.register(ProjectImage)
