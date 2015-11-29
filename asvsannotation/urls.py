from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^explanation/$', views.get_explanation, name='annotation_list'),
    url(r'^explanation/([0-9]+)/$', views.get_explanation,
        name='annotation_explanation'),
]
