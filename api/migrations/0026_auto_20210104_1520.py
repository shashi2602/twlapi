# Generated by Django 3.1.3 on 2021-01-04 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20210104_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsmodel',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='subcommentmodel',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
