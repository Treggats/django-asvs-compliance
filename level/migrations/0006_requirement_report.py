# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20151103_0915'),
        ('level', '0005_auto_20151103_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='report',
            field=models.ForeignKey(to='project.Report', blank=True, null=True, related_name='requirement_report'),
        ),
    ]
