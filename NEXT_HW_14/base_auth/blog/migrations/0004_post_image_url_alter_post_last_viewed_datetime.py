# Generated by Django 5.0.4 on 2024-05-03 01:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_last_viewed_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_viewed_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 3, 1, 30, 57, 650127)),
        ),
    ]
