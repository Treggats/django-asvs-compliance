# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0010_auto_20151104_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='related',
            field=models.ForeignKey(null=True, blank=True, to='level.AnnotationRelated'),
        ),
    ]
