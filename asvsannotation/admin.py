from django.contrib import admin
from django.db import models
from django_markdown.widgets import AdminMarkdownWidget
from hvad.admin import TranslatableAdmin

# from .models import AnnotationRelation, AnnotationRequirement
# from .models import AnnotationExplanation, AnnotationExplanationType
from .models import Annotation, AnnotationHelp, AnnotationRelation
from .models import AnnotationType


class AnnotationAdmin(TranslatableAdmin):
    def __init__(self, *args, **kwargs):
        super(AnnotationAdmin, self).__init__(*args, **kwargs)

    filter_horizontal = ('relations',)
    list_filter = ('category', 'relations')
    search_fields = ['translations__title']

admin.site.register(Annotation, AnnotationAdmin)


class AnnotationRelationAdmin(TranslatableAdmin):
    def __init__(self, *args, **kwargs):
        super(AnnotationRelationAdmin, self).__init__(*args, **kwargs)
admin.site.register(AnnotationRelation, AnnotationRelationAdmin)


class AnnotationHelpAdmin(TranslatableAdmin):
    def __init__(self, *args, **kwargs):
        super(AnnotationHelpAdmin, self).__init__(*args, **kwargs)
    # list_display = ('id', 'req_ann', 'type')
    formfield_overrides = {models.TextField: {'widget': AdminMarkdownWidget}}
admin.site.register(AnnotationHelp, AnnotationHelpAdmin)


class AnnotationTypeAdmin(TranslatableAdmin):
    def __init__(self, *args, **kwargs):
        super(AnnotationTypeAdmin, self).__init__(*args, **kwargs)
admin.site.register(AnnotationType, AnnotationTypeAdmin)
