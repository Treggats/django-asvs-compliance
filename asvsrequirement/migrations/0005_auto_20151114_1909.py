# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsrequirement', '0004_auto_20151111_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='asvsrequirement',
            field=models.ManyToManyField(to='asvsrequirement.Level'),
        ),
    ]
