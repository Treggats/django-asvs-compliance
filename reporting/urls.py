from django.conf.urls import url
from .views import ClientListView, ProjectListView, ReportListView

urlpatterns = [
    url(r'clients/$', ClientListView.as_view()),
    url(r'projects/$', ProjectListView.as_view()),
    url(r'reports/$', ReportListView.as_view())
]
