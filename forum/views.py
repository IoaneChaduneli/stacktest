from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from forum.models import Question, Answer
from forum.forms import QuestionCreateForm, SearchForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from forum.forms import AnswerForm

# Create your views here.

class HomeView(ListView):
    model = Question
    template_name = 'forum/question_list.html'
    paginate_by = 6
    



    def get_queryset(self):
        input_text = self.request.GET.get('q', '') 
        if input_text.startswith('@'):
            # if input_text.startswith('user:'):
            #     parts = input_text.split(':')
            return Question.objects.filter(user__username__icontains=input_text[1])
        elif input_text.startswith('[') and input_text.endswith(']'):
            return Question.objects.filter(tag__name__icontains=input_text[1:-1])

        return Question.objects.filter(title__icontains=input_text)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'forum/question_detail.html'

    def get(self, request, *args, **kwargs):
        self.object: Question = self.get_object()
        self.object.views += 1
        self.object.save()
        context = self.get_context_data(object = self.object)
        return self.render_to_response(context)

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
    
    form_class = QuestionCreateForm
    
    success_url = reverse_lazy('forum:home')

    def form_valid(self, form):
        self.object: Question = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)



    template_name = 'forum/question_add.html'

class StaffRequiredMixin:
     def get_queryset(self):
        if self.request.user.is_staff:
            return Question.objects.all()
        return Question.objects.filter(user = self.request.user)


class QuestionUpdateView(StaffRequiredMixin,LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['title', 'text']
    template_name = 'forum/question_edit.html'


class QuestionDeleteView(StaffRequiredMixin,LoginRequiredMixin, DeleteView):
    model = Question
    template_name = 'forum/question_confirm_delete.html'
    fields = ['title', 'text', 'tags']
    success_url = reverse_lazy('forum:home')
    # def get_queryset(self):
    #     if self.request.user.is_staff:
    #         return Question.objects.all()
    #     return Question.objects.filter(user = self.request.user)

    

class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ['text']
    template_name = 'forum/answer_add.html'

    
# we use this form if we want not to use all the fields of database(models), e make the validation

    def form_valid(self, form):
        self.object: Answer = form.save(commit=False)
        self.object.user = self.request.user
        question = get_object_or_404(Question,pk=self.request.GET.get('question')) 
        self.object.question = question
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('forum:question-detail', kwargs = {'pk':self.object.question.pk}) # how to make dynamic reverse lazy
    
    
  

    