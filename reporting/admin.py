from django.contrib import admin
from .models import Ticket, Project, Report, Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city')
admin.site.register(Client, ClientAdmin)


class TicketAdmin(admin.ModelAdmin):
    list_display = ('project', 'name', 'passed_all_requirements')
    filter_horizontal = ('requirements',)
admin.site.register(Ticket, TicketAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'level')
admin.site.register(Project, ProjectAdmin)


class ReportAdmin(admin.ModelAdmin):
    list_display = ('release_name', 'release_date', 'project')
admin.site.register(Report, ReportAdmin)
