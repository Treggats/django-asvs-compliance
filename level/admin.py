from django.contrib import admin
from .models import AsvsVersion
from .models import Level, LevelName
from .models import Category, CategoryName
from .models import Requirement, RequirementName


@admin.register(AsvsVersion)
class AsvsVersionAdmin(admin.ModelAdmin):
    pass


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    pass


@admin.register(LevelName)
class LevelNameAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(CategoryName)
class CategoryNameAdmin(admin.ModelAdmin):
    list_display = ('category_number', 'lang_code', 'name')


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    pass


@admin.register(RequirementName)
class RequirementNameAdmin(admin.ModelAdmin):
    pass
