# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsannotation', '0006_auto_20151215_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotationhelp',
            name='category',
        ),
        migrations.RemoveField(
            model_name='annotationhelp',
            name='requirement',
        ),
    ]
