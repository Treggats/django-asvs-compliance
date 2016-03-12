from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from reporting.models import Client, Project, Report


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


class ProjectCreate(CreateView):
    """docstring for ProjectCreate"""
    model = Project
    template_name = "edit/project/project_create_form.html"
    fields = ["name", "description", "client", "level"]
    success_url = "/reporting/projects"


class ReportListView(ListView):
    model = Report
    context_object_name = 'reports'


class ReportDetailView(DetailView):
    model = Report
    context_object_name = 'projects'
