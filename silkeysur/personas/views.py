from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import PersonaForm, TrabajadorForm
from .models import Persona, Trabajador

# Vistas para manejo de Persona y Trabajador
def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listar_personas') # Redirigir a alguna página
    else:
        form = PersonaForm()
    return render(request, 'personas/persona_form.html', {'form': form})

def listar_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/listar_personas.html', {'personas': personas})

def crear_trabajador(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_trabajadores') # Redirigir a alguna página
    else:
        form = TrabajadorForm()
    return render(request, 'personas/trabajador_form.html', {'form': form})

def listar_trabajadores(request):
    trabajadores = Trabajador.objects.all()
    return render(request, 'personas/listar_trabajadores.html', {'trabajadores': trabajadores})

# Vistas para autenticación
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Cambia 'home' por la vista a la que quieres redirigir después del registro
    else:
        form = UserCreationForm()
    return render(request, 'login/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Cambia 'home' por la vista a la que quieres redirigir después del login
    else:
        form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')
    
