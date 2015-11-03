# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0003_auto_20151103_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='req_nr',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
