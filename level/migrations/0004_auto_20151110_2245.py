# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0003_auto_20151110_1423'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('number',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterUniqueTogether(
            name='requirement',
            unique_together=set([]),
        ),
    ]
