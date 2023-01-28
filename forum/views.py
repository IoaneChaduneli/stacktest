from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from forum.models import Question
from forum.forms import QuestionCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomeView(ListView):
    model = Question
    template_name = 'forum/question_list.html'

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'forum/question_detail.html'

# def create_question_view(request):
    # question = Question(
    #       user_id = request.GET.get('user'),
    #       title = request.GET.get('title'),
    #       text = request.GET.get('text'),
    #       views = request.GET.get('views'),
    # )
  
    # question.save()
    # if request.method == 'GET':
    #     return render(
    #         request, 
    #         'forum/question_add.html', 
    #         {
    #             'form': QuestionCreateForm()
    #         }
    #      )
    # else:
    #     form = QuestionCreateForm(request.POST)
    #     if form.is_valid:
    #         form.save()
    #         return redirect('forum:home')

    #     return render(
    #         request, 
    #         'forum/question_add.html', 
    #         {
    #             'form': form
    #         }
    #      )

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = [

        'title', 
        'text'
    ]

    success_url = reverse_lazy('forum:home')

    def form_valid(self, form):
        self.object: Question = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)


    template_name = 'forum/question_add.html'

class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['title', 'text']
    template_name = 'forum/question_edit.html'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Question.objects.all()
        return Question.objects.filter(user = self.request.user)