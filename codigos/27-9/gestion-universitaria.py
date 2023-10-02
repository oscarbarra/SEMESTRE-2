#haciendo el ultimo ejercicio de la prueba

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

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

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

    def agregar_estudiante(self, new_estudiante):
        tam_grupo = len(self.estudiantes)
        aprobacion = True

        if tam_grupo == 0:
            self.estudiantes.append(new_estudiante)
            print(f"{new_estudiante.nombre} {new_estudiante.apellido} ha sido agregado correctamente al grupo")
        
        else:
            for i in range(0, tam_grupo):
                if new_estudiante.nombre == self.estudiantes[i].nombre and new_estudiante.apellido == self.estudiantes[i].apellido:
                    aprobacion = False

            if aprobacion:
                self.estudiantes.append(new_estudiante)
                print(f"{new_estudiante.nombre} {new_estudiante.apellido} ha sido agregado correctamente al grupo")
        
            else:
                print(f"{new_estudiante.nombre} {new_estudiante.apellido} ya forma parte de este grupo")

            
    def eliminar_estudiante(self, del_estudiante):
        tam_grupo = len(self.estudiantes)
        aprobacion = False

        if tam_grupo == 1:
            self.estudiantes.remove(del_estudiante)
            print(f"{del_estudiante.nombre} {del_estudiante.apellido} ha sido eliminado correctamente del grupo")
        
        else:
            for i in range(0, tam_grupo):
                if del_estudiante.nombre == self.estudiantes[i].nombre and del_estudiante.apellido == self.estudiantes[i].apellido:
                    aprobacion = True

            if aprobacion:
                self.estudiantes.remove(del_estudiante)
                print(f"{del_estudiante.nombre} {del_estudiante.apellido} ha sido eliminado correctamente del grupo")
        
            else:
                print(f"{del_estudiante.nombre} {del_estudiante.apellido} no forma parte del grupo")

    def mostrar_grupo(self):
        if len(self.estudiantes) == 0:
            print(self.estudiantes)

        else:
            for i in range(0, len(self.estudiantes)):
                j = i+1
                if j % 6 == 0:
                    print("\n")
                    print([self.estudiantes[i].nombre + " " + self.estudiantes[i].apellido], end=" ")
                    
                else:
                    print([self.estudiantes[i].nombre + " " + self.estudiantes[i].apellido], end=" ")
        print("\n")

class ProgramaAcademico:
    def __init__(self, nombre, codigo, grupos):
        self.nombre = nombre
        self.codigo = codigo
        self.grupos = grupos #lista obejtos


E1 = Estudiante("oscar", "barra", "17/04/2005", 0, "informatica", 2)
E2 = Estudiante("christian", "lagos", "19/04/2005", 0, "medicina", 1)
E3 = Estudiante("oscar", "jara", "17/04/2005", 0, "informatica", 2)
E4 = Estudiante("christian", "rojas", "19/04/2005", 0, "medicina", 1)
E5 = Estudiante("felipe","ocampo", "17/04/2005", 0, "informatica", 2)
E6 = Estudiante("max", "vañenzuela", "19/04/2005", 0, "medicina", 1)
E7 = Estudiante("max", "nunez", "19/04/2005", 0, "medicina", 1)

G1 = Grupo(0, "programacion 2", "elliot")

G1.mostrar_grupo()
G1.agregar_estudiante(E1)
G1.mostrar_grupo()

G1.agregar_estudiante(E2)
G1.mostrar_grupo()

#G1.eliminar_estudiante(E1)
#G1.mostrar_grupo()

G1.agregar_estudiante(E3)
G1.mostrar_grupo()

G1.agregar_estudiante(E4)
G1.mostrar_grupo()

G1.agregar_estudiante(E5)
G1.mostrar_grupo()

G1.agregar_estudiante(E6)
G1.mostrar_grupo()

G1.agregar_estudiante(E7)
G1.mostrar_grupo()


#G1.eliminar_estudiante(E2)
#G1.mostrar_grupo()

#print(G1.estudiantes)