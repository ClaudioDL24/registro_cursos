
from django.contrib import admin
from .models import Estudiante, Direccion, Curso, Profesor

# Register your models here.
@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'fecha_nac', 'activo', 'creacion_registro', 'modificacion_registro', 'creado_por')
    list_filter = ('activo',)
    search_fields = ('nombre', 'apellido', 'rut')

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('calle', 'numero', 'dpto', 'comuna', 'ciudad', 'region', 'estudiante')
    search_fields = ('calle', 'comuna', 'ciudad', 'region')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'version')
    search_fields = ('nombre', 'codigo')

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'activo', 'creacion_registro', 'modificacion_registro', 'creado_por')
    list_filter = ('activo',)
    search_fields = ('nombre', 'apellido', 'rut')