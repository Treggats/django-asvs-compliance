from django.contrib import admin
from .models import LevelNumber, Category, Requirement


class RequirementAdmin(admin.ModelAdmin):
    list_display = ('req_nr', 'level_number', 'category', 'description')
    list_filter = ['level_nr', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('version', 'name')

admin.site.register(LevelNumber)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Requirement, RequirementAdmin)
