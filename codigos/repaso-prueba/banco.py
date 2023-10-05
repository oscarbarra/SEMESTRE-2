class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Banco:
    def __init__(self):
        #almacena un id y el nombre de la persona/cliente
        self.clientes_activos = []
        #almacena el nombre y el saldo del cliente
        self.cuentas_activas = []

    #creacion de las cuentas
    def crear_cuenta(self,cliente, saldo=0):
        if saldo == 0:
            self.cuentas_activas.append([cliente.nombre, saldo])
            self.clientes_activos.append(cliente)
            print(f"{cliente.nombre} has creado tu cuenta con exito y tienes un saldo inicial de 0")

        else:
            self.cuentas_activas.append([cliente.nombre, saldo])
            self.clientes_activos.append(cliente)
            print(f"{cliente.nombre} has creado tu cuenta con exito y tienes un saldo inicial de {saldo}")

    #eliminacion de las cuentas
    def eliminar_cuenta(self, cliente):
        for i in range(0, len(self.cuentas_activas)):
            if cliente in self.clientes_activos and cliente.nombre == self.cuentas_activas[i][0]:
                self.cuentas_activas.remove(self.cuentas_activas[i])
                self.clientes_activos.remove(cliente)
                print(f"has eliminado del cliente {cliente.nombre}")

    #agrega saldo a la cuenta del banco
    def agragar_saldo(self):
        pass

    #sacar saldo a la cuenta del banco
    def sacar_saldo(self):
        pass

    #muestra las cuentas que estan en "self.cuentas_activas"
    def mostrar_cuentas(self):
        print(self.cuentas_activas)

    #muestra los clientes que estan en "self.clientes_activos"
    def mostrar_clientes(self):
        indice = 0
        for cliente in self.clientes_activos:
            indice +=1
            print(f"cliente {indice}: {cliente.nombre}")

p1 = Persona("oscar")
p2 = Persona("felipe")

main = Banco()

print("cuentas iniciales")
main.mostrar_cuentas()
input("")

print("creacion de las cuentas")
main.crear_cuenta(p1)
main.crear_cuenta(p2, 500)
input("")

print("muestra las cuentas activas")
main.mostrar_cuentas()
input("")

print("muestra los clientes activos")
main.mostrar_clientes()
input("")

print("eleminacion de las cuentas")
main.eliminar_cuenta(p1)
main.mostrar_cuentas()
input("")

print("eleminacion de las cuentas")
main.eliminar_cuenta(p2)
main.mostrar_cuentas()