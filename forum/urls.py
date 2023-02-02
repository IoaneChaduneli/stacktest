from django.urls import path
from forum.views import HomeView, QuestionDetailView, QuestionCreateView, QuestionUpdateView, QuestionDeleteView,AnswerCreateView, AnswerDetailView



app_name = 'forum'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('ask/', QuestionCreateView.as_view(), name='question-add'),
    path('question/<int:pk>/edit/', QuestionUpdateView.as_view(), name = 'question-edit'),
    path('question/<int:pk>/delete/',QuestionDeleteView.as_view(), name='question-delete' ),
    path('question/<int:pk>/question/', AnswerDetailView.as_view(), name='question-detail'),
    path('answer/', AnswerCreateView.as_view(), name='answer-add'),
]
