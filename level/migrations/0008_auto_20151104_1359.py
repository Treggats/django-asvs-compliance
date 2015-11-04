# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0007_auto_20151104_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('version', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='requirement',
            name='version',
            field=models.ForeignKey(to='level.Version', default=3),
            preserve_default=False,
        ),
    ]
