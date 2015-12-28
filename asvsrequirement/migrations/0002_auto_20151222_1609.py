# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsrequirement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asvsversion',
            name='release_date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asvsversion',
            name='version_number',
            field=models.PositiveIntegerField(),
        ),
    ]
