# Generated by Django 5.0.1 on 2024-01-05 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0002_alter_certification_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certification',
            options={'ordering': ('-date',)},
        ),
    ]