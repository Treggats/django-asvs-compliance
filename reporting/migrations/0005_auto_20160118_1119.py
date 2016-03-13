# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0004_auto_20160118_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='requirements',
        ),
        migrations.AddField(
            model_name='project',
            name='tickets',
            field=models.ManyToManyField(to='reporting.Ticket'),
        ),
    ]
