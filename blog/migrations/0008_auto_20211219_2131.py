# Generated by Django 3.0 on 2021-12-20 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_categoria_descripcion_corta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='descripcion',
            new_name='biografia',
        ),
        migrations.RemoveField(
            model_name='user',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nombre',
        ),
    ]
