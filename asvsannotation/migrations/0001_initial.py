# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsrequirement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='AnnotationHelp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='AnnotationHelpTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('help_text', models.TextField()),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, null=True, to='asvsannotation.AnnotationHelp')),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'asvsannotation_annotationhelp_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='AnnotationRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('url', models.URLField()),
                ('category', models.ForeignKey(to='asvsrequirement.Category')),
                ('requirement', models.ForeignKey(to='asvsrequirement.Requirement')),
            ],
        ),
        migrations.CreateModel(
            name='AnnotationRelationTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('relation_title', models.CharField(max_length=100)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, null=True, to='asvsannotation.AnnotationRelation')),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'asvsannotation_annotationrelation_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='AnnotationTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, null=True, to='asvsannotation.Annotation')),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'asvsannotation_annotation_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='AnnotationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnnotationTypeTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, null=True, to='asvsannotation.AnnotationType')),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'asvsannotation_annotationtype_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='annotationhelp',
            name='annotation_type',
            field=models.ForeignKey(to='asvsannotation.AnnotationType'),
        ),
        migrations.AddField(
            model_name='annotationhelp',
            name='category',
            field=models.ForeignKey(to='asvsrequirement.Category'),
        ),
        migrations.AddField(
            model_name='annotationhelp',
            name='requirement',
            field=models.ForeignKey(to='asvsrequirement.Requirement'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='annotation_help',
            field=models.ForeignKey(blank=True, to='asvsannotation.AnnotationHelp', null=True),
        ),
        migrations.AddField(
            model_name='annotation',
            name='category',
            field=models.ForeignKey(to='asvsrequirement.Category'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='relations',
            field=models.ManyToManyField(to='asvsannotation.AnnotationRelation'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='requirement',
            field=models.ForeignKey(to='asvsrequirement.Requirement'),
        ),
        migrations.AlterUniqueTogether(
            name='annotationtypetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='annotationtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='annotationrelationtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='annotationrelation',
            unique_together=set([('requirement', 'category')]),
        ),
        migrations.AlterUniqueTogether(
            name='annotationhelptranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='annotationhelp',
            unique_together=set([('requirement', 'category')]),
        ),
        migrations.AlterUniqueTogether(
            name='annotation',
            unique_together=set([('requirement', 'category')]),
        ),
    ]
