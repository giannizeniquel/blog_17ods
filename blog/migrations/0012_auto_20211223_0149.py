# Generated by Django 3.0 on 2021-12-23 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_user_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelTable(
            name='user',
            table='auth_user',
        ),
    ]