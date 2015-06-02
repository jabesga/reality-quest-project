from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       url(r'npc/$', views.npc, name="npc"),
                       url(r'npc/create/$', views.create_npc_with_form, name="create_npc_with_form"),
                       url(r'npc/(?P<_id>\d+)/$', views.find_npc_by_id, name='find_npc_by_id'),
                       url(r'npc/(?P<_id>\d+)/missions/$', views.find_missions_of_npc, name='find_missions_of_npc'),
                       url(r'mission/$', views.mission, name="mission"),
                       url(r'mission/create/$', views.create_mission_with_form, name='create_mission_with_form'),
                       #url(r'mission/(?P<id>[0-9])/$', views.mission, name="mission"),
                       )
