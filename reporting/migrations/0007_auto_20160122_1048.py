# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0006_ticket_passed_all_requirements'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='tickets',
        ),
        migrations.AddField(
            model_name='ticket',
            name='project',
            field=models.ForeignKey(default=1, to='reporting.Project'),
            preserve_default=False,
        ),
    ]
