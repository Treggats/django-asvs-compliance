# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsannotation', '0007_auto_20151222_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotationrelation',
            name='category',
        ),
        migrations.RemoveField(
            model_name='annotationrelation',
            name='requirement',
        ),
    ]
