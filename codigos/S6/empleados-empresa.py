class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad 
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, trab_pendientes):
        super().__init__(nombre, edad, salario)
        
        #trabajos por revisar
        self.trabajos_pendientes = trab_pendientes

    def describir_rol(self):
        print("me encargo de gestionar y aprobar los trabajos de esta empresa")

    def mostrar_trabajos_pendientes(self):
        print(f"actualmente tengo {self.trabajos_pendientes} trabajos que revisar")


class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, trab_activo):
        super().__init__(nombre, edad, salario)

        #identificador para no alterar el orden de la empresa
        self.trabajo_activo = trab_activo 

    def describir_rol(self):
        print("me encargo de dar solucion a los trabajos aprobados por el gerente")

    def mostrar_trabajos_activos(self):
        print(f"actualmente estoy trabajando en el proyecto {self.trabajo_activo}")


class Asistente(Empleado):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad, salario)

        self.registro_gastos = []

    def describir_rol(self):
        print("principalmente me encargo de crear y actuelizar los informes de gastos")

    def agragar_gastos(self,mes, gasto_mesnsual):
        self.registro_gastos.append([mes, gasto_mesnsual])

    def mostrar_resgistro(self):
        print("gastos de la enpresa")
        for i in self.registro_gastos:
            print(i)
        




#creacion de los objetos
G1 = Gerente("felipe", 25, 1000000, 123)
I1 = Ingeniero("eduardo", 20, 750000, "a1")
A1 = Asistente("florencia", 40, 600000)

print("gerente")
G1.describir_rol()
G1.mostrar_trabajos_pendientes()
input("")

print("ingeniero")
I1.describir_rol()
I1.mostrar_trabajos_activos()
input("")

print("asistente")
A1.describir_rol()
A1.agragar_gastos("enero", 10)
A1.agragar_gastos("febrero", 9)
A1.agragar_gastos("marzo", 8)
A1.mostrar_resgistro()