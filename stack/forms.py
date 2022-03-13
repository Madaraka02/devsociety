from dataclasses import fields
from pyexpat import model
from .models import *
from django.forms import ModelForm


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content', 'slug']


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['body']        

class AcceptForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['is_answer_helpful']           