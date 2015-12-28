from django.contrib import admin
from .models import Project, Report, Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city')
admin.site.register(Client, ClientAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'level')
    filter_horizontal = ('requirements',)
admin.site.register(Project, ProjectAdmin)


class ReportAdmin(admin.ModelAdmin):
    list_display = ('release_name', 'release_date', 'project')
admin.site.register(Report, ReportAdmin)
