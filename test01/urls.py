
from django.conf.urls import url, include
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),
    url(r'^weather2/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather2),
    url(r'^qs/', views.qs),
    url(r'^get_body/', views.get_body),


    url(r'^$', views.index, name='index'),
]
