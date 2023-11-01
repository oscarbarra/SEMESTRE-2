class Reserva:
    def __init__(self, nombre, num_vuelo, fecha):
        self.nombre_pasajero = nombre
        self.numero_vuelo = num_vuelo
        self.fecha = fecha


class Reserva_Economica(Reserva):
    def __init__(self, nombre, fecha):
        super().__init__(nombre, 1, fecha)
        self.tipo_vuelo = "Economico"
        self.horas_de_vuelo = "16h"
 
    def mostrar_detalle(self):
        print(f"nombre: {self.nombre_pasajero}, vuelo: {self.numero_vuelo} {self.tipo_vuelo}, fecha: {self.fecha}")

    def descripcion_vuelo(self):
        print(f"soy el vuelo que más tarde en llegar a destino, tardando {self.horas_de_vuelo} en aterrizar")

class Reserva_Bisness(Reserva):
    def __init__(self, nombre, fecha):
        super().__init__(nombre, 2, fecha)
        self.tipo_vuelo = "Bisness"
        self.horas_de_vuelo = "10h"
 
    def mostrar_detalle(self):
        print(f"nombre: {self.nombre_pasajero}, vuelo: {self.numero_vuelo} {self.tipo_vuelo}, fecha: {self.fecha}")

    def descripcion_vuelo(self):
        print(f"soy el vuelo que se encuentra en el promedio de los otros, tardando {self.horas_de_vuelo} en aterrizar")

class Reserva_Primera_Clase(Reserva):
    def __init__(self, nombre, fecha):
        super().__init__(nombre, 2, fecha)
        self.tipo_vuelo = "primera clase"
        self.horas_de_vuelo = "4h"

    def mostrar_detalle(self):
        print(f"nombre: {self.nombre_pasajero}, vuelo: {self.numero_vuelo} {self.tipo_vuelo}, fecha: {self.fecha}")

    def descripcion_vuelo(self):
        print(f"soy el vuelo que menos tarde en llegar a destino, tardando {self.horas_de_vuelo} en aterrizar")

E1 = Reserva_Economica("felipe","01/01/2023")
E2 = Reserva_Economica("eduardo", "02/10/2023")

B1 = Reserva_Bisness("oscar", "01/01/2023")
B2 = Reserva_Bisness("cristhofer", "03/10/2023")

P1 = Reserva_Primera_Clase("christian", "01/01/2023")
P2 = Reserva_Primera_Clase("esteban", "03/10/2023")

print("reserva economica")
E1.descripcion_vuelo()
print("\ndetalles del vuelo reservado")
E1.mostrar_detalle()
input("")


print("reserva bisness")
B1.descripcion_vuelo()
print("\ndetalles del vuelo reservado")
B1.mostrar_detalle()
input("")

print("reserva de primera clase")
P1.descripcion_vuelo()
print("\ndetalles del vuelo reservado")
P1.mostrar_detalle()
input("")