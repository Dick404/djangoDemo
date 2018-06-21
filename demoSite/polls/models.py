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

    @__str__
    def __str__(self):
        if not type(self) is None:
            print [{"question is": self.question_text, "publish date is": self.pub_date}]

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    @__str__
    def __str__(self):
        print [{"choice text is": self.choice_text, "the vote is": self.votes}]
