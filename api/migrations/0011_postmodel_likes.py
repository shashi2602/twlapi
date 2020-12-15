# Generated by Django 3.1.3 on 2020-12-05 16:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0010_remove_postmodel_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_like', to=settings.AUTH_USER_MODEL),
        ),
    ]