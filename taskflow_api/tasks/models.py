from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="nombre del proyecto")
    description = models.TextField(blank=True, verbose_name="descripcion del proyecto")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacioj")
    
    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.name
    
    @property
    def nombre_en_mayusculas(self):
        return self.name.upper()

class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "TODO", "Por hacer"
        IN_PROGRESS = "IN_PROGRESS", "En progreso"
        DONE = "DONE", "Completada"
    
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title