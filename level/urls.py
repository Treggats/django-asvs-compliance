from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^requirement/$', views.get_requirement, name='requirement_list'),
    url(r'^requirement/(\d+)/$', views.get_requirement,
        name='requirement_detail'),
    url(r'^level/(\d+)/$', views.get_level, name='get_level'),
    url(r'^category/$', views.get_category, name='get_category_list'),
    url(r'^category/([0-9]+)/$', views.get_category, name='get_category'),
    url(r'^explanation/$', views.get_explanation, name='annotation_list'),
    url(r'^explanation/([0-9]+)/$', views.get_explanation,
        name='annotation_explanation'),
]
