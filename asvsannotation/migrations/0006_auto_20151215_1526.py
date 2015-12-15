# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsannotation', '0005_auto_20151215_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='annotation_help',
        ),
        migrations.AddField(
            model_name='annotation',
            name='annotation_help',
            field=models.ManyToManyField(to='asvsannotation.AnnotationHelp', blank=True),
        ),
    ]
