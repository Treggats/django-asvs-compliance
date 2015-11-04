# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20151103_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='signed',
            field=models.TextField(null=True, blank=True),
        ),
    ]
