from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^requirement/(\d+)/$', views.get_requirement,
        name='get_requirement'),
    url(r'^level/(\d+)/$', views.get_level, name='get_level'),
    url(r'^category/$', views.get_category, name='get_category_list'),
    url(r'^category/(V[0-9]+)/$', views.get_category, name='get_category'),
]
