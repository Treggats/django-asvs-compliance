from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone

from asvsrequirement.models import Level, Requirement


@python_2_unicode_compatible
class Client(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=40)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    client = models.ForeignKey(Client)
    level = models.ForeignKey(Level)
    requirements = models.ManyToManyField(Requirement)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Report(models.Model):
    release_name = models.CharField(max_length=40)
    release_date = models.DateField(default=timezone.now)
    generation_date = models.DateField(auto_now_add=True)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.release
