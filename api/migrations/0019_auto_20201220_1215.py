# Generated by Django 3.1.3 on 2020-12-20 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20201220_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='tags',
            field=models.ManyToManyField(null=True, to='api.Tags'),
        ),
    ]