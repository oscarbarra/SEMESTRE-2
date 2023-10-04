class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def sonido_Animal(self,animal, sonido):
        print(f"hola soy {self.nombre} el {animal} y mi sonido es {sonido}")

    
class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)


class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)


class Pajaro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)


P1 = Perro("Canela", 3)
G1 = Gato("Copo de nieve", 5)
A1 = Pajaro("Chimuelo", 6)


#todo por herencia
A1.sonido_Animal("Pajaro", "pio pio")
input("")

G1.sonido_Animal("Gato", "miau miau")
input("")

P1.sonido_Animal("Perro", "guau guau")