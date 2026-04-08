from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', views.logoutUser, name='Logout'),
]
