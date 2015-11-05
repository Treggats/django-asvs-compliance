from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class AsvsVersion(models.Model):
          version_number = models.CharField(max_length=10, default='3')

          def __str__(self):
                    return self.version_number


@python_2_unicode_compatible
class LevelName(models.Model):
          lang_code = models.CharField(max_length=5)
          name = models.CharField(max_length=100)

          def __str__(self):
                    return self.name


@python_2_unicode_compatible
class Level(models.Model):
          number = models.PositiveSmallIntegerField()
          name = models.ForeignKey(LevelName)
          version = models.ForeignKey(AsvsVersion, default='3')

          def __str__(self):
                    return "{0}: {1}".format(self.number, self.name)


@python_2_unicode_compatible
class CategoryName(models.Model):
          lang_code = models.CharField(max_length=5)
          name = models.CharField(max_length=100)

          def __str__(self):
                    return self.name


@python_2_unicode_compatible
class Category(models.Model):
          number = models.PositiveSmallIntegerField()
          name = models.ForeignKey(CategoryName)
          version = models.ForeignKey(AsvsVersion, default='3')

          class Meta:
                    verbose_name_plural = 'Categories'

          def __str__(self):
                    return "{0}: {1}".format(self.number, self.name)


@python_2_unicode_compatible
class RequirementName(models.Model):
          lang_code = models.CharField(max_length=5)
          title = models.TextField()

          def __str__(self):
                    return "{}".format(self.title)


@python_2_unicode_compatible
class Requirement(models.Model):
          number = models.PositiveSmallIntegerField()
          category = models.ForeignKey(Category)
          name = models.ForeignKey(RequirementName)
          version = models.ForeignKey(AsvsVersion, default='3')

          def __str__(self):
                    return "{}".format(self.name)

