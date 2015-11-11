# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsvsVersion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('version_number', models.CharField(default='3', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('category_number', models.PositiveIntegerField()),
                ('version', models.ForeignKey(to='level.AsvsVersion')),
            ],
            options={
                'ordering': ('category_number',),
            },
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(to='level.Category', null=True, related_name='translations', editable=False)),
            ],
            options={
                'db_table': 'level_category_translation',
                'managed': True,
                'default_permissions': (),
                'abstract': False,
                'db_tablespace': '',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('level_number', models.PositiveIntegerField()),
                ('version', models.ForeignKey(to='level.AsvsVersion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LevelTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(to='level.Level', null=True, related_name='translations', editable=False)),
            ],
            options={
                'db_table': 'level_level_translation',
                'managed': True,
                'default_permissions': (),
                'abstract': False,
                'db_tablespace': '',
            },
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('requirement_number', models.PositiveIntegerField()),
                ('category', models.ForeignKey(to='level.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequirementTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.TextField()),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(to='level.Requirement', null=True, related_name='translations', editable=False)),
            ],
            options={
                'db_table': 'level_requirement_translation',
                'managed': True,
                'default_permissions': (),
                'abstract': False,
                'db_tablespace': '',
            },
        ),
        migrations.AlterUniqueTogether(
            name='requirementtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='leveltranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
