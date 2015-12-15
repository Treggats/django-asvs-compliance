# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsannotation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annotationhelp',
            options={'verbose_name': 'Annotation help text', 'verbose_name_plural': 'Annotation help texts'},
        ),
        migrations.AlterUniqueTogether(
            name='annotationhelp',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='annotationrelation',
            unique_together=set([]),
        ),
    ]
