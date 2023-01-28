from django import forms
from forum.models import Question

class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

