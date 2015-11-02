from django.db import models
from level.models import LevelNumber
from report.models import Report


class Project(models.Model):
    name = models.CharField()
    description = models.TextField()
    level = models.ForeignKey(LevelNumber)
    report = models.ForeignKey(Report)
    done = models.BooleanField()
    signed = models.TextField()
