# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsrequirement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('category_number',), 'verbose_name_plural': 'Categories', 'verbose_name': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='requirement',
            options={'ordering': ('requirement_number',)},
        ),
        migrations.AddField(
            model_name='requirement',
            name='asvsrequirement',
            field=models.ManyToManyField(to='asvsrequirement.Level'),
        ),
    ]
