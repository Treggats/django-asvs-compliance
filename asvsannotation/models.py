from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from hvad.models import TranslatableModel, TranslatedFields
from django.db import models
from asvsrequirement.models import Requirement, Category


@python_2_unicode_compatible
class AnnotationType(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=40)
    )

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class AnnotationHelp(TranslatableModel):
    requirement = models.ForeignKey(Requirement)
    category = models.ForeignKey(Category)
    annotation_type = models.ForeignKey(AnnotationType)

    translations = TranslatedFields(
        help_text=models.TextField()
    )

    class Meta:
        unique_together = ('requirement', 'category')
        verbose_name = 'Annotation help text'
        verbose_name_plural = 'Annotation help texts'

    def __str__(self):
        return self.help_text


@python_2_unicode_compatible
class AnnotationRelation(TranslatableModel):
    requirement = models.ForeignKey(Requirement)
    category = models.ForeignKey(Category)
    url = models.URLField()

    translations = TranslatedFields(
        relation_title=models.CharField(max_length=100)
    )

    @property
    def title_(self):
        return self.relation_title

    class Meta:
        unique_together = ('requirement', 'category')

    def __str__(self):
        return self.title_


@python_2_unicode_compatible
class Annotation(TranslatableModel):
    requirement = models.ForeignKey(Requirement)
    category = models.ForeignKey(Category)
    annotation_help = models.ForeignKey(AnnotationHelp, blank=True, null=True)
    relations = models.ManyToManyField(AnnotationRelation)

    translations = TranslatedFields(
        title=models.CharField(max_length=100)
    )

    @property
    def title_(self):
        return self.title

    class Meta:
        unique_together = ('requirement', 'category')

    def __str__(self):
        return self.title_
