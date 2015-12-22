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
    annotation_type = models.ForeignKey(AnnotationType)

    translations = TranslatedFields(
        help_text=models.TextField()
    )

    @property
    def help_text(self):
        return self.help_text

    class Meta:
        # unique_together = ('requirement', 'category')
        verbose_name = 'Annotation help text'
        verbose_name_plural = 'Annotation help texts'

    def __str__(self):
        return "{}: {}".format(self.annotation_type, self.help_text)


@python_2_unicode_compatible
class AnnotationRelation(TranslatableModel):
    requirement = models.ForeignKey(Requirement)
    category = models.ForeignKey(Category)
    url = models.URLField()

    translations = TranslatedFields(
        relation_title=models.CharField(max_length=100)
    )

    @property
    def relation_title(self):
        return self.relation_title

    class Meta:
        # unique_together = ('requirement', 'category')
        pass

    def __str__(self):
        return self.relation_title


@python_2_unicode_compatible
class Annotation(TranslatableModel):
    requirement = models.ForeignKey(Requirement)
    category = models.ForeignKey(Category)
    annotation_help = models.ManyToManyField(AnnotationHelp, blank=True)
    relations = models.ManyToManyField(AnnotationRelation, blank=True)

    translations = TranslatedFields(
        title=models.CharField(max_length=100)
    )

    @property
    def annotation_title(self):
        return self.title

    class Meta:
        # unique_together = ('requirement', 'category')
        pass

    def __str__(self):
        return self.annotation_title
