# Generated by Django 3.1.3 on 2020-12-05 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_postmodel_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='likes',
        ),
    ]
