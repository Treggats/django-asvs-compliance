from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Version(models.Model):
    version = models.CharField(max_length=5, verbose_name='ASVS version')

    class Meta:
        verbose_name = 'ASVS version'

    def __str__(self):
        return self.version


@python_2_unicode_compatible
class LevelNumber(models.Model):
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "level number"
        ordering = ['number']

    def __str__(self):
        return str(self.number) + ": " + self.name


class CategoryManager(models.Manager):
    def get_by_natural_key(self, version, name):
        return self.get(version, name)


@python_2_unicode_compatible
class Category(models.Model):
    objects = CategoryManager()
    version = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    def natural_key(self):
        return (self.version, self.name)

    class Meta:
        verbose_name_plural = 'categories'
        unique_together = (('version', 'name'))

    def __str__(self):
        return self.version + ": " + self.name


class RequirementManager(models.Manager):
    def get_by_natural_key(self, category, req_nr):
        return self.get(category=category, req_nr=req_nr)


@python_2_unicode_compatible
class Requirement(models.Model):
    objects = RequirementManager()
    req_nr = models.PositiveSmallIntegerField(verbose_name='Requirement number')
    level_nr = models.ManyToManyField(LevelNumber,
                                      related_name='level_nr',
                                      verbose_name='Level number')
    category = models.ForeignKey(Category, related_name='requirement_category')
    description = models.TextField()
    report = models.ForeignKey('project.Report',
                               related_name='requirement_report',
                               blank=True, null=True)
    version = models.ForeignKey(Version, verbose_name='ASVS version')

    def level_number(self):
        return ", ".join([str(n.number) for n in self.level_nr.all()])

    class Meta:
        verbose_name = 'requirement'
        unique_together = (('category', 'req_nr'))

    def __str__(self):
        return str(self.category.version) + '.' + str(self.req_nr)


@python_2_unicode_compatible
class AnnotationTitle(models.Model):
    lang_code = models.CharField(max_length=10, verbose_name='Language code')
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Annotation title'

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class AnnotationRelated(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Annotation related'
        verbose_name_plural = 'Annotation related'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Annotation(models.Model):
    title = models.ForeignKey(AnnotationTitle)
    category = models.ForeignKey(Category)
    requirement = models.ManyToManyField(Requirement)
    related = models.ForeignKey(AnnotationRelated, blank=True, null=True)

    class Meta:
        verbose_name = 'Annotation'
