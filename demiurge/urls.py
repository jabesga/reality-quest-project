import django.conf.urls
from demiurge import views

urlpatterns = django.conf.urls.patterns('',
                       django.conf.urls.url(r'^$', views.index, name="index"),
                       )