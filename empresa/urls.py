from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio),
    path("bienvenido/", views.saludar),
    path("otra_url/", views.saludar2),
    path("numero/<int:numero_x>/", views.ver_numero),
    path("saludar/<str:nombre>/", views.saludar),

    path("sumar/<int:a>/<int:b>", views.sumar)
]