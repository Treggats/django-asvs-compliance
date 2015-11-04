# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0002_auto_20151103_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('done', models.BooleanField()),
                ('level', models.ForeignKey(to='level.LevelNumber')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('signed', models.TextField()),
                ('project', models.ForeignKey(to='project.Project')),
                ('requirements', models.ForeignKey(to='level.Requirement')),
            ],
        ),
    ]
