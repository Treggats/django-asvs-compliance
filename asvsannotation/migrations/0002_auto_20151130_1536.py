# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsannotation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationExplanationTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('explanation', models.TextField()),
                ('language_code', models.CharField(max_length=15, db_index=True)),
            ],
            options={
                'db_table': 'asvsannotation_annotationexplanation_translation',
                'default_permissions': (),
                'managed': True,
                'db_tablespace': '',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnnotationExplanationTypeTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('type', models.CharField(max_length=40)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
            ],
            options={
                'db_table': 'asvsannotation_annotationexplanationtype_translation',
                'default_permissions': (),
                'managed': True,
                'db_tablespace': '',
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='annotationexplanation',
            options={'ordering': ('id',)},
        ),
        migrations.RemoveField(
            model_name='annotationexplanation',
            name='explanation',
        ),
        migrations.RemoveField(
            model_name='annotationexplanationtype',
            name='type',
        ),
        migrations.AddField(
            model_name='annotationexplanationtypetranslation',
            name='master',
            field=models.ForeignKey(null=True, editable=False, to='asvsannotation.AnnotationExplanationType', related_name='translations'),
        ),
        migrations.AddField(
            model_name='annotationexplanationtranslation',
            name='master',
            field=models.ForeignKey(null=True, editable=False, to='asvsannotation.AnnotationExplanation', related_name='translations'),
        ),
        migrations.AlterUniqueTogether(
            name='annotationexplanationtypetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='annotationexplanationtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
