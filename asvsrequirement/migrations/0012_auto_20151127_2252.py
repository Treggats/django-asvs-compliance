# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('asvsrequirement', '0011_relatedannotated_req_annotate_pk'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationExplanation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('req_ann', models.ForeignKey(to='asvsrequirement.RequirementAnnotated')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnnotationExplanationTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('explanation', django_markdown.models.MarkdownField()),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(null=True, to='asvsrequirement.AnnotationExplanation', editable=False, related_name='translations')),
            ],
            options={
                'default_permissions': (),
                'managed': True,
                'db_table': 'level_annotationexplanation_translation',
                'abstract': False,
                'db_tablespace': '',
            },
        ),
        migrations.AlterUniqueTogether(
            name='annotationexplanationtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
