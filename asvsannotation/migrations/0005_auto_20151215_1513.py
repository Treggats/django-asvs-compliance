# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsannotation', '0004_auto_20151215_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='relations',
            field=models.ManyToManyField(to='asvsannotation.AnnotationRelation', blank=True),
        ),
    ]
