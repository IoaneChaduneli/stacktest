from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.views import LogoutView as DjangoLogoutView
# Create your views here.

class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('forum:home')