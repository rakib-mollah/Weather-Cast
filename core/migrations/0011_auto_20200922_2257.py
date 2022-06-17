# Generated by Django 3.0.5 on 2020-09-23 01:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0010_auto_20200921_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='user',
        ),
        migrations.AddField(
            model_name='city',
            name='user',
            field=models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]