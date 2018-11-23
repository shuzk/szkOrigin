
from django.conf.urls import url, include
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),
    url(r'^weather2/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather2),
    url(r'^qs/', views.qs),
    url(r'^get_body/', views.get_body),
    url(r'^json/', views.get_body_json),
    url(r'^headers/', views.get_headers),

    url(r'^response/', views.demo_view),
    url(r'^responsejson/', views.demo_view2),

    url(r'^$', views.index, name='index'),
]
