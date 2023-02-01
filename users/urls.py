from django.urls import path
from users.views import LogoutView, loginView, RegisterView,ProfileView
app_name = 'users'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name= 'auth-logout' ),
    path('login/', loginView.as_view(), name='auth-login'),
    path('signup/', RegisterView.as_view(), name='auth-signup'),
    path('profile/', ProfileView.as_view(), name='auth-profile')
]
