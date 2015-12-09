from django.conf.urls import url
from .views import LevelListView, CategoryListView, CategoryDetailView, \
    RequirementListView, HomeView, RequirementDetailView

urlpatterns = [
    url(r'^$', HomeView.as_view(title='Home', content_template='index.html'),
        name='home'),
    url(r'^requirement/$', RequirementListView.as_view(),
        name='requirement_list'),
    url(r'^requirement/(?P<pk>[0-9]+)/$', RequirementDetailView.as_view(),
        name='requirement_detail'),
    url(r'^level/(\d+)/$', LevelListView.as_view(), name='level_list'),
    url(r'^category/$', CategoryListView.as_view(),
        name='category_list'),
    url(r'^category/(?P<category_number>[0-9]+)/$',
        CategoryDetailView.as_view(),
        name='category_list'),
    url(r'^project/$', HomeView.as_view(title='Create Project',
        content_template='create_project.html'), name='create_project')
]

handler404 = 'asvsrequirement.views.NotFoundView'
