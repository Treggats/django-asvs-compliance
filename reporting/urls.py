from django.conf.urls import url
from .views import ClientListView, ClientDetailView, ClientCreateView, \
    ClientUpdateView, ProjectListView, ProjectDetailView, ProjectCreateView, \
    ProjectUpdateView, ProjectTicketDetailView, ProjectTicketUpdateView, \
    ReportListView, ReportDetailView, ReportCreateView, ReportUpdateView

urlpatterns = [
    url(r'clients/$', ClientListView.as_view(), name='client_list'),
    url(r'^clients/(?P<pk>[0-9]+)/$', ClientDetailView.as_view(),
        name='client_detail'),
    url(r'clients/create$', ClientCreateView.as_view(), name='client_create'),
    url(r'^clients/(?P<pk>[0-9]+)/edit/$',
        ClientUpdateView.as_view(), name='client_update'),

    url(r'projects/$', ProjectListView.as_view(), name='project_list'),
    url(r'^projects/(?P<pk>[0-9]+)/$', ProjectDetailView.as_view(),
        name='project_detail'),
    url(r'^projects/ticket/(?P<pk>[0-9]+)/$',
        ProjectTicketDetailView.as_view(), name='project_ticket_detail'),
    url(r'^projects/ticket/(?P<pk>[0-9]+)/edit/$',
        ProjectTicketUpdateView.as_view(), name='project_ticket_update'),
    url(r'projects/create$', ProjectCreateView.as_view(),
        name='project_create'),
    url(r'^projects/(?P<pk>[0-9]+)/edit/$',
        ProjectUpdateView.as_view(), name='project_update'),

    url(r'reports/$', ReportListView.as_view(), name='report_list'),
    url(r'^reports/(?P<pk>[0-9]+)/$', ReportDetailView.as_view(),
        name='report_detail'),
    url(r'reports/create$', ReportCreateView.as_view(), name='report_create'),
    url(r'^reports/(?P<pk>[0-9]+)/edit/$',
        ReportUpdateView.as_view(), name='report_update'),
]
