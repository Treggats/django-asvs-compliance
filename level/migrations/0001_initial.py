# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('version', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='LevelNumber',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('number', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['number'],
                'verbose_name': 'level number',
            },
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(to='level.Category')),
                ('number', models.ManyToManyField(to='level.LevelNumber')),
            ],
            options={
                'verbose_name': 'requirement',
            },
        ),
    ]
