# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20151103_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='requirements',
            field=models.TextField(null=True, blank=True),
        ),
    ]
