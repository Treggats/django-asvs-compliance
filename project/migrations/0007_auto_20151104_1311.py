# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0007_auto_20151104_1311'),
        ('project', '0006_report_requirements'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='requirement',
        ),
        migrations.RemoveField(
            model_name='report',
            name='requirements',
        ),
        migrations.AddField(
            model_name='report',
            name='requirements',
            field=models.ManyToManyField(related_name='report_requirements', blank=True, to='level.Requirement'),
        ),
    ]
