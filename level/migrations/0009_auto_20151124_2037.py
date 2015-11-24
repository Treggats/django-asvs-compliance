# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0008_auto_20151123_1130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requirementannotated',
            options={'ordering': ('requirement', 'category'), 'verbose_name': 'Requirement annotated', 'verbose_name_plural': 'Requirement annotations'},
        ),
        migrations.AlterUniqueTogether(
            name='requirementannotated',
            unique_together=set([('requirement', 'category')]),
        ),
    ]
