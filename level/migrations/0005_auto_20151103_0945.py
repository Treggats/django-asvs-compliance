# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0004_requirement_req_nr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requirement',
            old_name='cat_nr',
            new_name='level_nr',
        ),
    ]
