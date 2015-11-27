# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0012_auto_20151127_2252'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='annotationexplanationtranslation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='annotationexplanationtranslation',
            name='master',
        ),
        migrations.AddField(
            model_name='annotationexplanation',
            name='explanation',
            field=django_markdown.models.MarkdownField(default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AnnotationExplanationTranslation',
        ),
    ]
