from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    percentage = models.IntegerField(blank=True, null = True)