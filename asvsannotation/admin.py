from django.contrib import admin
from hvad.admin import TranslatableAdmin
from django_markdown.admin import MarkdownModelAdmin

from .models import RelatedAnnotated, RequirementAnnotated
from .models import AnnotationExplanation


class RelatedAnnotatedAdmin(TranslatableAdmin):
    def __init__(self, *args, **kwargs):
        super(RelatedAnnotatedAdmin, self).__init__(*args, **kwargs)
admin.site.register(RelatedAnnotated, RelatedAnnotatedAdmin)


class RequirementAnnotatedAdmin(TranslatableAdmin):
    def __init__(self, *args, **kwargs):
        super(RequirementAnnotatedAdmin, self).__init__(*args, **kwargs)

    filter_horizontal = ('relations',)
    list_display = ('requirement_number', 'category',
                    'title_', 'related_')
    list_filter = ('category', 'relations')
    search_fields = ['translations__title']
admin.site.register(RequirementAnnotated, RequirementAnnotatedAdmin)

admin.site.register(AnnotationExplanation, MarkdownModelAdmin)
