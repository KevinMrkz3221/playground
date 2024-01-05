from django.db import models

# Create your models here.
class Knowledge(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/knowledge', blank=True, null=True)

    class Meta:
        db_table = 'knowledge'