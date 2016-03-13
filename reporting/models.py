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

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('client_detail', args=[str(self.id)])


@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    client = models.ForeignKey(Client)
    level = models.ForeignKey(Level)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('project_detail', args=[str(self.id)])


@python_2_unicode_compatible
class Ticket(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project)
    requirements = models.ManyToManyField(Requirement)
    passed_all_requirements = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('project_detail', args=[str(self.project.id)])


@python_2_unicode_compatible
class Report(models.Model):
    release_name = models.CharField(max_length=40)
    release_date = models.DateField(default=timezone.now)
    comments = models.TextField(blank=True)
    generation_date = models.DateField(auto_now_add=True)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.release_name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('report_detail', args=[str(self.id)])
