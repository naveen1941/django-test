# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20150305_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
            preserve_default=True,
        ),
    ]
