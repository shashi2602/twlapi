# Generated by Django 3.1.3 on 2020-12-03 10:16

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('api', '0007_auto_20201201_1838'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tagsmodel',
        ),
        migrations.AddField(
            model_name='placemodel',
            name='pname_slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='topicmodel',
            name='tpname_slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='overview',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.placemodel'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.topicmodel'),
        ),
    ]