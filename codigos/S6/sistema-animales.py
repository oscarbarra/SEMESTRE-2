class Animal:
    def __init__(self, nombre, edad, sonido):
        self.nombre = nombre
        self.edad = edad
        self.sonido_animal = sonido

    def sonidoA(self):
        print(f"soy un {self.nombre} tengo {self.edad} anos y mi sonido es {self.sonido_animal}")


class Perro(Animal):
    def __init__(self, nombre, edad, sonido_animal):
        super().__init__(nombre, edad, sonido_animal)


class Gato(Animal):
    def __init__(self, nombre, edad, sonido_animal):
        super().__init__(nombre, edad, sonido_animal)

class Pajaro(Animal):
    def __init__(self, nombre, edad, sonido_animal):
        super().__init__(nombre, edad, sonido_animal)



P1 = Perro("canela", 3, "guau guau")
G1 = Gato("carbon", 5, "miau miau")
PJ1 = Pajaro("rio", 6, "pio pio")

for i in (P1, G1, PJ1):
    i.sonidoA()
    print("\n")