# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('asvsrequirement', '0014_auto_20151128_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationExplanation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('explanation', django_markdown.models.MarkdownField()),
            ],
        ),
        migrations.CreateModel(
            name='RelatedAnnotated',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('req_annotate_pk', models.PositiveIntegerField()),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Related annotations',
                'verbose_name': 'Related annotated',
            },
        ),
        migrations.CreateModel(
            name='RelatedAnnotatedTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=250)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='asvsannotation.RelatedAnnotated', editable=False, related_name='translations', null=True)),
            ],
            options={
                'db_tablespace': '',
                'abstract': False,
                'default_permissions': (),
                'db_table': 'asvsannotation_relatedannotated_translation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RequirementAnnotated',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('category', models.ForeignKey(to='asvsrequirement.Category')),
                ('relations', models.ManyToManyField(to='asvsannotation.RelatedAnnotated')),
                ('requirement', models.ForeignKey(to='asvsrequirement.Requirement')),
            ],
            options={
                'verbose_name_plural': 'Requirement annotations',
                'verbose_name': 'Requirement annotated',
                'ordering': ('requirement', 'category'),
            },
        ),
        migrations.CreateModel(
            name='RequirementAnnotatedTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='asvsannotation.RequirementAnnotated', editable=False, related_name='translations', null=True)),
            ],
            options={
                'db_tablespace': '',
                'abstract': False,
                'default_permissions': (),
                'db_table': 'asvsannotation_requirementannotated_translation',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='annotationexplanation',
            name='req_ann',
            field=models.ForeignKey(to='asvsannotation.RequirementAnnotated'),
        ),
        migrations.AlterUniqueTogether(
            name='requirementannotatedtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='requirementannotated',
            unique_together=set([('requirement', 'category')]),
        ),
        migrations.AlterUniqueTogether(
            name='relatedannotatedtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
