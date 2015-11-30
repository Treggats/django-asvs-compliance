from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from hvad.models import TranslatableModel, TranslatedFields
from django_markdown.models import MarkdownField
from django.db import models
from asvsrequirement.models import Requirement, Category


@python_2_unicode_compatible
class AnnotationRelation(TranslatableModel):
    # TODO: Find a better way to solve this
    req_annotate_pk = models.PositiveIntegerField()
    url = models.URLField()

    translations = TranslatedFields(
        name=models.CharField(max_length=250)
    )

    @property
    def related_name(self):
        return self.name

    def __str__(self):
        return self.lazy_translation_getter('name', str(self.pk))


@python_2_unicode_compatible
class AnnotationRequirement(TranslatableModel):
    requirement = models.ForeignKey(Requirement)
    category = models.ForeignKey(Category)
    relations = models.ManyToManyField(AnnotationRelation)

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
        unique_together = ('requirement', 'category')
        ordering = ('requirement', 'category')

    def __str__(self):
        return self.lazy_translation_getter('title', str(self.pk))


@python_2_unicode_compatible
class AnnotationExplanationType(TranslatableModel):
    translations = TranslatedFields(
        type=models.CharField(max_length=40)
    )

    @property
    def type_(self):
        return self.type

    def __str__(self):
        return self.type


@python_2_unicode_compatible
class AnnotationExplanation(TranslatableModel):
    req_ann = models.ForeignKey(AnnotationRequirement)
    type = models.ForeignKey(AnnotationExplanationType)

    translations = TranslatedFields(
        explanation=models.TextField()
    )

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.req_ann.title_
