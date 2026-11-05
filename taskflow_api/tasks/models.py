from django.db import models

# Create your models here.

class Paciente(models.Model):
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    peso_actual = models.DecimalField(max_digits=5, decimal_places=2, help_text="Peso en Kg")
    estatura = models.DecimalField(max_digits=4, decimal_places=2, help_text="Estatura en metros")
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class PlanDietetico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="planes")
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    calorias_diarias = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.paciente.nombre}"

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    motivo = models.CharField(max_length=255)
    completada = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Cita de {self.paciente.nombre} el {self.fecha_hora}"