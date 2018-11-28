from django.conf.urls import url, include
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^student/', views.StudentView.as_view()),
    url(r'^index/', views.index),
    url(r'^index2/', views.index2),
]
