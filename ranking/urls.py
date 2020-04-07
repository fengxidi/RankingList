# _*_ coding: utf-8 _*_
__auther__ = 'guozheng'
__date__ = '2020-4-7 21:05'

from django.urls import path,re_path
from ranking import views

app_name = 'ranking'
urlpatterns = [
    re_path(r'^rank/(?P<account>\w+)/',views.RankView.as_view(),name='rank'),
]