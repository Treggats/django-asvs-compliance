from django.contrib import admin
from django_markdown.models import MarkdownField
from django_markdown.widgets import AdminMarkdownWidget
from hvad.admin import TranslatableAdmin
from django_markdown.admin import MarkdownModelAdmin

from .models import AnnotationRelation, AnnotationRequirement
from .models import AnnotationExplanation, AnnotationExplanationType


class RelatedAnnotatedAdmin(TranslatableAdmin):
    def __init__(self, *args, **kwargs):
        super(RelatedAnnotatedAdmin, self).__init__(*args, **kwargs)
admin.site.register(AnnotationRelation, RelatedAnnotatedAdmin)


class RequirementAnnotatedAdmin(TranslatableAdmin):
    def __init__(self, *args, **kwargs):
        super(RequirementAnnotatedAdmin, self).__init__(*args, **kwargs)

    filter_horizontal = ('relations',)
    list_display = ('requirement_number', 'category',
                    'title_', 'related_')
    list_filter = ('category', 'relations')
    search_fields = ['translations__title']
admin.site.register(AnnotationRequirement, RequirementAnnotatedAdmin)


class AnnotationExplanationAdmin(admin.ModelAdmin):
    list_display = ('id', 'req_ann', 'type')
    formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}
admin.site.register(AnnotationExplanation, AnnotationExplanationAdmin)

admin.site.register(AnnotationExplanationType)
