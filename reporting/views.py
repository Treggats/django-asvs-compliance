from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from reporting.models import Client, Project, Report


class ClientListView(ListView):
    model = Client
    context_object_name = 'clients'


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'


class ProjectCreate(CreateView):
    """docstring for ProjectCreate"""
    model = Project
    template_name = "project_create_form.html"
    fields = ["name", "description", "client", "level"]
    success_url = "/reporting/projects"


class ReportListView(ListView):
    model = Report
    context_object_name = 'reports'
