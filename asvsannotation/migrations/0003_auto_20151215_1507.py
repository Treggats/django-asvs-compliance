# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsannotation', '0002_auto_20151215_1349'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='annotation',
            unique_together=set([]),
        ),
    ]
