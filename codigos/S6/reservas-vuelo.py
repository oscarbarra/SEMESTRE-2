class Reserva:
    def __init__(self, nombre, num_vuelo, fecha):
        self.nombre_pasajero = nombre
        self.numero_vuelo = num_vuelo
        self.fecha = fecha


class Reserva_Economica(Reserva):
    def __init__(self, nombre, num_vuelo, fecha, tipo):
        super().__init__(nombre, num_vuelo, fecha)
        self.tipo_vuelo = "Economico"
        self.tipo = tipo
        
    def presentacion(self):
        print(f"hola soy {self.nombre_pasajero} y compre un boleto {self.tipo_vuelo} {self.tipo}")

    def mostrar_detalle(self):
        print(f"soy {self.nombre_pasajero} voy en el vuelo {self.numero_vuelo} y puedo escoger entre plan familiar e individual")


class Reserva_Bisness(Reserva):
    def __init__(self, nombre, num_vuelo, fecha):
        super().__init__(nombre, num_vuelo, fecha)
        self.tipo_vuelo = "Bisness"
        self.entretenimiento = "incluido"

    def presentacion(self):
        print(f"hola soy {self.nombre_pasajero} y compre un boleto tipo {self.tipo_vuelo}")

    def mostrar_detalle(self):
        print(f"soy {self.nombre_pasajero} voy en el vuelo {self.numero_vuelo} y puedo pasar el rato con un entretenimiento {self.entretenimiento}")


class Reserva_Primera_Clase(Reserva):
    def __init__(self, nombre, num_vuelo, fecha):
        super().__init__(nombre, num_vuelo, fecha)
        self.tipo_vuelo = "primera clase"
        self.comidas = "incluido"

    def presentacion(self):
        print(f"hola soy {self.nombre_pasajero} y compre un voleto de {self.tipo_vuelo}")
    
    def mostrar_detalle(self):
        print(F"soy {self.nombre_pasajero} voy en el vuelo {self.numero_vuelo} que tiene la comida {self.comidas}")


P1 = Reserva_Economica("felipe", 1, "01/01/2023", "personal")
P2 = Reserva_Bisness("oscar", 2, "01/01/2023")
P3 = Reserva_Primera_Clase("christian", 3, "01/01/2023")

for i in (P1, P2, P3):
    i.presentacion()
    i.mostrar_detalle()
    print("\n")