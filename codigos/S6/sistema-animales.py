class Animal:
    def __init__(self, nombre, edad, sonido):
        self.nombre = nombre
        self.edad = edad
        self.sonido_animal = sonido

    def sonidoA(self):
        print(f"soy {self.nombre} y mi sonido es {self.sonido_animal}")

    
class Perro(Animal):
    def __init__(self, nombre, edad, sonido_animal, raza):
        super().__init__(nombre, edad, sonido_animal)
        self.raza = raza 

    def caracteristicas(self):
        print(f"hola soy {self.nombre} y soy de la raza {self.raza}")


class Gato(Animal):
    def __init__(self, nombre, edad, sonido_animal, color):
        super().__init__(nombre, edad, sonido_animal)
        self.color = color

    def caracteristicas(self):
        print(f"hola soy {self.nombre} y soy de color {self.color}")


class Pajaro(Animal):
    def __init__(self, nombre, edad, sonido_animal, exotico):
        super().__init__(nombre, edad, sonido_animal)
        self.exotico = exotico 

    def caracteristicas(self):
        print(f"hola soy {self.nombre} y vengo {self.exotico}")


P1 = Perro("canela", 3, "guau guau", "pastor aleman")
G1 = Gato("carbon", 5, "miau miau", "negro")
PJ1 = Pajaro("rio", 6, "pio pio", "directo desde brasil")

for i in (P1, G1, PJ1):
    i.caracteristicas()
    i.sonidoA()
    print("\n")