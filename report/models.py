from django.db import models
from project.models import Project
from level.models import Requirement


class Report(models.Model):
    project = models.ForeignKey(Project)
    requirements = models.ForeignKey(Requirement)
