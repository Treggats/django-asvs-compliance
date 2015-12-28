# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0002_auto_20151228_2209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='release',
            new_name='release_name',
        ),
    ]
