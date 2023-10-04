class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Banco:
    def __init__(self):
        self.clientes_activos = []
        self.cuentas_activas = []

    def crear_cuenta(self,cliente, saldo=0):
        if saldo == 0:
            self.cuentas_activas.append([cliente.nombre, saldo])
            self.clientes_activos.append(cliente)
            print(f"{cliente.nombre} has creado tu cuenta con exito y tienes un saldo inicial de 0")

        else:
            self.cuentas_activas.append([cliente.nombre, saldo])
            self.clientes_activos.append([cliente])
            print(f"{cliente.nombre} has creado tu cuenta con exito y tienes un saldo inicial de {saldo}")

    def eliminar_cuenta(self, cliente):
        for i in range(0, len(self.cuentas_activas)):
            if cliente in self.clientes_activos and cliente.nombre == self.cuentas_activas[i][0]:
                self.cuentas_activas.remove(self.cuentas_activas[i])
                self.clientes_activos.remove(cliente)
                print("has eliminado la cuenta con exito")

    def mostrar_cuentas(self):
        print(self.cuentas_activas)
        for clientes in self.clientes_activos:
            print(clientes.nombre)

p1 = Persona("oscar")
p2 = Persona("felipe")

main = Banco()


main.mostrar_cuentas()
main.crear_cuenta(p1)
main.crear_cuenta(p2, 500)
input("")

main.mostrar_cuentas()
input("")

main.eliminar_cuenta(p1)
main.mostrar_cuentas()