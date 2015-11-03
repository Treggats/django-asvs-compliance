from django.contrib import admin
from .models import Project, Report
from level.models import Requirement


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'done')


class RequirementInline(admin.TabularInline):
    model = Requirement
    extra = 2


class ReportAdmin(admin.ModelAdmin):
    list_filter = ['project']
    # inlines = [RequirementInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Report, ReportAdmin)
