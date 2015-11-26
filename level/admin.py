from django.contrib import admin
from hvad.admin import TranslatableAdmin

from .models import AsvsVersion
from .models import Level
from .models import Category
from .models import Requirement
from.models import RelatedAnnotated, RequirementAnnotated


@admin.register(AsvsVersion)
class AsvsVersionAdmin(admin.ModelAdmin):
    ordering = ('version_number',)


class LevelAdmin(TranslatableAdmin):
    def __init__(self, *args, **kwargs):
        super(LevelAdmin, self).__init__(*args, **kwargs)

    list_display = ('level_number', 'level_name', 'version')
    list_filter = ('version',)
    ordering = ('level_number',)
admin.site.register(Level, LevelAdmin)


class CategoryAdmin(TranslatableAdmin):
    def __init__(self, *args, **kwargs):
        super(CategoryAdmin, self).__init__(*args, **kwargs)

    list_display = ('category_number', 'category_name', 'version')
    list_filter = ('version',)
    ordering = ('category_number',)
admin.site.register(Category, CategoryAdmin)


class RequirementAdmin(TranslatableAdmin):
    def __init__(self, *args, **kwargs):
        super(RequirementAdmin, self).__init__(*args, **kwargs)

    list_display = ('requirement_number', 'category_version', 'level_number',
                    'requirement_title')
    list_filter = ('levels', 'category__version', 'category')
    search_fields = ['translations__title']
admin.site.register(Requirement, RequirementAdmin)


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
