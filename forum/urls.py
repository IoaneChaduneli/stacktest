from django.urls import path
from forum.views import HomeView, QuestionDetailView, QuestionCreateView, QuestionUpdateView, QuestionDeleteView, question_detail



app_name = 'forum'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('ask/', QuestionCreateView.as_view(), name='question-add'),
    path('question/<int:pk>/edit/', QuestionUpdateView.as_view(), name = 'question-edit'),
    path('question/<int:pk>/delete/',QuestionDeleteView.as_view(), name='question-delete' ),
    # path('answer/', AnswerCreateView.as_view(), name='answer-add'),
    path('<int:pk>/', question_detail, name='question-detail')
]
