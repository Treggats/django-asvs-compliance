# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsrequirement', '0013_auto_20151127_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotationexplanation',
            name='req_ann',
        ),
        migrations.AlterUniqueTogether(
            name='relatedannotatedtranslation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='relatedannotatedtranslation',
            name='master',
        ),
        migrations.AlterUniqueTogether(
            name='requirementannotated',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='requirementannotated',
            name='category',
        ),
        migrations.RemoveField(
            model_name='requirementannotated',
            name='relations',
        ),
        migrations.RemoveField(
            model_name='requirementannotated',
            name='requirement',
        ),
        migrations.AlterUniqueTogether(
            name='requirementannotatedtranslation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='requirementannotatedtranslation',
            name='master',
        ),
        migrations.DeleteModel(
            name='AnnotationExplanation',
        ),
        migrations.DeleteModel(
            name='RelatedAnnotated',
        ),
        migrations.DeleteModel(
            name='RelatedAnnotatedTranslation',
        ),
        migrations.DeleteModel(
            name='RequirementAnnotated',
        ),
        migrations.DeleteModel(
            name='RequirementAnnotatedTranslation',
        ),
    ]
