# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('asvsrequirement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationExplanation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('explanation', django_markdown.models.MarkdownField()),
            ],
        ),
        migrations.CreateModel(
            name='AnnotationExplanationType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='AnnotationRelation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('req_annotate_pk', models.PositiveIntegerField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='AnnotationRelationTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=250)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(null=True, related_name='translations', to='asvsannotation.AnnotationRelation', editable=False)),
            ],
            options={
                'abstract': False,
                'db_tablespace': '',
                'default_permissions': (),
                'managed': True,
                'db_table': 'asvsannotation_annotationrelation_translation',
            },
        ),
        migrations.CreateModel(
            name='AnnotationRequirement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('category', models.ForeignKey(to='asvsrequirement.Category')),
                ('relations', models.ManyToManyField(to='asvsannotation.AnnotationRelation')),
                ('requirement', models.ForeignKey(to='asvsrequirement.Requirement')),
            ],
            options={
                'ordering': ('requirement', 'category'),
            },
        ),
        migrations.CreateModel(
            name='AnnotationRequirementTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(null=True, related_name='translations', to='asvsannotation.AnnotationRequirement', editable=False)),
            ],
            options={
                'abstract': False,
                'db_tablespace': '',
                'default_permissions': (),
                'managed': True,
                'db_table': 'asvsannotation_annotationrequirement_translation',
            },
        ),
        migrations.AddField(
            model_name='annotationexplanation',
            name='req_ann',
            field=models.ForeignKey(to='asvsannotation.AnnotationRequirement'),
        ),
        migrations.AddField(
            model_name='annotationexplanation',
            name='type',
            field=models.ForeignKey(to='asvsannotation.AnnotationExplanationType'),
        ),
        migrations.AlterUniqueTogether(
            name='annotationrequirementtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='annotationrequirement',
            unique_together=set([('requirement', 'category')]),
        ),
        migrations.AlterUniqueTogether(
            name='annotationrelationtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
