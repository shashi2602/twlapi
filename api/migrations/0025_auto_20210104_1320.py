# Generated by Django 3.1.3 on 2021-01-04 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20210102_2142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentsmodel',
            old_name='like',
            new_name='likes',
        ),
        migrations.RenameField(
            model_name='subcommentmodel',
            old_name='like',
            new_name='likes',
        ),
    ]
