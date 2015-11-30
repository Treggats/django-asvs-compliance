# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asvsannotation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationExplanationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='annotationexplanation',
            name='type',
            field=models.ForeignKey(default=1, to='asvsannotation.AnnotationExplanationType'),
            preserve_default=False,
        ),
    ]
