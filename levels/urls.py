from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^requirement/(\d+)/$', views.get_requirement, name='get_requirement'),
    url(r'^category/(\d+)/$', views.get_category, name='get_category'),
]
