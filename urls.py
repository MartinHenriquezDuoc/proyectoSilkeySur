# proyectoSilkeysur-master/silkeysur/urls.py

from django.contrib import admin
from django.urls import path, include  # Importa include para incluir URLs de aplicaciones
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personas/', include('personas.urls')),  # Incluye las URLs de la aplicación personas
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    # Puedes añadir más URLs del proyecto aquí si es necesario
]
