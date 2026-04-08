from django.urls import path
from . import views

urlpatterns = [
    path('verViaje/', views.verViaje, name='verViaje'),
    path('cargarViaje/', views.cargarViaje, name='cargarViaje'),
    path('misViajes/', views.misViajes, name='misViajes'),
]
