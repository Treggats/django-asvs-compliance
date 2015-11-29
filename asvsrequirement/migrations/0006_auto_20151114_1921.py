# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsrequirement', '0005_auto_20151114_1909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requirement',
            old_name='asvsrequirement',
            new_name='levels',
        ),
    ]
