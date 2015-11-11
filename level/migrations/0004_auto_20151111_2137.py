# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0003_auto_20151111_1234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requirement',
            options={'ordering': ('requirement_number', 'category')},
        ),
        migrations.AlterField(
            model_name='asvsversion',
            name='version_number',
            field=models.CharField(max_length=10),
        ),
    ]
