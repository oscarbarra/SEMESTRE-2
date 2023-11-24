#proyecto final de progra 2 
#hacer una interfas grafica con el comportamiento

from tkinter import Tk, Canvas, PhotoImage, ttk
from random import choice, randint

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

#---------------------------------------------------
#Animales de la simulacion
#---------------------------------------------------
#minimo 10
class Animal(Organismo):
    def __init__(self, imagen, vida, energia, velocidad, posicion,alimentacion, hambre, sed, sexo, movimiento, vision):
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

    def actualizaPosicion(self, fila, columna):
        direcciones = ["arriba", "abajo", "izquierda", "derecha"]
        direccionEscogida = choice(direcciones)

        if direccionEscogida == "arriba":
            if self.posicion[0] - (40 *self.movimiento) -40 >= 0:
                self.posicion[0] -= (40 *self.movimiento) -40

            else:
                self.posicion[0] += (40 *self.movimiento) -40

        if direccionEscogida == "abajo":
            if self.posicion[0] + (40 *self.movimiento) -40 <= fila:
                self.posicion[0] += (40 *self.movimiento) -40

            else:
                self.posicion[0] -= (40 *self.movimiento) -40

        if direccionEscogida == "izquierda":
            if self.posicion[1] - (40 *self.movimiento) -40 >= 0:
                self.posicion[1] -= (40 *self.movimiento) -40

            else:
                self.posicion[1] += (40 *self.movimiento) -40

        if direccionEscogida == "derecha":
            if self.posicion[1] + (40 *self.movimiento) -40 <= columna:
                self.posicion[1] += (40 *self.movimiento) -40

            else:
                self.posicion[1] -= (40 *self.movimiento) -40

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
        self.nombre = "leon"
        self.imagen = PhotoImage(file=f"PROGRAMACION-2\PROYECTO FINAL\{str('imagenes')}\{str('animales')}\{str('leon')}.png")

        #atributos
        self.vida = 2000
        self.energia = 100
        self.velocidad = 2
        self.posicion = [40 *randint(0, 9),40 *randint(0, 9)]
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

#---------------------------------------------------
#Plantas de la simulacion
#---------------------------------------------------
#minimo 5
class Planta(Organismo):
    def __init__(self, imagen, vida, energia, velocidad, posicion):
        super().__init__(vida, energia, velocidad, posicion)

        self.imagen = imagen

    def fotosintesis(self):
        pass

    def reproducirse(self):
        pass

    def morir(self):
        pass

class Zanahoria(Planta):
    def __init__(self):
        self.imagen = None
        self.vida = 100
        self.energia = 100
        self.velocidad = 2
        self.posicion = [randint(0, 9), randint(0, 9)]

        super().__init__(self.imagen, self.vida, self.energia,self.velocidad, self.posicion)

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

#---------------------------------------------------
#Habitats de la simulacion
#---------------------------------------------------
class Habitat:
    def __init__(self):
        #esencia del habitat
        self.color = choice(("#F7E505", "#3CC600", "#FFFFFF"))

        #posicion del habitat
        self.cuadrado = None

        #animal que esta en el habitat
        self.animal = None

        self.imagenPrincipalAnimal = None

        #planta que esta en el habitat
        self.planta = None
        
        self.imagenPrincipalPlanta = None

#---------------------------------------------------
#Ecosistema regulador de la simalucaion
#---------------------------------------------------
class Ecosistema:
    def __init__(self):
        self.fila = 10
        self.columna = 10
        self.habitat = None
        self.mapa = [[ "_" for c in range(self.columna)] for f in range(self.fila)]

    def creaMapa(self):
        for f in range(self.fila):
            for c in range(self.columna):
                self.habitat = Habitat()
                self.mapa[f][c] = self.habitat

    def creaAnimales(self):
        for f in range(self.fila):
            for c in range(self.columna):
                self.mapa[f][c].animal = choice((Leon(), None, None, None, None))

    def actualizaPosicionAnimales(self):
        for f in range(self.fila):
            for c in range(self.columna):
                try:
                    print(self.mapa[f][c].animal.posicion)
                    self.mapa[f][c].animal.actualizaPosicion(f, c)
                    print(self.mapa[f][c].animal.posicion)
                except AttributeError:
                    pass
#---------------------------------------------------
#Interfaz de la simulacion
#---------------------------------------------------
class Interfaz(Ecosistema):
    def __init__(self):
        super().__init__()
        super().creaMapa()

        self.L_CUADRADO = 40

        self.ventana = Tk()
        self.ventana.title("ajedrez")
        self.ventana.geometry(f"{str(self.L_CUADRADO *self.columna)}x{str(self.L_CUADRADO *self.fila +30)}")
        #self.ventana.resizable(0, 0)

        self.interfaz = Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)
        
        super().creaAnimales()

    def __call__(self):
        self.ventana.mainloop()

    def dibujarAnimales(self):
        self.mapa[0][0].animal = Leon()
        self.mapa[0][0].animal.imagen = PhotoImage(file=f"PROGRAMACION-2\PROYECTO FINAL\{str('imagenes')}\{str('animales')}\{str('tigre')}.png")
        for f in range(self.fila):
            for c in range(self.columna):
                try:
                    self.mapa[f][c].imagenPrincipalAnimal = self.interfaz.create_image(self.mapa[f][c].animal.posicion[1] +4, self.mapa[f][c].animal.posicion[0] +4, image = self.mapa[f][c].animal.imagen, anchor="nw")
                except AttributeError:
                    pass
                
    def actualizaImagenesAnimales(self):
        for f in range(self.fila):
            for c in range(self.columna):
                try:
                    self.interfaz.move(self.mapa[f][c].imagenPrincipalAnimal, self.mapa[f][c].animal.posicion[1], self.mapa[f][c].animal.posicion[0])
                except AttributeError:
                    continue

    def dibujarTablero(self):
        #self.interfaz.create_rectangle(x0, y0, x1, y1, fill=)
        for y in range(self.fila):
            for x in range(self.columna):
                self.interfaz.create_rectangle(x *self.L_CUADRADO, y *self.L_CUADRADO, (x +1) *self.L_CUADRADO, (y +1) *self.L_CUADRADO, fill=self.mapa[y][x].color)

        boton = ttk.Button(text="siguiente ciclo", width=66, command= lambda: (self.actualizaPosicionAnimales(), self.actualizaImagenesAnimales()))
        boton.place(x=0, y=402)

interfaz = Interfaz()

interfaz.dibujarTablero()
interfaz.dibujarAnimales()
interfaz()