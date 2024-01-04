from django.db import models

# Create your models here.

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    job_position = models.CharField(max_length=300)
    join_date = models.DateField()
    left_date = models.DateField()
    current = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title + ' | ' +self.company
    
class Task(models.Model):
    experience = models.ForeignKey(Experience, on_delete = models.CASCADE, related_name='tasks')
    note = models.CharField(max_length=400)


    def __str__(self) -> str:
        return self.experience.title