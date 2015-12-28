# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsrequirement', '0002_auto_20151222_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('level', models.ForeignKey(to='asvsrequirement.Level')),
                ('requirements', models.ManyToManyField(to='asvsrequirement.Requirement')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('release', models.CharField(max_length=40)),
                ('release_date', models.DateField()),
                ('generation_date', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(to='reporting.Client')),
                ('project', models.ForeignKey(to='reporting.Project')),
            ],
        ),
    ]
