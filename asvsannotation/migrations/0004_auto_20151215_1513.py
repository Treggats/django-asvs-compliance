# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsannotation', '0003_auto_20151215_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='relations',
            field=models.ManyToManyField(to='asvsannotation.AnnotationRelation', null=True, blank=True),
        ),
    ]
