# Generated by Django 5.0.1 on 2024-01-05 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_alter_skill_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('-percentage',)},
        ),
    ]
