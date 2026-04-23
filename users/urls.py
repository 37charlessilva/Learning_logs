"""'Definir padrões de URL para users."""

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'users'

urlpatterns = [
    # Página de login
    path('login/', LoginView.as_view(template_name = 'users/login.html'), name='login'),
    # Página de logout
    path('logout/', LogoutView.as_view(next_page='learning_logs:index'), name='logout')
]