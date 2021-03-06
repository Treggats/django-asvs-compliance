from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from hvad.models import TranslatableModel, TranslatedFields


@python_2_unicode_compatible
class AsvsVersion(models.Model):
    version_number = models.PositiveIntegerField()
    release_date = models.DateField()

    def __str__(self):
        return str(self.version_number)


@python_2_unicode_compatible
class Level(TranslatableModel):
    level_number = models.PositiveIntegerField()
    version = models.ForeignKey(AsvsVersion)

    translations = TranslatedFields(
        name=models.CharField(max_length=100)
    )

    @property
    def level_name(self):
        return self.name

    def __str__(self):
        return "{}: {}".format(self.level_number,
                               self.lazy_translation_getter('name',
                                                            str(self.pk)))


@python_2_unicode_compatible
class Category(TranslatableModel):
    category_number = models.PositiveIntegerField()
    version = models.ForeignKey(AsvsVersion)

    translations = TranslatedFields(
        name=models.CharField(max_length=100)
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('category_number',)

    @property
    def category_name(self):
        return self.name

    def __str__(self):
        return "V{}: {}".format(self.category_number,
                                self.lazy_translation_getter('name',
                                                             str(self.pk)))


@python_2_unicode_compatible
class Requirement(TranslatableModel):
    requirement_number = models.PositiveIntegerField()
    category = models.ForeignKey(Category)
    levels = models.ManyToManyField(Level)

    translations = TranslatedFields(
        title=models.TextField()
    )

    @property
    def requirement_title(self):
        return self.title

    @property
    def category_version(self):
        return self.category.category_number

    @property
    def category_title(self):
        return self.category.category_name

    @property
    def level_number(self):
        return ", ".join([str(l.level_number) for l in self.levels.all()])

    class Meta:
        ordering = ('requirement_number', 'category')

    def __str__(self):
        return "{}:{} {}".format(self.category_version, self.requirement_number, self.requirement_title)
