# Generated by Django 3.1.3 on 2020-12-01 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_postmodel_title_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='title_slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
