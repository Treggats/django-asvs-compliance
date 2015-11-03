from django.db import models
from level.models import LevelNumber, Requirement


class Project(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    level = models.ForeignKey(LevelNumber)
    done = models.BooleanField()


class Report(models.Model):
    project = models.ForeignKey(Project)
    requirements = models.ForeignKey(Requirement)
    signed = models.TextField()
