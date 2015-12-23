# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsrequirement', '0002_auto_20151222_1609'),
        ('asvsannotation', '0010_annotationhelp_requirement_pk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotationhelp',
            name='requirement_pk',
        ),
        migrations.AddField(
            model_name='annotationhelp',
            name='requirement',
            field=models.ForeignKey(default=1, to='asvsrequirement.Requirement'),
            preserve_default=False,
        ),
    ]
