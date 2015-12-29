from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from reporting.models import Client, Project, Report


class ClientListView(ListView):
    model = Client
    context_object_name = 'clients'


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'


class ReportListView(ListView):
    model = Report
    context_object_name = 'reports'
