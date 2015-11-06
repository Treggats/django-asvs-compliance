from django.contrib import admin
from django.contrib.admin import models

from .models import AsvsVersion
from .models import Level, LevelName
from .models import Category, CategoryName
from .models import Requirement, RequirementName


@admin.register(AsvsVersion)
class AsvsVersionAdmin(admin.ModelAdmin):
    ordering = ('version_number',)


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'version')
    ordering = ('number',)


@admin.register(LevelName)
class LevelNameAdmin(admin.ModelAdmin):
    list_display = ('level_number', 'name', 'lang_code')
    ordering = ('level_number',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'version')
    ordering = ('number',)


@admin.register(CategoryName)
class CategoryNameAdmin(admin.ModelAdmin):
    list_display = ('category_number', 'name', 'lang_code')
    ordering = ('category_number',)


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('number', 'category', 'name', 'version')
    list_filter = ('category',)
    ordering = ('number',)


@admin.register(RequirementName)
class RequirementNameAdmin(admin.ModelAdmin):
    list_display = ('requirement_number', 'title', 'lang_code')
    ordering = ('requirement_number',)
