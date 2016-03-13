from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from reporting.models import Client, Project, Report, Ticket


class ClientListView(ListView):
    model = Client
    context_object_name = 'clients'


class ClientDetailView(DetailView):
    model = Client
    context_object_name = 'client'


class ClientCreateView(CreateView):
    model = Client
    template_name = "edit/client/client_create_form.html"
    fields = ["name", "address", "postal_code", "city"]
    success_url = "/reporting/clients"


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['tickets'] = Ticket.objects.filter(project=context['object'])
        return context


class ProjectCreateView(CreateView):
    model = Project
    template_name = "edit/project/project_create_form.html"
    fields = ["name", "description", "client", "level"]
    success_url = "/reporting/projects"


class ProjectTicketDetailView(DetailView):
    model = Ticket
    context_object_name = 'ticket'

    def get_context_data(self, **kwargs):
        context = super(ProjectTicketDetailView, self). \
            get_context_data(**kwargs)
        context['requirements'] = context['object'].requirements.all()
        return context


class ReportListView(ListView):
    model = Report
    context_object_name = 'reports'


class ReportDetailView(DetailView):
    model = Report
    context_object_name = 'report'


class ReportCreateView(CreateView):
    model = Report
    template_name = "edit/report/report_create_form.html"
    fields = ["release_name", "release_date", "comments", "project"]
    success_url = "/reporting/reports"
