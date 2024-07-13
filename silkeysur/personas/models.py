from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    # Otros campos según tus necesidades para la entidad Persona
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Trabajador(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    # Otros campos según tus necesidades para la cantidad de Trabajadores
    
    def __str__(self):
        return f"{self.persona.nombre} - {self.cargo}"
    
    class Meta:
        verbose_name_plural = 'trabajadores'

# Create your models here.
