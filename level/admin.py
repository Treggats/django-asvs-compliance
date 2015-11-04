from django.contrib import admin
from .models import LevelNumber, Category, Requirement, Version


class RequirementAdmin(admin.ModelAdmin):
    list_display = ('req_nr_view', 'level_number', 'category', 'description')
    list_filter = ['level_nr', 'category']
    readonly_fields = ('description',)
    filter_horizontal = ['level_nr']

    fieldsets = (
                 (
                        'ASVS version', {
                        'fields': ('version',),
                        'classes': ('collapse',)},
                 ),
                 (
                  None, {
                    'fields': ('req_nr', 'level_nr', 'category', 'description'),
                    'classes': ('wide', 'extrapretty'),
                  },
                  )
                )

    def req_nr_view(self, obj):
        return ("%s" % obj)
    req_nr_view.short_description = 'Requirement number'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('version', 'name')

admin.site.register(Version)
admin.site.register(LevelNumber)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Requirement, RequirementAdmin)
