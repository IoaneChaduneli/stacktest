from django.urls import path
from users.views import LogoutView, loginView
app_name = 'users'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name= 'auth-logout' ),
    path('login/', loginView.as_view(), name='auth-login')
]
