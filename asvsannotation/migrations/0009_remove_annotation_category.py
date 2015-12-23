# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsannotation', '0008_auto_20151223_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='category',
        ),
    ]
