# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsrequirement', '0010_auto_20151125_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatedannotated',
            name='req_annotate_pk',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
