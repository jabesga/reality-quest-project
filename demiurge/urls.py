import django.conf.urls
from demiurge import views

urlpatterns =  [
                       django.conf.urls.url(r'^$', views.index, name="index"),
                       ]
