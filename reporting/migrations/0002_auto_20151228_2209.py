# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='client',
        ),
        migrations.AddField(
            model_name='project',
            name='client',
            field=models.ForeignKey(default='', to='reporting.Client'),
            preserve_default=False,
        ),
    ]
