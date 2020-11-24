'''
Author: your name
Date: 2020-11-23 08:45:20
LastEditTime: 2020-11-23 13:49:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Pull_Site\polls\urls.py
'''
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>'),
]
