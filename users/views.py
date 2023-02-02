from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LogoutView as DjangoLogoutView, LoginView as DjangoLoginView
from users.models import User
from users.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import Profile
# Create your views here.

class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('forum:home')

class loginView(DjangoLoginView):
    next_page = reverse_lazy('forum:home')
    template_name = 'auth/login.html'
    redirect_authenticated_user = False

class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'auth/login.html'
    success_url = reverse_lazy('forum:home')

#user profile template

class ProfileView(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = 'auth/profile.html'
    fields = ('icon',)
    success_url = reverse_lazy('users:auth-profile')

    def form_valid(self, form):
        self.object: Profile = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)



