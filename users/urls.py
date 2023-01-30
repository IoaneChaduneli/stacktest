from django.urls import path
from users.views import LogoutView
app_name = 'users'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name= 'auth-logout' )
]
