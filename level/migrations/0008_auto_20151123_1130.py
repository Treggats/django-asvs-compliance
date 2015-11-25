# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0007_auto_20151123_1055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relatedannotated',
            options={'verbose_name_plural': 'Related annotations', 'verbose_name': 'Related annotated'},
        ),
        migrations.RemoveField(
            model_name='requirementannotated',
            name='related',
        ),
        migrations.AddField(
            model_name='requirementannotated',
            name='related',
            field=models.ManyToManyField(to='level.RelatedAnnotated'),
        ),
    ]
