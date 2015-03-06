# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import photo.models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20150304_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='thumbnail',
            field=models.ImageField(max_length=500, blank=True, upload_to=photo.models.get_upload_file_name_thumb, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=photo.models.get_upload_file_name),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photocategory',
            name='category',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
