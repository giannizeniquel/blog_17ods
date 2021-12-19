# Generated by Django 3.0 on 2021-12-18 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='estado',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='blog.Estado'),
        ),
        migrations.AlterField(
            model_name='user',
            name='rol',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='blog.Rol'),
        ),
    ]