# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0008_auto_20151104_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.ForeignKey(to='level.Category')),
            ],
        ),
        migrations.CreateModel(
            name='AnnotationRelated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name': 'ASVS version'},
        ),
        migrations.AlterField(
            model_name='requirement',
            name='level_nr',
            field=models.ManyToManyField(to='level.LevelNumber', related_name='level_nr', verbose_name='Level number'),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='req_nr',
            field=models.PositiveSmallIntegerField(verbose_name='Requirement number'),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='version',
            field=models.ForeignKey(to='level.Version', verbose_name='ASVS version'),
        ),
        migrations.AlterField(
            model_name='version',
            name='version',
            field=models.CharField(max_length=5, verbose_name='ASVS version'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='related',
            field=models.ForeignKey(to='level.AnnotationRelated'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='requirement',
            field=models.ForeignKey(to='level.Requirement'),
        ),
    ]
