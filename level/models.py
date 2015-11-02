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


@python_2_unicode_compatible
class Requirement(models.Model):
    number = models.ManyToManyField(LevelNumber, related_name='level_nr')
    category = models.ForeignKey(Category)
    description = models.TextField()

    class Meta:
        verbose_name = 'requirement'

    def __str__(self):
        return self.description

    def level_number(self):
        return ", ".join([str(n.number) for n in self.number.all()])

    def level_verbose(self):
        return [n for n in self.number.all()]
