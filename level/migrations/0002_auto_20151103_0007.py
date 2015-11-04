# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='number',
            field=models.ManyToManyField(to='level.LevelNumber', related_name='level_nr'),
        ),
    ]
