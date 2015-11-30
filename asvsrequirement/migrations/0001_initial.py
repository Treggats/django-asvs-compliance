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
                ('version_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('category_number', models.PositiveIntegerField()),
                ('version', models.ForeignKey(to='asvsrequirement.AsvsVersion')),
            ],
            options={
                'ordering': ('category_number',),
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(null=True, related_name='translations', to='asvsrequirement.Category', editable=False)),
            ],
            options={
                'abstract': False,
                'db_tablespace': '',
                'default_permissions': (),
                'managed': True,
                'db_table': 'asvsrequirement_category_translation',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('level_number', models.PositiveIntegerField()),
                ('version', models.ForeignKey(to='asvsrequirement.AsvsVersion')),
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
                ('master', models.ForeignKey(null=True, related_name='translations', to='asvsrequirement.Level', editable=False)),
            ],
            options={
                'abstract': False,
                'db_tablespace': '',
                'default_permissions': (),
                'managed': True,
                'db_table': 'asvsrequirement_level_translation',
            },
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('requirement_number', models.PositiveIntegerField()),
                ('category', models.ForeignKey(to='asvsrequirement.Category')),
                ('levels', models.ManyToManyField(to='asvsrequirement.Level')),
            ],
            options={
                'ordering': ('requirement_number', 'category'),
            },
        ),
        migrations.CreateModel(
            name='RequirementTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.TextField()),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(null=True, related_name='translations', to='asvsrequirement.Requirement', editable=False)),
            ],
            options={
                'abstract': False,
                'db_tablespace': '',
                'default_permissions': (),
                'managed': True,
                'db_table': 'asvsrequirement_requirement_translation',
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
