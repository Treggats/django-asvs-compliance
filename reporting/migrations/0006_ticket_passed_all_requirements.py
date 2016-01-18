# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0005_auto_20160118_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='passed_all_requirements',
            field=models.BooleanField(default=False),
        ),
    ]
