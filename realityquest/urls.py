from django.conf.urls import patterns, include, url
from django.contrib import admin
from authsys import urls
from demiurge import urls

urlpatterns = patterns('',
                       url(r'^demiurge/', include('demiurge.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
