from django.conf.urls import url
from .views import ClientListView, ProjectListView, ReportListView

urlpatterns = [
    url(r'clients/$', ClientListView.as_view(), name='client_list'),
    url(r'projects/$', ProjectListView.as_view(), name='project_list'),
    url(r'reports/$', ReportListView.as_view(), name='report_list'),
]
