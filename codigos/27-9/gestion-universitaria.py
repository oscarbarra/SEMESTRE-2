#haciendo el ultimo ejercicio de la prueba
import random

class Persona:
    def __init__(self, nombre, apellido, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento

    def presentarse(self):
        print(f"hola soy {self.nombre} {self.apellido} y nací en {self.fecha_nacimiento}")

class Estudiante(Persona):
    def __init__(self,nombre, apellido, fecha_nacimiento, matricula, carrera, semestre):
        self.matricula = matricula
        self.carrera = carrera
        self.semestre = semestre
        super().__init__(nombre, apellido, fecha_nacimiento)

    def estudiar(self, materia, horas_estudio):
        print(f"{self.nombre} ha estado estudiando {materia} por {horas_estudio}hrs")

    def presentarse(self):
        print(f"hola soy {self.nombre} {self.apellido} naci el {self.fecha_nacimiento}\ny voy en el semestre {self.semestre} de {self.carrera}")

    def __repr__(self):
        return self.nombre, self.apellido

class Profesor(Persona):
    def __init__(self,nombre, apellido, fecha_nacimiento, numero_empleado, departamento):
        self.numero_empleado = numero_empleado
        self.departamento = departamento
        super().__init__(nombre, apellido, fecha_nacimiento)
    def enseñar(self, materia):
        print(f"el profesor {self.nombre} esta enseñando {materia}")
    
    def presentarse(self):
        print(f"hola soy el profesor {self.nombre}, formo parte del departamento de {self.departamento} y voy a estar todo el semestre con ustedes")

class Asignatura:
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos

    def mostrar_informacion(self):
        print(f"id: {self.codigo} nombre: {self.nombre} creditos_max: {self.creditos}")
 
class Grupo:
    def __init__(self, numero_grupo, asignatura, profesor):
        self.numero_grupo = numero_grupo 
        self.asignatura = asignatura #objeto
        self.profesor = profesor #objeto
        self.estudiantes = [] #lista objetos

    def agregar_estudiante(self, estudiante):
        tam_grupo = len(self.estudiantes)
        aprobacion = False

        for i in range(0, tam_grupo):
            for j in range(0, tam_grupo):
                if True:
                    pass

            
    def eliminar_estudiante(self):
        pass

    def mostrar_grupo(self):
        print(self.estudiantes)

class ProgramaAcademico:
    def __init__(self, nombre, codigo, grupos):
        self.nombre = nombre
        self.codigo = codigo
        self.grupos = grupos #lista obejtos


E1 = Estudiante("oscar", "barra", "17/04/2005", 0, "informatica", 2)
#E2 = Estudiante("oscar", "barra", "17/04/2005", 0, "informatica", 2)

G1 = Grupo(0, "programacion 2", "elliot")
G1.mostrar_grupo()
G1.agregar_estudiante(E1)
#G1.agregar_estudiante(E2)
G1.mostrar_grupo()
