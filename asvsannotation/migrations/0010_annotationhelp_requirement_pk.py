# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsannotation', '0009_remove_annotation_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotationhelp',
            name='requirement_pk',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
