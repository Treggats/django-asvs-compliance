# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0006_auto_20151114_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedAnnotated',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RelatedAnnotatedTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(editable=False, related_name='translations', to='level.RelatedAnnotated', null=True)),
            ],
            options={
                'abstract': False,
                'managed': True,
                'db_tablespace': '',
                'db_table': 'level_relatedannotated_translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='RequirementAnnotated',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.ForeignKey(to='level.Category')),
                ('related', models.ForeignKey(to='level.RelatedAnnotated')),
                ('requirement', models.ForeignKey(to='level.Requirement')),
            ],
            options={
                'verbose_name': 'Requirement annotated',
                'verbose_name_plural': 'Requirement annotations',
            },
        ),
        migrations.CreateModel(
            name='RequirementAnnotatedTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(editable=False, related_name='translations', to='level.RequirementAnnotated', null=True)),
            ],
            options={
                'abstract': False,
                'managed': True,
                'db_tablespace': '',
                'db_table': 'level_requirementannotated_translation',
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='requirementannotatedtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='relatedannotatedtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
