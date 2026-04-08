from .views import home
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),  # SOLO una raíz

    path('admin/', admin.site.urls),

    # apps
    path('GestionViajes/', include('GestionViajes.urls')),
    path('auth/', include('Authentication.urls')),

    # opcional (si realmente lo usás)
    path('app/', include('MatchViajesApp.urls')),
]
