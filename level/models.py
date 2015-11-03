from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class LevelNumber(models.Model):
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "level number"
        ordering = ['number']

    def __str__(self):
        return str(self.number) + ": " + self.name


@python_2_unicode_compatible
class Category(models.Model):
    version = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.version + ": " + self.name

    def natural_key(self):
        return (self.version,)


class RequirementManager(models.Manager):
    def get_by_natural_key(self, category, req_nr):
        return self.get(category=category, req_nr=req_nr)


@python_2_unicode_compatible
class Requirement(models.Model):
    objects = RequirementManager()
    req_nr = models.PositiveSmallIntegerField()
    level_nr = models.ManyToManyField(LevelNumber, related_name='level_nr')
    category = models.ForeignKey(Category)
    description = models.TextField()
    report = models.ForeignKey('project.Report', related_name='requirement_report', blank=True, null=True)

    class Meta:
        verbose_name = 'requirement'
        unique_together = (('category', 'req_nr'))

    def __str__(self):
        return ": ".join(map(str, self.natural_key()))

    def level_number(self):
        return ", ".join([str(n.number) for n in self.level_nr.all()])

    def natural_key(self):
        return self.category.natural_key() + (self.req_nr,)
