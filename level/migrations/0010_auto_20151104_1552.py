# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0009_auto_20151104_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='requirement',
        ),
        migrations.AddField(
            model_name='annotation',
            name='requirement',
            field=models.ManyToManyField(to='level.Requirement'),
        ),
    ]
