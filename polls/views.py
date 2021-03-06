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
from django.urls import reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question,Choice
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        # redisplay the quesiton voting form
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"您没有进行任何选择",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))