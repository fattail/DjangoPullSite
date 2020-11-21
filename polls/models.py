'''
Author: ray
Date: 2020-11-20 16:12:20
LastEditTime: 2020-11-20 17:07:43
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Pull_Site\polls\models.py
'''
from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('发布日期')

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)