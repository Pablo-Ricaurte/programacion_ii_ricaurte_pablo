from django.contrib import admin
from .models import Paciente, PlanDietetico, Cita
# Register your models here.

admin.site.register(Paciente)
admin.site.register(PlanDietetico)
admin.site.register(Cita)from django.contrib import admin

# Register your models here.
from .models import Project, NominaTrabajo, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "due_date")
    list_filter = ("status", "project")
    search_fields = ("title", "description")

@admin.register(NominaTrabajo)
class NominaTrabajoAdmin(admin.ModelAdmin):
    list_display = ("nombre_trabajador", "anio_contrato", "sueldo_asignado", "created_at")
    search_fields = ("nombre_trabajador",)