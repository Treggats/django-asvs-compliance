from django.conf.urls import url
from .views import LevelList
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^requirement/$', views.get_requirement, name='requirement_list'),
    url(r'^requirement/(\d+)/$', views.get_requirement,
        name='requirement_detail'),
    url(r'^level/(\d+)/$', LevelList.as_view()),
    url(r'^category/$', views.get_category, name='get_category_list'),
    url(r'^category/([0-9]+)/$', views.get_category, name='get_category'),
]
