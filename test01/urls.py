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
    url(r'^redirect/', views.demo_view3),

    url(r'^cookie_set/', views.cookie_set),
    url(r'^cookie_read/', views.cookie_read),

    url(r'^register/', views.register),
    url(r'^RegisterView/', views.RegisterView.as_view()),

    url(r'^demoView/$', views.my_decorator(views.DemoView.as_view())),

    url(r'^demoView2/$', views.DemoView2.as_view()),
    url(r'^demoView3/$', views.DemoView3.as_view()),

    url(r'^middleware/$', views.demo_view_middleware),  # 中间件

    url(r'^$', views.index, name='index'),
]
