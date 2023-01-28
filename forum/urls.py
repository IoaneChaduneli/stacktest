from django.urls import path
from forum.views import HomeView
app_name = 'forum'

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
