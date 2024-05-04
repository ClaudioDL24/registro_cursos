from django.db import models

# Create your models here.

class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    depto = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f"{self.calle}, {self.numero}, {self.comuna}, {self.ciudad}, {self.region}"
    
class CursoProfesor(models.Model):
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('curso', 'profesor')

class Curso(models.Model):
    codigo = models.CharField(max_length=10, unique=True, primary_key=True)
    nombre = models.CharField(max_length=50)
    version = models.IntegerField()
    profesores = models.ManyToManyField(Profesor, through='CursoProfesor')
    estudiantes = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nombre


    


    