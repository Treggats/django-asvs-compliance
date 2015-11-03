# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0002_auto_20151103_0007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requirement',
            old_name='number',
            new_name='cat_nr',
        ),
    ]
