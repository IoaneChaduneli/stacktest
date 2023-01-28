from django.urls import path
from forum.views import HomeView, QuestionDetailView, QuestionCreateView, QuestionUpdateView



app_name = 'forum'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('ask/', QuestionCreateView.as_view(), name='question-add'),
    path('question/<int:pk>/edit/', QuestionUpdateView.as_view(), name = 'question-edit')
]
