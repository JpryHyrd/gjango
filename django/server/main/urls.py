from django.urls import path
from .views import index
from .views import contacts

app_name = "main"


urlpatterns = [
    path("", index),
    path("contacts/", contacts),
]