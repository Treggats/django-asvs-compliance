# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0002_auto_20151107_1221'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='requirement',
            unique_together=set([('requirement_name', 'version')]),
        ),
    ]
