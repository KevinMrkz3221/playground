# Generated by Django 5.0.1 on 2024-01-05 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_project_description'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='project',
            table='project',
        ),
        migrations.AlterModelTable(
            name='projectimage',
            table='project_image',
        ),
        migrations.AlterModelTable(
            name='projecttag',
            table='project_tag',
        ),
        migrations.AlterModelTable(
            name='technology',
            table='technology',
        ),
    ]