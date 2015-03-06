# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import photo.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Photo Title:', max_length=100)),
                ('description', models.TextField(blank=True, verbose_name='Description: ', max_length=250)),
                ('category', models.CharField(verbose_name='Category :', max_length=100)),
                ('image', models.FileField(upload_to=photo.models.get_upload_file_name)),
                ('uploaded', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
