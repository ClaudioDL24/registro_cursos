from .models import Curso, Profesor, Estudiante, Direccion

def crear_curso(codigo, nombre, version):
    curso, created = Curso.objects.get_or_create(codigo=codigo, defaults={'nombre': nombre, 'version': version})
    return curso

def crear_profesor(rut, nombre, apellido, activo, creado_por):
    profesor = Profesor.objects.create(rut=rut, nombre=nombre, apellido=apellido, activo=activo, creado_por=creado_por)
    return profesor

def crear_estudiante(rut, nombre, apellido, fecha_nac, activo, creado_por):
    estudiante = Estudiante.objects.create(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, activo=activo, creado_por=creado_por)
    return estudiante

def crear_direccion(calle, numero, dpto, comuna, ciudad, region, estudiante):
    direccion = Direccion.objects.create(calle=calle, numero=numero, dpto=dpto, comuna=comuna, ciudad=ciudad, region=region, estudiante=estudiante)
    return direccion

def obtiene_estudiante(rut):
    estudiante = Estudiante.objects.get(rut=rut)
    return estudiante

def obtiene_profesor(rut):
    profesor = Profesor.objects.get(rut=rut)
    return profesor

def obtiene_curso(codigo):
    curso = Curso.objects.get(codigo=codigo)
    return curso

def agrega_profesor_a_curso(profesor, curso):
    curso.profesores.add(profesor)

def agrega_cursos_a_estudiante(estudiante, *cursos):
    estudiante.cursos.add(*cursos)

def imprime_estudiante_cursos(rut):
    estudiante = Estudiante.objects.get(rut=rut)
    cursos_estudiante = estudiante.cursos.all()
    print(f"Cursos del estudiante {estudiante.nombre} {estudiante.apellido}:")
    for curso in cursos_estudiante:
        print(curso.nombre)
