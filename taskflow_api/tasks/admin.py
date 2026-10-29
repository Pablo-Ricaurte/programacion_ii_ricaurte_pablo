from django.contrib import admin
from .models import Project, Task
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "nombre_en_mayusculas", "created_at")
    
@admin.register(Task)
class TAskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "due_date")
    list_filter = ("status", "project")
    search_fields = ("title", "description")