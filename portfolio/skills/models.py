from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/skills', blank=True, null=True)
    level = models.CharField(max_length=200)
    percentage = models.IntegerField(blank=True, null = True)

    class Meta:
        db_table = 'skill'
        ordering = ('-percentage',)

    def __str__(self) -> str:
        return self.name