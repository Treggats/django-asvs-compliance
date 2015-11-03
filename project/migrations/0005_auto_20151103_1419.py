# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0006_requirement_report'),
        ('project', '0004_auto_20151103_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='requirements',
        ),
        migrations.AddField(
            model_name='report',
            name='requirement',
            field=models.ForeignKey(to='level.Requirement', blank=True, null=True, related_name='report_requirement'),
        ),
    ]
