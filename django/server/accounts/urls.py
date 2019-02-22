from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (
    login_view, registration_view,
)


app_name = 'accounts'

urlpatterns = [
    path('', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('registration', registration_view, name='registration'),
]

