from django.contrib import admin
from .models import Project, Report
from level.models import Requirement
from django.core.serializers import serialize, deserialize


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'done')


class RequirementInline(admin.TabularInline):
    model = Requirement
    extra = 2


class ReportAdmin(admin.ModelAdmin):
    list_filter = ['project']
    # inlines = [RequirementInline]

    def save_model(self, request, obj, form, change):
        """
        for obj in deserialize('json',
                               obj.requirements,
                               use_natural_foreign_keys=True,
                               use_natural_primary_keys=True):
            print(obj)
        """
        req_obj = Requirement.objects.filter(id__in=[1, 2, 3])
        req_json = serialize('json',
                             req_obj,
                             indent=2,
                             fields=('req_nr', 'category'),
                             use_natural_foreign_keys=True,
                             use_natural_primary_keys=True)
        obj.requirements = req_json
        obj.save()


admin.site.register(Project, ProjectAdmin)
admin.site.register(Report, ReportAdmin)
