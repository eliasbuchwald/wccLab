# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 15:38
# @Author  : BOSSBLOCK
# @Email   : sa515038@mail.ustc.edu.cn
# @File    : urls.py
# @Software: PyCharm



from . import views
from django.urls import path,re_path

urlpatterns = [
    path('', views.index, name='index'),
    re_path('^login/$',views.login,name='login'),

    re_path("^(\d+)/(\d+)$",views.detail),  # django2.0x新特性，path不支持正则，必须使用re_path
    path('book/', views.books),
    re_path('^dept/(\d+)$', views.wecarInfo),
    path('dept/', views.depts)

]
