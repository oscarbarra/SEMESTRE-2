class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad 
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, grupo, años_trabajos):
        super().__init__(nombre, edad, salario)
        self.grupo = grupo #grupo al que perteneco
        self.pos = "Gerente" #posicion de trabajo en la empresa
        self.años_trabajados = años_trabajos

    def presentacion(self):
        print(f"hola soy {self.nombre} y en la empresa he trabajado {self.años_trabajados} anos")

    def describir_rol(self):
        print(f"yo como {self.pos} me encargo de que todos los grupos funcionen correctamente")


class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, grupo, tipo):
        super().__init__(nombre, edad, salario)
        self.grupo = grupo 
        self.pos = "ingeniero"
        self.tipo = tipo

    def presentacion(self):
        print(f"hola soy {self.nombre} y trabajo como {self.pos} {self.tipo}")

    def describir_rol(self):
        print(f"yo como {self.pos} me encargo de realizar los proyectos que aprueba el gerente")

class Asistente(Empleado):
    def __init__(self, nombre, edad, salario, grupo, dias_trabajo):
        super().__init__(nombre, edad, salario)
        self.grupo = grupo  
        self.pos = "Asistente"
        self.dias_trabajo = dias_trabajo

    def presentacion(self):
        print(f"hola soy {self.nombre} y trabajo de {self.dias_trabajo}")

    def describir_rol(self):
        print(f"yo como {self.pos} me encargo de gestionar el dia del gerente")


G1 = Gerente("felipe", 25, 1000000, 0, 15)
I1 = Ingeniero("oscar", 20, 750000, 1, "civil informatico")
A1 = Asistente("florencia", 40, 600000, 1, "lunes/miercoles")

for i in (G1, I1, A1):
    i.presentacion()
    i.describir_rol()
    print("\n")