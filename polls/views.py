'''
Author: your name
Date: 2020-11-20 16:12:20
LastEditTime: 2020-11-20 16:27:03
LastEditors: your name
Description: In User Settings Edit
FilePath: \Pull_Site\polls\views.py
'''
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('欢迎参与投票！')