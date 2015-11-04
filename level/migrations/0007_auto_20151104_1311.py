# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0006_requirement_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='category',
            field=models.ForeignKey(to='level.Category', related_name='requirement_category'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('version', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='requirement',
            unique_together=set([('category', 'req_nr')]),
        ),
    ]
