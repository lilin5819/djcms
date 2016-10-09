# -*- coding:utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from focus import urls as focus_urls
from focus import views

urlpatterns = [
    url(r'^focus/', include(focus_urls)),
    url(r'^$', views.index, name='index'),
    url(r'^json/arm/', views.json_arm, name='json_arm'), #json解析测试
    url(r'^update/', views.update,name='update'), #Ajxa动态刷新测试
    url(r'^admin/', include(admin.site.urls)),
]
