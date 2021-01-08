# Generated by Django 3.1.3 on 2020-12-20 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20201219_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='postmodel',
            name='tags',
            field=models.ManyToManyField(to='api.Tags'),
        ),
    ]
