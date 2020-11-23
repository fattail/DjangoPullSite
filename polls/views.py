'''
Author: Ray
Date: 2020-11-20 16:12:20
LastEditTime: 2020-11-20 16:27:03
LastEditors: Ray
Description: In User Settings Edit
FilePath: \Pull_Site\polls\views.py
'''
from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse,Http404
from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    response = '您正在阅览第%s道问题的选项'
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse('您正在参与第%s道问题的投票' % question_id)