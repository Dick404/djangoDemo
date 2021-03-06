# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


def __str__(fn):
    def wrapper(*args):
        if type(args[0]) is None:
            return __str__(args[0])
        else:
            return fn(args[0])
    return wrapper


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

#    @__str__
#    def __str__(self):
#        if not type(self) is None:
#            print [{"question is": self.question_text, "publish date is": self.pub_date}]
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

 #   @__str__
 #   def __str__(self):
 #       print [{"choice text is": self.choice_text, "the vote is": self.votes}]

    def __str__(self):
        return self.choice_text


'''
class serialbindhost(models.Model):

    class Meta:
        db_table = 'serialbindhost'

    serialnum = models.CharField(max_length=100, primary_key='serialNum')
    host = models.CharField(max_length=100)

    def get_serial_num_bind_host(self):
        return [self.serialNum, self.host]
'''
