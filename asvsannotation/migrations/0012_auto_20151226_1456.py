# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsannotation', '0011_auto_20151223_2319'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='annotationtypetranslation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='annotationtypetranslation',
            name='master',
        ),
        migrations.AddField(
            model_name='annotationtype',
            name='title',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AnnotationTypeTranslation',
        ),
    ]
