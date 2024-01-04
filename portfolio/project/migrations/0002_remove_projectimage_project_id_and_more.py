# Generated by Django 5.0.1 on 2024-01-03 22:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectimage',
            name='project_id',
        ),
        migrations.RemoveField(
            model_name='projecttag',
            name='project_id',
        ),
        migrations.RemoveField(
            model_name='technology',
            name='project_id',
        ),
        migrations.AddField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='project.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projecttag',
            name='project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='project.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technology',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='technologies', to='project.project'),
            preserve_default=False,
        ),
    ]