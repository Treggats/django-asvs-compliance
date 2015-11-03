from django.contrib import admin
from .models import Project, Report

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'done')


class ReportAdmin(admin.ModelAdmin):
    list_filter = ['project']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Report, ReportAdmin)
