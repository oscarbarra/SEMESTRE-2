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