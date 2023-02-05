from django import forms
from forum.models import Question, Answer
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.forms import ModelMultipleChoiceField

class QuestionCreateForm(forms.ModelForm):
        
    class Meta:
        model = Question
        fields = ['title', 'text', 'tags']



class SearchForm(forms.Form):
    q = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
                                        'type': "search",
                                        'class':"form-control me-2",
                                        'placeholder': "search"
    }))


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']

        
    