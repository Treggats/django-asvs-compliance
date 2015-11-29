from django.contrib import admin
from .models import Project, Report


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'asvsrequirement', 'done')


class ReportAdmin(admin.ModelAdmin):
    list_display = ('project', 'project')
    list_filter = ['project']
    filter_horizontal = ['requirements']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Report, ReportAdmin)
