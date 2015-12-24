from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from hvad.models import TranslatableModel, TranslatedFields
from django.db import models
from asvsrequirement.models import Requirement


@python_2_unicode_compatible
class AnnotationType(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=40)
    )

    @property
    def type_title(self):
        return self.title


@python_2_unicode_compatible
class AnnotationHelp(TranslatableModel):
    annotation_type = models.ForeignKey(AnnotationType)
    requirement = models.ForeignKey(Requirement)

    translations = TranslatedFields(
        help_text=models.TextField()
    )

    @property
    def help_text_(self):
        return self.help_text

    class Meta:
        verbose_name = 'Annotation help text'
        verbose_name_plural = 'Annotation help texts'

    def __str__(self):
        excerpt = self.help_text.split()[:10]
        return " ".join(excerpt)


@python_2_unicode_compatible
class AnnotationRelation(TranslatableModel):
    url = models.URLField()

    translations = TranslatedFields(
        relation_title=models.CharField(max_length=100)
    )

    @property
    def relation_title_(self):
        return self.relation_title

    class Meta:
        pass

    def __str__(self):
        return self.relation_title


@python_2_unicode_compatible
class Annotation(TranslatableModel):
    requirement = models.ForeignKey(Requirement)
    annotation_help = models.ManyToManyField(AnnotationHelp, blank=True)
    relations = models.ManyToManyField(AnnotationRelation, blank=True)

    translations = TranslatedFields(
        title=models.CharField(max_length=100)
    )

    @property
    def annotation_title(self):
        return self.title

    class Meta:
        pass

    def __str__(self):
        return self.title
