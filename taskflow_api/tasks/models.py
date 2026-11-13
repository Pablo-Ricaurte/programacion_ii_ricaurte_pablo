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

class PlanDietetico(models.Mofrom django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class NominaTrabajo(models.Model):
    nombre_trabajador = models.CharField(max_length=100)
    anio_contrato = models.IntegerField()
    sueldo_asignado = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_trabajador

class Sensei(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    sensei = models.ForeignKey(
            'Sensei', 
            on_delete=models.CASCADE,
            related_name='alumnos')
    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    misiones = models.ManyToManyField('Mision', related_name='alumnos', blank=True)

    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfiles/')
    created_at = models.DateTimeField(auto_now_add=True)

class Mision(models.Model):
    sensei = models.ForeignKey(
            'Sensei',
            on_delete=models.CASCADE,
            related_name='misiones')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True)


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    titulo = models.CharField(max_length=100)
    objetivo = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    estudiante = models.ManyToManyField(Estudiante,
                    through='Participacion')

class Participacion(models.Model):
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE
    )
    actividad = models.ForeignKey(
        Actividad,
        on_delete=models.CASCADE
    )
    rol = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "TODO", "Por hacer"
        IN_PROGRESS = "IN_PROGRESS", "En progreso"
        DONE = "DONE", "Completada"

    # ForeignKey: cada Task pertenece a UN Project.
    # Un Project puede tener MUCHAS Task — relación muchos a uno.
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titledel):
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