from django.conf.urls import url
from .views import ClientListView, ProjectListView, ReportListView, \
    ProjectCreate

urlpatterns = [
    url(r'clients/$', ClientListView.as_view(), name='client_list'),
    url(r'projects/$', ProjectListView.as_view(), name='project_list'),
    url(r'projects/create$', ProjectCreate.as_view(), name='project_create'),
    url(r'reports/$', ReportListView.as_view(), name='report_list'),
]
