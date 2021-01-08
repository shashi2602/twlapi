# Generated by Django 3.1.3 on 2020-12-19 06:47

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('api', '0013_postmodel_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]