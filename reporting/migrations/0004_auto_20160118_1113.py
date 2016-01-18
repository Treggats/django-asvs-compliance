# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('asvsrequirement', '0002_auto_20151222_1609'),
        ('reporting', '0003_auto_20151228_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('requirements', models.ManyToManyField(to='asvsrequirement.Requirement')),
            ],
        ),
        migrations.AlterField(
            model_name='report',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
