class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad 
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, grupo):
        super().__init__(nombre, edad, salario)
        self.grupo = grupo
        self.pos = "Gerente"

    def describir_rol(self):
        print(f"yo como {self.pos} me encargo de que todos los grupos funcionen correctamente")


class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, grupo):
        super().__init__(nombre, edad, salario)
        self.grupo = grupo 
        self.pos = "ingeniero"

    def describir_rol(self):
        print(f"yo como {self.pos} me encargo de realizar los proyectos que aprueba el gerente")

class Asistente(Empleado):
    def __init__(self, nombre, edad, salario, grupo):
        super().__init__(nombre, edad, salario)
        self.grupo = grupo  
        self.pos = "Asistente"

    def describir_rol(self):
        print(f"yo como {self.pos} me encargo de gestionar el dia del gerente")


G1 = Gerente("felipe", 25, 1000000, 0)
I1 = Ingeniero("oscar", 20, 750000, 1)
A1 = Asistente("cony", 40, 600000, 1)

for i in (G1, I1, A1):
    i.describir_rol()
    print("\n")