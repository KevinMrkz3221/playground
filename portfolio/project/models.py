from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github = models.URLField(blank=True, null=True)
    web = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'project'

    def __str__(self) -> str:
        return self.title

class ProjectTag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'project_tag'

    def __str__(self) -> str:
        return self.name

class Technology(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE, related_name='technologies')
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=200)

    class Meta:
        db_table = 'technology'

    def __str__(self) -> str:
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete= models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project/images', blank=True, null=True)
    
    class Meta:
        db_table = 'project_image'

    def __str__(self) -> str:
        return self.image.url