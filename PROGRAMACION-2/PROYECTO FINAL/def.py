from tkinter import PhotoImage


def rellenoMapa(self):
        if len(self.animales) != 0:
            for animal in self.animales:
                self.mapa[animal.posicion[0]][animal.posicion[1]].animal = animal
                self.mapa[animal.posicion[0]][animal.posicion[1]].posicion = animal.posicion

        if len(self.plantas) != 0:
            for planta in self.plantas:
                self.mapa[planta.posicion[0]][planta.posicion[1]].planta = planta
                self.mapa[planta.posicion[0]][planta.posicion[1]].posicion = planta.posicion

class hola:
     def __init__(self):
          self.hola = "hola"

class persona(hola):
     def __init__(self):
          super().__init__()
          self.nombre = "oscar"

     def saludar(self):
          print(self.hola + " " + self.nombre)

p1 = persona()
p1.saludar()

class Leon(Animal):
    def __init__(self):
        self.nombre = "leon"
        self.imagen = PhotoImage(file=f"PROGRAMACION-2\PROYECTO FINAL\{str('imagenes')}\{str('animales')}\{str('leon')}.png")

        #atributos
        self.vida = 2000
        self.energia = 100
        self.velocidad = 2
        self.posicion = [randint(0, 9), randint(0, 9)]
        self.alimentacion = "carnivoro"
        self.hambre = 100
        self.sed = 100
        self.sexo = choice(("macho", "hembra"))
        self.movimiento = 2
        self.vision= 2
        
        super().__init__(self.imagen, self.vida, self.energia, self.velocidad, self.posicion, self.alimentacion, self.hambre, self.sed, self.sexo, self.movimiento, self.vision)
