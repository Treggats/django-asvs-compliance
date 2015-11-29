# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsrequirement', '0014_auto_20151128_2313'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='categorytranslation',
            table='asvsrequirement_category_translation',
        ),
        migrations.AlterModelTable(
            name='leveltranslation',
            table='asvsrequirement_level_translation',
        ),
        migrations.AlterModelTable(
            name='requirementtranslation',
            table='asvsrequirement_requirement_translation',
        ),
    ]
