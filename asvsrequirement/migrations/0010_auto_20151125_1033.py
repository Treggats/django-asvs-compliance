# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsrequirement', '0009_auto_20151124_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requirementannotated',
            old_name='related',
            new_name='relations',
        ),
    ]
