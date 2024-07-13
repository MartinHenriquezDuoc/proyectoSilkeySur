from django import forms
from .models import Persona, Trabajador

class PersonaForm(forms.ModelForm):
    class meta:
        model = Persona
        fields = ['nombre', 'apellido', 'edad']
        
class TrabajadorForm(forms.ModelForm):
    class meta:
        model = Trabajador
        fields = ['persona', 'cargo', 'salario']