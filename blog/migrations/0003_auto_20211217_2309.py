# Generated by Django 3.0 on 2021-12-18 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211217_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='user',
            name='rol',
        ),
    ]