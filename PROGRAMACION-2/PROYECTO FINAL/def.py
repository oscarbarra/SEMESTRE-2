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


        if self.posicion[0] != excluir[0] and self.posicion[1] != excluir[1]:
            if contador < 4:
                if direccion == "arriba":
                    if self.posicion[0] -(self.movimiento *cuadrado) >= 0:
                        if raiz[int((self.posicion[0] -(self.movimiento *cuadrado)) /cuadrado)][int(self.posicion[1] /cuadrado)].animal == "-" and raiz[int((self.posicion[0] -(self.movimiento *cuadrado)) /cuadrado)][int(self.posicion[1] /cuadrado)].planta == "-":
                            raiz[int(self.posicion[0] /cuadrado)][int(self.posicion[1] /cuadrado)].animal, raiz[int((self.posicion[0] -(self.movimiento *cuadrado)) /cuadrado)][int(self.posicion[1] /cuadrado)].animal = raiz[int((self.posicion[0] -(self.movimiento *cuadrado)) /cuadrado)][int(self.posicion[1] /cuadrado)].animal, raiz[int(self.posicion[0] /cuadrado)][int(self.posicion[1] /cuadrado)].animal
                        else:
                            self.cambiaPosicion("abajo", raiz, contador +1, excluir)
                    else:
                            self.cambiaPosicion("abajo", raiz, contador +1, excluir)

                if direccion == "abajo":
                    if self.posicion[0] +(self.movimiento *cuadrado) <= fila*cuadrado -40:
                        if raiz[int((self.posicion[0] +(self.movimiento *cuadrado)) /cuadrado)][int(self.posicion[1] /cuadrado)].animal == "-" and raiz[int((self.posicion[0] +(self.movimiento *cuadrado)) /cuadrado)][int(self.posicion[1] /cuadrado)].planta == "-":
                            raiz[int(self.posicion[0] /cuadrado)][int(self.posicion[1] /cuadrado)].animal, raiz[int((self.posicion[0] +(self.movimiento *cuadrado)) /cuadrado)][int(self.posicion[1] /cuadrado)].animal = raiz[int((self.posicion[0] +(self.movimiento *cuadrado)) /cuadrado)][int(self.posicion[1] /cuadrado)].animal, raiz[int(self.posicion[0] /cuadrado)][int(self.posicion[1] /cuadrado)].animal
                        else:
                            self.cambiaPosicion("izquierda", raiz, contador +1, excluir)
                    else:
                            self.cambiaPosicion("izquierda", raiz, contador +1, excluir)
                
                if direccion == "izquierda":
                    if self.posicion[1] -(self.movimiento *cuadrado) >= 0:
                        if raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] -(self.movimiento *cuadrado)) /cuadrado)].animal == "-" and raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] -(self.movimiento *cuadrado)) /cuadrado)].planta == "-":
                            raiz[int(self.posicion[0] /cuadrado)][int(self.posicion[1] /cuadrado)].animal, raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] -(self.movimiento *cuadrado)) /cuadrado)].animal = raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] -(self.movimiento *cuadrado)) /cuadrado)].animal, raiz[int(self.posicion[0] /cuadrado)][int(self.posicion[1] /cuadrado)].animal

                        else:
                            self.cambiaPosicion("derecha", raiz, contador +1, excluir)
                    else:
                            self.cambiaPosicion("derecha", raiz, contador +1, excluir)

                if direccion == "derecha":
                    if self.posicion[1] +(self.movimiento *cuadrado) <= columna*cuadrado -40:
                        if raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] +(self.movimiento *cuadrado)) /cuadrado)].animal == "-" and raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] +(self.movimiento *cuadrado)) /cuadrado)].planta == "-": 
                            raiz[int(self.posicion[0] /cuadrado)][int(self.posicion[1] /cuadrado)].animal, raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] +(self.movimiento *cuadrado)) /cuadrado)].animal = raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] +(self.movimiento *cuadrado)) /cuadrado)].animal, raiz[int(self.posicion[0] /cuadrado)][int(self.posicion[1] /cuadrado)].animal
                        else:
                            self.cambiaPosicion("arriba", raiz, contador +1, excluir)
                    else:
                            self.cambiaPosicion("arriba", raiz, contador +1, excluir)