# Generated by Django 5.0.1 on 2024-01-05 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0002_remove_task_experience_id_task_experience'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='experience',
            table='experience',
        ),
        migrations.AlterModelTable(
            name='task',
            table='task',
        ),
    ]