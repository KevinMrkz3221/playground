from django.db import models

# Create your models here.
class Certification(models.Model):
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=100)
    date = models.DateField()
    file = models.FileField(upload_to='archivos/', blank=True, null=True)
    url = models.URLField()


    def __str__(self) -> str:
        return self.title
