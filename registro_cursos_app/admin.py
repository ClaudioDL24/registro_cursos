from django.contrib import admin
from .models import Estudiante, Profesor, Direccion, Curso, CursoProfesor

# Register your models here.

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'fecha_nac', 'activo', 'creacion_registro', 'modificacion_registro', 'creado_por')

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'activo', 'creacion_registro', 'modificacion_registro', 'creado_por')

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('calle', 'numero', 'depto', 'comuna', 'ciudad', 'region', 'estudiante')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'version', 'estudiantes_list')

    def estudiantes_list(self, obj):
        return ", ".join([estudiante.nombre for estudiante in obj.estudiantes.all()])

@admin.register(CursoProfesor)
class CursoProfesorAdmin(admin.ModelAdmin):
    list_display = ('curso', 'profesor')
