# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requirement',
            old_name='name',
            new_name='requirement_name',
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='category',
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='number',
        ),
        migrations.AddField(
            model_name='requirementname',
            name='category',
            field=models.ForeignKey(default=1, to='level.Category'),
            preserve_default=False,
        ),
    ]
