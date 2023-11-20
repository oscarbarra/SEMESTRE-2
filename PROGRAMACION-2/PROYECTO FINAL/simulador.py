#proyecto final de progra 2 
#hacer una interfas grafica con el comportamiento

from random import choice

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

        pass 

    #posiblemente lo borre
    def tomar_agua(self):
        pass

    def comer(self):
        pass

    def reproducirse(self):
        pass

    def morir(self):
        pass

class Leon(Animal):
    def __init__(self, imagen, vida, energia, velocidad, posicion, alimentacion, hambre, sed, sexo, movimiento, vision):
        super().__init__(imagen, vida, energia, velocidad, posicion, alimentacion, hambre, sed, sexo, movimiento, vision)

    def cazar(self):
        pass

class Conejo(Animal):
    def __init__(self, imagen, vida, energia, velocidad, posicion, alimentacion, hambre, sed, sexo, movimiento, vision):
        super().__init__(imagen, vida, energia, velocidad, posicion, alimentacion, hambre, sed, sexo, movimiento, vision)

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
    def __init__(self, color, animal, planta, posicion):
        self.color = color
        self.animal = animal
        self.planta = planta
        self.posicion = posicion

#gestiona el comportamiento
class Ecosistema:
    def __init__(self, animales, plantas):
        self.fila = 10
        self.columna = 10
        self.mapa = []
        self.animales = animales
        self.plantas = plantas

    def muestraMapa(self):
        for f in range(self.fila):
            for c in range(self.columna):
                print(self.mapa[f][c].color, end="   ")
            print("\n")

    def pintaMapa(self):
        for f in range(self.fila):
            self.mapa.append([])
            for c in range(self.columna):
                habiat = Habitat(choice(("amarillo", "verde", "blanco")), "", 0, "")
                self.mapa[f].append(habiat)

    def rellenoMapa(self):
        if len(self.animales) != 0:
            for animal in self.animales:
                self.mapa[animal.posicion[0]][animal.posicion[1]].animal = animal
                self.mapa[animal.posicion[0]][animal.posicion[1]].posicion = animal.posicion

        if len(self.plantas) != 0:
            for planta in self.plantas:
                self.mapa[planta.posicion[0]][planta.posicion[1]].planta = planta
                self.mapa[planta.posicion[0]][planta.posicion[1]].posicion = planta.posicion

#animales de la simulacion
#imagen, vida, energia, velocidad, posicion, alimentacion, hambre, sed, sexo, movimiento, vision 
leon_1 = Leon("L1", 1000, 100, 2, [0, 0], "carnivoro", 100, 100, choice(("macho", "hembra")), 2, 3)
leon_2 = Leon("L2", 1000, 100, 2, [9, 9], "carnivoro", 100, 100, choice(("macho", "hembra")), 2, 3)

ecosistema = Ecosistema([leon_1, leon_2], [])

while True:
    ecosistema.pintaMapa()
    ecosistema.rellenoMapa() 
    ecosistema.muestraMapa()

    ecosistema.animales[0].moverse(ecosistema.fila, ecosistema.columna)
    print(ecosistema.animales[0].posicion)

    fin = int(input("numero: "))
    if fin == 0:
        break