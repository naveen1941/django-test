# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MPTTComment',
            fields=[
                ('comment_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, auto_created=True, to='comments.Comment')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(null=True, blank=True, related_name='children', to='commentsapp.MPTTComment')),
            ],
            options={
                'ordering': ['tree_id', 'lft'],
            },
            bases=('comments.comment', models.Model),
        ),
    ]
