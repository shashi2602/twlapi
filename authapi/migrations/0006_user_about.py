# Generated by Django 3.1.3 on 2021-01-08 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapi', '0005_user_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
