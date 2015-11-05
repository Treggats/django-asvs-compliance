# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0012_auto_20151105_1032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annotation',
            options={'verbose_name': 'Annotation'},
        ),
        migrations.AlterModelOptions(
            name='annotationrelated',
            options={'verbose_name_plural': 'Annotation related', 'verbose_name': 'Annotation related'},
        ),
    ]
