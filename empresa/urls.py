from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio),
    path("bienvenido/", views.saludar),
    path("otra_url/", views.saludar2)
]