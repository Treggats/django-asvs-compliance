from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from asvsrequirement.apiviews import RequirementViewSet

router = routers.DefaultRouter()
router.register(r'requirements', RequirementViewSet)

admin.site.site_header = 'ASVS Compliance'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('asvsrequirement.urls')),
    url(r'', include('asvsannotation.urls')),
    url(r'reporting/', include('reporting.urls')),
    url('^markdown/', include('django_markdown.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))
]
