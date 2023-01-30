from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.views import LogoutView as DjangoLogoutView, LoginView as DjangoLoginView
# Create your views here.

class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('forum:home')

class loginView(DjangoLoginView):
    next_page = reverse_lazy('forum:home')
    template_name = 'auth/login.html'
    redirect_authenticated_user = False