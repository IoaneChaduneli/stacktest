from django import forms
from forum.models import Question

class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class SearchForm(forms.Form):
    q = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
                                        'type': "search",
                                        'class':"form-control me-2",
                                        'placeholder': "search"
    }))

