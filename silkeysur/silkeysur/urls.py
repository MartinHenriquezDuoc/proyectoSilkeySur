"""
URL configuration for silkeysur project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from personas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear_persona/', views.crear_persona, name='crear_persona'),
    path('listar_personas/', views.listar_personas, name='listar_personas'),
    path('crear_trabajador/', views.crear_trabajador, name='crear_trabajador'),
    path('listar_trabajadores/', views.listar_trabajadores, name='listar_trabajadores'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('', views.home, name='home'),
    # Define más URLs según tus necesidades
]