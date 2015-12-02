from django.conf.urls import url
from .views import LevelListView, CategoryListView, CategoryDetailView, \
    RequirementListView, HomeView, RequirementDetailView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^requirement/$', RequirementListView.as_view()),
    url(r'^requirement/(?P<pk>[0-9]+)/$', RequirementDetailView.as_view(),
        name='requirement_detail'),
    url(r'^level/(\d+)/$', LevelListView.as_view()),
    url(r'^category/$', CategoryListView.as_view()),
    url(r'^category/(?P<category_number>[0-9]+)/$',
        CategoryDetailView.as_view(),
        name='get_category'),
]

handler404 = 'asvsrequirement.views.NotFoundView'
