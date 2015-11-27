from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from hvad.models import TranslatableModel, TranslatedFields
from django_markdown.models import MarkdownField


@python_2_unicode_compatible
class AsvsVersion(models.Model):
    version_number = models.CharField(max_length=10)

    def __str__(self):
        return self.version_number


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
    def level_number(self):
        return ", ".join([str(l.level_number) for l in self.levels.all()])

    class Meta:
        ordering = ('requirement_number', 'category')

    def __str__(self):
        return "{}: {}".format(self.requirement_number,
                               self.lazy_translation_getter('title',
                                                            str(self.pk)))


@python_2_unicode_compatible
class RelatedAnnotated(TranslatableModel):
    # TODO: Find a better way to solve this
    req_annotate_pk = models.PositiveIntegerField()
    url = models.URLField()

    translations = TranslatedFields(
        name=models.CharField(max_length=250)
    )

    @property
    def related_name(self):
        return self.name

    class Meta:
        verbose_name = _('Related annotated')
        verbose_name_plural = _('Related annotations')

    def __str__(self):
        return self.lazy_translation_getter('name', str(self.pk))


@python_2_unicode_compatible
class RequirementAnnotated(TranslatableModel):
    requirement = models.ForeignKey(Requirement)
    category = models.ForeignKey(Category)
    relations = models.ManyToManyField(RelatedAnnotated)

    translations = TranslatedFields(
        title=models.CharField(max_length=100)
    )

    @property
    def title_(self):
        return self.title

    @property
    def requirement_number(self):
        return self.requirement.requirement_number

    @property
    def category_number(self):
        return self.category.category_number

    @property
    def related_(self):
        return ", ".join([str(r.name) for r in self.relations.all()])

    class Meta:
        verbose_name = _('Requirement annotated')
        verbose_name_plural = _('Requirement annotations')
        unique_together = ('requirement', 'category')
        ordering = ('requirement', 'category')

    def __str__(self):
        return self.lazy_translation_getter('title', str(self.pk))

@python_2_unicode_compatible
class AnnotationExplanation(models.Model):
    req_ann = models.ForeignKey(RequirementAnnotated)
    explanation = MarkdownField()

    def __str__(self):
        return self.req_ann.title

