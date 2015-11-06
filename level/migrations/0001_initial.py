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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('version_number', models.CharField(default='3', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('category_number', models.PositiveIntegerField()),
                ('lang_code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LevelName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('level_number', models.PositiveIntegerField()),
                ('lang_code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.PositiveSmallIntegerField()),
                ('category', models.ForeignKey(to='level.Category')),
            ],
        ),
        migrations.CreateModel(
            name='RequirementName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('requirement_number', models.PositiveIntegerField()),
                ('lang_code', models.CharField(max_length=5)),
                ('title', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='requirement',
            name='name',
            field=models.ForeignKey(to='level.RequirementName'),
        ),
        migrations.AddField(
            model_name='requirement',
            name='version',
            field=models.ForeignKey(default='3', to='level.AsvsVersion'),
        ),
        migrations.AddField(
            model_name='level',
            name='name',
            field=models.ForeignKey(to='level.LevelName'),
        ),
        migrations.AddField(
            model_name='level',
            name='version',
            field=models.ForeignKey(default='3', to='level.AsvsVersion'),
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.ForeignKey(to='level.CategoryName'),
        ),
        migrations.AddField(
            model_name='category',
            name='version',
            field=models.ForeignKey(default='3', to='level.AsvsVersion'),
        ),
    ]
