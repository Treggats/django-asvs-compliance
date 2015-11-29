from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    level = models.ForeignKey('asvsrequirement.Level')
    done = models.BooleanField()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Report(models.Model):
    name = models.CharField(max_length=40, default="")
    project = models.ForeignKey(Project)
    requirements = models.ManyToManyField('asvsrequirement.Requirement',
                                          related_name='report_requirements',
                                          blank=True)
    signed = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
