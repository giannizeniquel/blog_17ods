# Generated by Django 3.0 on 2021-12-18 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211217_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.Estado'),
        ),
        migrations.AddField(
            model_name='user',
            name='rol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.Rol'),
        ),
    ]
