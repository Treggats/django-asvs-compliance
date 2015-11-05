# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0011_auto_20151104_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lang_code', models.CharField(verbose_name='Language code', max_length=10)),
                ('title', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Annotation title',
            },
        ),
        migrations.AlterModelOptions(
            name='annotationrelated',
            options={'verbose_name': 'Annotation related'},
        ),
        migrations.AlterField(
            model_name='annotation',
            name='title',
            field=models.ForeignKey(to='level.AnnotationTitle'),
        ),
    ]
