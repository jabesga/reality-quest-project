from django.conf.urls import include, url
from django.contrib import admin
# from authsys import urls
from demiurge import urls
from api import urls

urlpatterns = [
               url(r'^demiurge/', include('demiurge.urls')),
               url(r'^api/', include('api.urls')),
               url(r'^admin/', include(admin.site.urls)),
               ]
