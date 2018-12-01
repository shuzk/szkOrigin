from django.conf.urls import url, include
from django.contrib import admin
from . import views
from rest_framework.routers import DefaultRouter

from . import views
urlpatterns = [
    url(r'^student/', views.StudentView.as_view()),
    url(r'^index/', views.index),
    url(r'^index2/', views.index2),
    # url(r'^studentsViewSet/', views.StudentsInfoViewSet.as_view(), name='studentsa'),
    url(r'^studentS/$', views.StudentsListView.as_view())
    url(r'^studentS2/(?P<pk>\d+)/$', views.StudentsDetailView.as_view())
]

router = DefaultRouter()  # 可以处理视图的路由器
# 不能加^和/
router.register(r'studentsViewSet', views.StudentsInfoViewSet)  # 向路由器中注册视图集
urlpatterns += router.urls  # 将路由器中的所有路由信息追到django的路由列表中
