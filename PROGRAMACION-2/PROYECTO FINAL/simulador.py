#proyecto final de progra 2 
#hacer una interfas grafica con el comportamiento

from email.mime import image
import tkinter as tk
from random import choice
from random import randint
from types import NoneType

class Organismo:
    def __init__(self, vida, energia, velocidad, posicion):
        self.vida = vida

        # determina la velocidad maxima  // determina la vida de la planta
        self.energia = energia # 0 /100

        # casillas que se mueve cuando 'caza' // determina el crecimiento de la planta
        # movimento *2 *energia 
        self.velocidad = velocidad

        # donde esta en la simulacion
        self.posicion = posicion

#minimo 10
class Animal(Organismo):
    def __init__(self,imagen, vida, energia, velocidad, posicion,alimentacion, hambre, sed, sexo, movimiento, vision):
        super().__init__(vida, energia, velocidad, posicion)

        self.imagen = imagen

        # determina se es 'carnovoro' 'hervivoro' 'omnivoro'
        self.alimentacion = alimentacion

        # modifica la 'energia del animal'
        self.hambre = hambre # 0 /1

        # modifica la 'energia del animal'
        self.sed = sed #0 /1

        # determina si es 'macho' 'hembra' 
        self.sexo = sexo

        # determina cuantas casillas se mueve por el mapa
        self.movimiento = movimiento

        # determina cuanto puede ver
        self.vision = vision

    def moverse(self, fila, columna):
        direcciones = ["arriba", "abajo", "izquierda", "derecha"]
        direccionEscogida = choice(direcciones)

        print(direccionEscogida)
        if direccionEscogida == "arriba":
            if self.posicion[0] - self.movimiento >= 0:
                self.posicion[0] -= self.movimiento

            else:
                self.posicion[0] += self.movimiento

        if direccionEscogida == "abajo":
            if self.posicion[0] + self.movimiento <= fila:
                self.posicion[0] += self.movimiento

            else:
                self.posicion[0] -= self.movimiento

        if direccionEscogida == "izquierda":
            if self.posicion[1] - self.movimiento >= 0:
                self.posicion[1] -= self.movimiento

            else:
                self.posicion[1] += self.movimiento

        if direccionEscogida == "derecha":
            if self.posicion[1] + self.movimiento <= columna:
                self.posicion[1] += self.movimiento

            else:
                self.posicion[1] -= self.movimiento

    def tomar_agua(self):
        pass

    def comer(self):
        pass

    def reproducirse(self):
        pass

    def morir(self):
        pass

class Leon(Animal):
    def __init__(self):
        self.imagen = "./imagenes/animales/leon"
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

    def cazar(self):
        pass

class Conejo(Animal):
    def __init__(self):
        pass

    def huir(self):
        pass

#minimo 5
class Planta(Organismo):
    def __init__(self, vida, energia, velocidad, posicion):
        super().__init__(vida, energia, velocidad, posicion)

    def fotosintesis(self):
        pass

    def reproducirse(self):
        pass

    def morir(self):
        pass

#minimo 3
class Ambiente:
    def __init__(self, temperatura):
        self.temepratura = temperatura

    # estados del clima 
    def clima_soleado(self):
        pass
    
    def clima_calido(self):
        pass

    def clima_frio(self):
        pass

    def clima_lluvia(self):
        pass

    # desastres naturales
    def terremoto(self):
        pass

    def errupcion_volcanica(self):
        pass

    def meteorito(self):
        pass

class Habitat:
    def __init__(self, posicion):
        #esencia del habitat
        self.color = choice(("#F7E505", "#3CC600", "#FFFFFF"))

        #posicion del habitat
        self.posicion = posicion

        #animal que esta en el habitat
        self.animal = None

        #planta que esta en el habitat
        self.planta = None

#gestiona el comportamiento
class Ecosistema:
    def __init__(self):
        self.fila = 10
        self.columna = 10
        self.habitat = None
        self.mapa = [[ "_" for c in range(self.columna)] for f in range(self.fila)]
        self.animales = None
        self.plantas = None

    def creaMapa(self):
        for f in range(self.fila):
            for c in range(self.columna):
                self.habitat = Habitat([f,c])
                self.mapa[f][c] = self.habitat

    def muestraMapa(self):
        for f in range(self.fila):
            for c in range(self.columna):
                print(self.mapa[f][c].color, end="    ")
            print("\n")

class Interfaz(Ecosistema):
    def __init__(self):
        super().__init__()
        super().creaMapa()
        
        self.L_CUADRADO = 50

        self.ventana = tk.Tk()
        self.ventana.title("ajedrez")
        self.ventana.geometry(f"{str(self.L_CUADRADO *self.columna)}x{str(self.L_CUADRADO *self.fila)}")

        self.interfaz = tk.Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)

    def __call__(self):
        self.ventana.mainloop()

    def dibujarTablero(self):
        #self.interfaz.create_rectangle(x0, y0, x1, y1, fill=)
        for f in range(self.fila):
            for c in range(self.columna):
                self.interfaz.create_rectangle(f *self.L_CUADRADO, c *self.L_CUADRADO, (f +1) *self.L_CUADRADO, (c +1) *self.L_CUADRADO, fill=self.mapa[f][c].color)

    def dibujarOrganismos(self):
        for f in range(self.fila):
            for c in range(self.columna):
                try:
                    self.interfaz.create_image(f, c, image= self.mapa[f][c].animal.imagen)
                
                except AttributeError:
                    pass

interfaz = Interfaz()

interfaz.dibujarTablero()
interfaz.dibujarOrganismos()
interfaz()