#proyecto final de progra 2 
#hacer una interfas grafica con el comportamiento

from tkinter import Tk, Canvas, PhotoImage, ttk
from random import choice, randint

#---------------------------------------------------
#variables globales
#---------------------------------------------------
fila = 10; columna = 20; cuadrado = 40; excluir = ["", ""]

class Organismo:
    def __init__(self, vida, energia, velocidad, posicion):
        self.vida = vida

        # determina los ciclos de apareamiento // determina la vida de la planta
        self.energia = energia # 0 /100        // energia < 50 -> vida -20 cada ciclo

        # casillas que se mueve cuando 'caza' // determina el crecimiento de la planta
        # movimento *2 *energia 
        self.velocidad = velocidad

        # donde esta en la simulacion
        self.posicion = posicion

    def morir(self):
        pass

#---------------------------------------------------
#Animales de la simulacion #minimo 10
#---------------------------------------------------
class Animal(Organismo):
    def __init__(self, imagen, vida, energia, velocidad, posicion,alimentacion, hambre, sed, sexo, movimiento, vision):
        super().__init__(vida, energia, velocidad, posicion)

        self.imagen = imagen

        # determina se es 'carnovoro' 'hervivoro' 'omnivoro'
        self.alimentacion = alimentacion

        # modifica la 'vida del animal'
        self.hambre = hambre # 0 /1

        # modifica la 'vida del animal'
        self.sed = sed #0 /1

        # determina si es 'macho' o 'hembra' 
        self.sexo = sexo

        # determina cuantas casillas se mueve por el mapa
        self.movimiento = movimiento

        # determina cuanto puede ver
        self.vision = vision

    def cambiaPosicion(self, direccion, raiz, contador, excluir):
        if self.posicion[0] == excluir[0] and self.posicion[1] == excluir[1]:
            return

        if contador < 4:
            if direccion == "arriba":
                if self.posicion[0] -(self.movimiento *cuadrado) >= 0:
                    if raiz[int((self.posicion[0] -(self.movimiento *cuadrado)) /cuadrado)][int(self.posicion[1] /cuadrado)].animal == "-" and raiz[int((self.posicion[0] -(self.movimiento *cuadrado)) /cuadrado)][int(self.posicion[1] /cuadrado)].planta == "-":
                        raiz[int(self.posicion[0] /cuadrado)][int(self.posicion[1] /cuadrado)].animal, raiz[int((self.posicion[0] -(self.movimiento *cuadrado)) /cuadrado)][int(self.posicion[1] /cuadrado)].animal = raiz[int((self.posicion[0] -(self.movimiento *cuadrado)) /cuadrado)][int(self.posicion[1] /cuadrado)].animal, raiz[int(self.posicion[0] /cuadrado)][int(self.posicion[1] /cuadrado)].animal
                else:
                        self.cambiaPosicion("abajo", raiz, contador +1, excluir)

            if direccion == "abajo":
                if self.posicion[0] +(self.movimiento *cuadrado) <= fila*cuadrado -40:
                    if raiz[int((self.posicion[0] +(self.movimiento *cuadrado)) /cuadrado)][int(self.posicion[1] /cuadrado)].animal == "-" and raiz[int((self.posicion[0] +(self.movimiento *cuadrado)) /cuadrado)][int(self.posicion[1] /cuadrado)].planta == "-":
                        raiz[int(self.posicion[0] /cuadrado)][int(self.posicion[1] /cuadrado)].animal, raiz[int((self.posicion[0] +(self.movimiento *cuadrado)) /cuadrado)][int(self.posicion[1] /cuadrado)].animal = raiz[int((self.posicion[0] +(self.movimiento *cuadrado)) /cuadrado)][int(self.posicion[1] /cuadrado)].animal, raiz[int(self.posicion[0] /cuadrado)][int(self.posicion[1] /cuadrado)].animal
                else:
                        self.cambiaPosicion("izquierda", raiz, contador +1, excluir)
                
            if direccion == "izquierda":
                if self.posicion[1] -(self.movimiento *cuadrado) >= 0:
                    if raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] -(self.movimiento *cuadrado)) /cuadrado)].animal == "-" and raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] -(self.movimiento *cuadrado)) /cuadrado)].planta == "-":
                        raiz[int(self.posicion[0] /cuadrado)][int(self.posicion[1] /cuadrado)].animal, raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] -(self.movimiento *cuadrado)) /cuadrado)].animal = raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] -(self.movimiento *cuadrado)) /cuadrado)].animal, raiz[int(self.posicion[0] /cuadrado)][int(self.posicion[1] /cuadrado)].animal
                else:
                        self.cambiaPosicion("derecha", raiz, contador +1, excluir)

            if direccion == "derecha":
                if self.posicion[1] +(self.movimiento *cuadrado) <= columna*cuadrado -40:
                    if raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] +(self.movimiento *cuadrado)) /cuadrado)].animal == "-" and raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] +(self.movimiento *cuadrado)) /cuadrado)].planta == "-": 
                        raiz[int(self.posicion[0] /cuadrado)][int(self.posicion[1] /cuadrado)].animal, raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] +(self.movimiento *cuadrado)) /cuadrado)].animal = raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] +(self.movimiento *cuadrado)) /cuadrado)].animal, raiz[int(self.posicion[0] /cuadrado)][int(self.posicion[1] /cuadrado)].animal
                else:
                        self.cambiaPosicion("arriba", raiz, contador +1, excluir)
    
    def creaHijo(self, direccion, raiz, contador, raza):
        if contador < 4:
            if direccion == "arriba":
                if self.posicion[0] - cuadrado >= 0: #revisa que este viendo dentro del mapa
                    if raiz[int((self.posicion[0] - cuadrado) /cuadrado)][int(self.posicion[1] /cuadrado)].animal == "-" and raiz[int((self.posicion[0] - cuadrado) /cuadrado)][int(self.posicion[1] /cuadrado)].planta == "-": #revisa que no exista un animal o planta
                        raiz[int((self.posicion[0] - cuadrado) /cuadrado)][int(self.posicion[1] /cuadrado)].animal = raza
                        raiz[int((self.posicion[0] - cuadrado) /cuadrado)][int(self.posicion[1] /cuadrado)].animal.posicion = [self.posicion[0], self.posicion[1]]
                    else:
                        self.creaHijo("abajo", raiz, contador +1, raza)
                else:
                    self.creaHijo("abajo", raiz, contador +1, raza)

            if direccion == "abajo":
                if self.posicion[0] + cuadrado <= fila*cuadrado -cuadrado: #revisa que este viendo dentro del mapa
                    if raiz[int((self.posicion[0] + cuadrado) /cuadrado)][int(self.posicion[1] /cuadrado)].animal == "-" and raiz[int((self.posicion[0] + cuadrado) /cuadrado)][int(self.posicion[1] /cuadrado)].planta  == "-": #revisa que no exista un animal o planta
                        raiz[int((self.posicion[0] + cuadrado) /cuadrado)][int(self.posicion[1] /cuadrado)].animal = raza
                        raiz[int((self.posicion[0] + cuadrado) /cuadrado)][int(self.posicion[1] /cuadrado)].animal.posicion = [self.posicion[0] + cuadrado, self.posicion[1]]
                    else:
                        self.creaHijo("izquierda", raiz, contador +1, raza)
                else:
                    self.creaHijo("izquierda", raiz, contador +1, raza)

            if direccion == "izquierda":
                if self.posicion[1] - cuadrado >= 0: #revisa que este viendo dentro del mapa
                    if raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] -cuadrado) /cuadrado)].animal == "-" and raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] - cuadrado) /cuadrado)].planta == "-": #revisa que no exista un animal o planta
                        raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] -cuadrado) /cuadrado)].animal = raza
                        raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] -cuadrado) /cuadrado)].animal.posicion = [self.posicion[0], self.posicion[1] -cuadrado]
                    else:
                        self.creaHijo("derecha", raiz, contador +1, raza)
                else:
                    self.creaHijo("derecha", raiz, contador +1, raza)

            if direccion == "derecha":
                if self.posicion[1] + cuadrado <= columna*cuadrado -cuadrado : #revisa que este viendo dentro del mapa
                    if raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] +cuadrado) /cuadrado)].animal == "-" and raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] + cuadrado) /cuadrado)].planta == "-": #revisa que no exista un animal o planta
                        raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] +cuadrado) /cuadrado)].animal = raza
                        raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] +cuadrado) /cuadrado)].animal.posicion = [self.posicion[0], self.posicion[1] +cuadrado]
                    else:
                        self.creaHijo("arriba", raiz, contador +1, raza)
                else:
                    self.creaHijo("arriba", raiz, contador +1, raza)

    def reproduccion(self, direccion, raiz):
        global excluir

        if direccion == "arriba":
            if self.posicion[0] - self.vision*cuadrado >= 0: #revisa que este viendo dentro del mapa
                if raiz[int((self.posicion[0] - self.vision*cuadrado) /cuadrado)][int(self.posicion[1] /cuadrado)].animal != "-": #revisa que exista un animal e la casilla
                    if raiz[int((self.posicion[0] - self.vision*cuadrado) /cuadrado)][int(self.posicion[1] /cuadrado)].animal.nombre == self.nombre: #revisa que los animales sean de la misma raza
                        if raiz[int((self.posicion[0] - self.vision*cuadrado) /cuadrado)][int(self.posicion[1] /cuadrado)].animal.sexo != self.sexo: #revisa que los animales sean de sexo opuesto
                            excluir = [self.posicion[0] - self.vision*cuadrado, self.posicion[1]]
                            self.cambiaPosicion("arriba", raiz, 0, excluir)
                            return 1

        if direccion == "abajo":
            if self.posicion[0] + self.vision*cuadrado <= fila*cuadrado -40: #revisa que este viendo dentro del mapa
                if raiz[int((self.posicion[0] +self.vision*cuadrado) /cuadrado)][int(self.posicion[1] /cuadrado)].animal != "-": #revisa que exista un animal e la casilla
                    if raiz[int((self.posicion[0] + self.vision*cuadrado) /cuadrado)][int(self.posicion[1] /cuadrado)].animal.nombre == self.nombre: #revisa que los animales sean de la misma raza
                        if raiz[int((self.posicion[0] + self.vision*cuadrado) /cuadrado)][int(self.posicion[1] /cuadrado)].animal.sexo != self.sexo: #revisa que los animales sean de sexo opuesto
                            excluir = [self.posicion[0] + self.vision*cuadrado, self.posicion[1]]
                            self.cambiaPosicion("abajo", raiz, 0, excluir)
                            return 1
                            

        if direccion == "izquierda":
            if self.posicion[1] - self.vision*cuadrado >= 0: #revisa que este viendo dentro del mapa
                if raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] - self.vision*cuadrado) /cuadrado)].animal != "-": #revisa que exista un animal e la casilla
                    if raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] - self.vision*cuadrado) /cuadrado)].animal.nombre == self.nombre: #revisa que los animales sean de la misma raza
                        if raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] - self.vision*cuadrado) /cuadrado)].animal.sexo != self.sexo: #revisa que los animales sean de sexo opuesto
                            excluir = [self.posicion[0], self.posicion[1] - self.vision*cuadrado]
                            self.cambiaPosicion("izquierda", raiz, 0, excluir)
                            return 1
                            
                
        if direccion == "derecha":
            if self.posicion[1] + self.vision*cuadrado <= columna*cuadrado -40: #revisa que este viendo dentro del mapa
                if raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] + self.vision*cuadrado) /cuadrado)].animal != "-": #revisa que exista un animal e la casilla
                    if raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] + self.vision*cuadrado) /cuadrado)].animal.nombre == self.nombre: #revisa que los animales sean de la misma raza
                        if raiz[int(self.posicion[0] /cuadrado)][int((self.posicion[1] + self.vision*cuadrado) /cuadrado)].animal.sexo != self.sexo: #revisa que los animales sean de sexo opuesto
                            excluir = [self.posicion[0], self.posicion[1] + self.vision*cuadrado]
                            self.cambiaPosicion("derecha", raiz, 0, excluir)
                            return 1

class Leon(Animal):
    def __init__(self, posicion):
        self.nombre = "leon"
        self.imagen = PhotoImage(file=f"PROGRAMACION-2\PROYECTO FINAL\{str('imagenes')}\{str('animales')}\{str('leon')}.png")

        #atributos
        self.vida = 2000
        self.energia = 100
        self.velocidad = 2
        self.posicion = posicion
        self.alimentacion = "carnivoro"
        self.hambre = 100
        self.sed = 100
        self.sexo = choice(("macho", "hembra"))
        self.movimiento = 2
        self.vision= 3
        
        super().__init__(self.imagen, self.vida, self.energia, self.velocidad, self.posicion,
                          self.alimentacion, self.hambre, self.sed, self.sexo, self.movimiento, self.vision)

    def cazar(self):
        pass

class Tigre(Animal):
    def __init__(self, posicion):
        self.nombre = "tigre"
        self.imagen = PhotoImage(file=f"PROGRAMACION-2\PROYECTO FINAL\{str('imagenes')}\{str('animales')}\{str('tigre')}.png")

        self.vida = 2250
        self.energia = 100
        self.velocidad = 2
        self.posicion = posicion
        self.alimentacion = "carnivoro"
        self.hambre = 100
        self.sed = 100
        self.sexo = choice(("macho", "hembra"))
        self.movimiento = 2
        self.vision = 3
       
        super().__init__(self.imagen, self.vida, self.energia, self.velocidad, self.posicion, self.alimentacion, self.hambre, self.sed, self.sexo, self.movimiento, self.vision)

    def cazar(self):
        pass

class Lobo(Animal):
    def __init__(self, posicion):
        self.nombre = "lobo"
        self.imagen = PhotoImage(file=f"PROGRAMACION-2\PROYECTO FINAL\{str('imagenes')}\{str('animales')}\{str('lobo')}.png")

        self.vida = 1800
        self.energia = 100
        self.velocidad = 2
        self.posicion = posicion
        self.alimentacion = "carnivoro"
        self.hambre = 100
        self.sed = 100
        self.sexo = choice(("macho", "hembra"))
        self.movimiento = 2
        self.vision = 3

        super().__init__(self.imagen, self.vida, self.energia, self.velocidad, self.posicion, self.alimentacion,
                          self.hambre, self.sed, self.sexo, self.movimiento, self.vision)

    def cazar(self):
        pass

class OsoPolar(Animal):
    def __init__(self, posicion):
        self.nombre = "osoPolar"
        self.imagen = PhotoImage(file=f"PROGRAMACION-2\PROYECTO FINAL\{str('imagenes')}\{str('animales')}\{str('osoPolar')}.png")

        self.vida = 3000
        self.energia = 100
        self.velocidad = 2
        self.posicion = posicion
        self.alimentacion = "carnivoro"
        self.hambre = 100
        self.sed = 100
        self.sexo = choice(("macho", "hembra"))
        self.movimiento = 2
        self.vision = 3

        super().__init__(self.imagen, self.vida, self.energia, self.velocidad, self.posicion, self.alimentacion, self.hambre, self.sed, self.sexo, self.movimiento, self.vision)

    def cazar(self):
        pass

class Zorro(Animal):
    def __init__(self, posicion):
        self.nombre = "zorro"
        self.imagen = PhotoImage(file=f"PROGRAMACION-2\PROYECTO FINAL\{str('imagenes')}\{str('animales')}\{str('zorro')}.png")

        self.vida = 1600
        self.energia = 100
        self.velocidad = 2
        self.posicion = posicion
        self.alimentacion = "carnivoro"
        self.hambre = 100
        self.sed = 100
        self.sexo = choice(("macho", "hembra"))
        self.movimiento = 2
        self.vision = 3

        super().__init__(self.imagen, self.vida, self.energia, self.velocidad, self.posicion, self.alimentacion, self.hambre, self.sed, self.sexo, self.movimiento, self.vision)

    def cazar(self):
        pass

class Conejo(Animal):
    def __init__(self, posicion):
        self.nombre = "conejo"
        self.imagen = PhotoImage(file=f"PROGRAMACION-2\PROYECTO FINAL\{str('imagenes')}\{str('animales')}\{str('conejo')}.png")

        self.vida = 750
        self.energia = 100
        self.velocidad = 2
        self.posicion = posicion
        self.alimentacion = "herbivoro"
        self.hambre = 100
        self.sed = 100
        self.sexo = choice(("macho", "hembra"))
        self.movimiento = 1
        self.vision = 2

        super().__init__(self.imagen, self.vida, self.energia, self.velocidad, self.posicion, self.alimentacion,
                          self.hambre, self.sed, self.sexo, self.movimiento, self.vision)

    def huir(self):
        pass

class Cerdo(Animal):
    def __init__(self, posicion):
        self.nombre = "cerdo"
        self.imagen = PhotoImage(file=f"PROGRAMACION-2\PROYECTO FINAL\{str('imagenes')}\{str('animales')}\{str('cerdo')}.png")

        self.vida = 1250
        self.energia = 100
        self.velocidad = 2
        self.posicion = posicion
        self.alimentacion = "herbivoro"
        self.hambre = 100
        self.sed = 100
        self.sexo = choice(("macho", "hembra"))
        self.movimiento = 1
        self.vision = 2

        super().__init__(self.imagen, self.vida, self.energia, self.velocidad, self.posicion, self.alimentacion, self.hambre, self.sed, self.sexo, self.movimiento, self.vision)

    def huir(self):
        pass

class Cebra(Animal):
    def __init__(self, posicion):
        self.nombre = "cebra"
        self.imagen = PhotoImage(file=f"PROGRAMACION-2\PROYECTO FINAL\{str('imagenes')}\{str('animales')}\{str('cebra')}.png")

        self.vida = 1500
        self.energia = 100
        self.velocidad = 2
        self.posicion = posicion
        self.alimentacion = "herbivoro"
        self.hambre = 100
        self.sed = 100
        self.sexo = choice(("macho", "hembra"))
        self.movimiento = 1
        self.vision = 2

        super().__init__(self.imagen, self.vida, self.energia, self.velocidad, self.posicion, self.alimentacion, self.hambre, self.sed, self.sexo, self.movimiento, self.vision)

    def huir(self):
        pass

class Raton(Animal):
    def __init__(self, posicion):
        self.nombre = "raton"
        self.imagen = PhotoImage(file=f"PROGRAMACION-2\PROYECTO FINAL\{str('imagenes')}\{str('animales')}\{str('raton')}.png")

        self.vida = 500
        self.energia = 100
        self.velocidad = 2
        self.posicion = posicion
        self.alimentacion = "herbivoro"
        self.hambre = 100
        self.sed = 100
        self.sexo = choice(("macho", "hembra"))
        self.movimiento = 1
        self.vision = 2

        super().__init__(self.imagen, self.vida, self.energia, self.velocidad, self.posicion, self.alimentacion, self.hambre, self.sed, self.sexo, self.movimiento, self.vision)

    def huir(self):
        pass

class Vaca(Animal):
    def __init__(self, posicion):
        self.nombre = "cerdo"
        self.imagen = PhotoImage(file=f"PROGRAMACION-2\PROYECTO FINAL\{str('imagenes')}\{str('animales')}\{str('cerdo')}.png")

        self.vida = 1300
        self.energia = 100
        self.velocidad = 2
        self.posicion = posicion
        self.alimentacion = "herbivoro"
        self.hambre = 100
        self.sed = 100
        self.sexo = choice(("macho", "hembra"))
        self.movimiento = 1
        self.vision = 2

        super().__init__(self.imagen, self.vida, self.energia, self.velocidad, self.posicion, self.alimentacion, self.hambre, self.sed, self.sexo, self.movimiento, self.vision)

    def huir(self):
        pass

#---------------------------------------------------
#Plantas de la simulacion #minimo 5
#---------------------------------------------------
class Planta(Organismo):
    def __init__(self, imagen, vida, energia, velocidad, posicion):
        super().__init__(vida, energia, velocidad, posicion)

        self.imagen = imagen

    def fotosintesis(self):
        pass

class Zanahoria(Planta):
    def __init__(self, posicion):
        self.imagen = PhotoImage(file=f"PROGRAMACION-2\PROYECTO FINAL\{'imagenes'}\{'plantas'}\{'zanahoria'}.png")
        self.vida = 100
        self.energia = 100
        self.velocidad = 2
        self.posicion = posicion

        super().__init__(self.imagen, self.vida, self.energia,self.velocidad, self.posicion)

class FrutoRojo(Planta):
    def __init__(self, posicion):
        self.imagen = PhotoImage(file=f"PROGRAMACION-2\PROYECTO FINAL\{'imagenes'}\{'plantas'}\{'frutoRojo'}.png")
        self.vida = 100
        self.energia = 100
        self.velocidad = 2
        self.posicion = posicion

        super().__init__(self.imagen, self.vida, self.energia,self.velocidad, self.posicion)

class Hierba(Planta):
    def __init__(self, posicion):
        self.imagen = PhotoImage(file=f"PROGRAMACION-2\PROYECTO FINAL\{'imagenes'}\{'plantas'}\{'hierba'}.png")
        self.vida = 100
        self.energia = 100
        self.velocidad = 2
        self.posicion = posicion

        super().__init__(self.imagen, self.vida, self.energia,self.velocidad, self.posicion)

#------------------------------------------
#Ambientes de la simulacion
#------------------------------------------
class Ambiente:
    def __init__(self, temperatura):
        self.temepratura = temperatura

    # desastres naturales
    def terremoto(self):
        pass

    def errupcion_volcanica(self):
        pass

    def meteorito(self):
        pass

class Soleado(Ambiente):
    def __init__(self):
        super().__init__(randint(25, 40))

class Lluvia(Ambiente):
    def __init__(self):
        super().__init__(randint(10, 25))

class Frio(Ambiente):
    def __init__(self):
        super().__init__(randint(-10, 10))

#---------------------------------------------------
#Habitats de la simulacion
#---------------------------------------------------
class Habitat:
    def __init__(self):
        #esencia del habitat
        self.color = choice(("#F7E505", "#61D850", "#FFFFFF"))

        self.ambiente = "-"

        #animal que esta en el habitat
        self.animal = "-"

        self.imagenPrincipalAnimal = "-"

        #planta que esta en el habitat
        self.planta = "-"
        
        self.imagenPrincipalPlanta = "-"
    
    def cambioDeDia(self):
        self.animal.energia -= 10
        self.animal.hambre -= 20
        self.animal.sed -= 20

        if self.animal.hambre <= 50 or self.animal.sed <= 50:
            self.animal.vida -=20

class Desierto(Habitat):
    def __init__(self):
        #esencia del habitat
        self.color = "#F7E505"

        self.ambiente = Soleado()

        #animal que esta en el habitat
        self.animal = "-"

        self.imagenPrincipalAnimal = "-"

        #planta que esta en el habitat
        self.planta = "-"
        
        self.imagenPrincipalPlanta = "-"

class Bosque(Habitat):
    def __init__(self):
        #esencia del habitat
        self.color = "#61D850"

        self.ambiente = Lluvia()

        #animal que esta en el habitat
        self.animal = "-"

        self.imagenPrincipalAnimal = "-"

        #planta que esta en el habitat
        self.planta = "-"
        
        self.imagenPrincipalPlanta = "-"

class Antartida(Habitat):
    def __init__(self):
        #esencia del habitat
        self.color = "#FFFFFF"

        self.ambiente = Frio()

        #animal que esta en el habitat
        self.animal = "-"

        self.imagenPrincipalAnimal = "-"

        #planta que esta en el habitat
        self.planta = "-"
        
        self.imagenPrincipalPlanta = "-"
#---------------------------------------------------
#Ecosistema regulador de la simalucaion
#---------------------------------------------------
class Ecosistema:
    def __init__(self):
        self.habitat = None
        self.mapaPrincipal = [[ "-" for c in range(columna)] for f in range(fila)]

    def creaMapaPrincipal(self):
        for f in range(fila):
            for c in range(columna):
                self.habitat = choice((Desierto(), Bosque(), Antartida()))
                self.mapaPrincipal[f][c] = self.habitat

    def creaPlantas(self):
            for f in range(fila):
                for c in range(columna):
                    planta = choice((Zanahoria([cuadrado*f, cuadrado*c]), FrutoRojo([cuadrado*f, cuadrado*c]), Hierba([cuadrado*f, cuadrado*c]),
                                                                "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
                                                                  "-", "-", "-", "-", "-", "-"))
                    if self.mapaPrincipal[f][c].planta == "-":
                        self.mapaPrincipal[f][c].planta = planta

    def creaAnimales(self):
        for f in range(fila):
            for c in range(columna):
                if self.mapaPrincipal[f][c].planta == "-":
                    animal = choice((Leon([cuadrado*f, cuadrado*c]), Tigre([cuadrado*f, cuadrado*c]), Lobo([cuadrado*f, cuadrado*c]),
                                      OsoPolar([cuadrado*f, cuadrado*c]), Zorro([cuadrado*f, cuadrado*c]),
                                      Conejo([cuadrado*f, cuadrado*c]), Cerdo([cuadrado*f, cuadrado*c]),
                                      Cebra([cuadrado*f, cuadrado*c]), Raton([cuadrado*f, cuadrado*c]), Vaca([cuadrado*f, cuadrado*c]),
                                      "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
                                        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"))
                    
                    self.mapaPrincipal[f][c].animal = animal

    def cambiaPosicionAnimales(self):
        for f in range(fila):
            for c in range(columna):
                if self.mapaPrincipal[f][c].animal != "-":
                    self.mapaPrincipal[f][c].animal.cambiaPosicion(choice(("arriba", "abajo", "izquierda", "derecha")), self.mapaPrincipal, 0, excluir)

    def cantidadAnimalesTotales(self):
        contador = 0
        for f in range(fila):
            for c in range(columna):
                try:
                    if self.mapaPrincipal[f][c].animal.nombre in ("leon", "tigre", "conejo", "cerdo"):
                        contador +=1
                except AttributeError:
                    continue
        print(contador)

    def cicloDeVida(self):
        for f in range(fila):
            for c in range(columna):
                if self.mapaPrincipal[f][c].animal != "-":
                    print(self.mapaPrincipal[f][c].animal.nombre)
                    self.mapaPrincipal[f][c].cambioDeDia()

                    if self.mapaPrincipal[f][c].animal.vida <= 0:
                        self.mapaPrincipal[f][c].animal = "-"

                    #elif self.mapaPrincipal[f][c].animal.energia >= 70:
                        #print(self.mapaPrincipal[f][c].animal.nombre)
                        #if self.mapaPrincipal[f][c].animal.reproduccion(choice(("arriba", "abajo", "izquierda", "derecha")), self.mapaPrincipal) == 1:
                        
                            
                            #print(self.mapaPrincipal[f][c].animal.nombre)
                            #if self.mapaPrincipal[f][c].animal.nombre == "leon":
                                #self.mapaPrincipal[f][c].animal.creaHijo(choice(("arriba", "abajo", "izquierda", "derecha")), self.mapaPrincipal, 0, Leon("-"))

                            #elif self.mapaPrincipal[f][c].animal.nombre == "lobo":
                               #self.mapaPrincipal[f][c].animal.creaHijo(choice(("arriba", "abajo", "izquierda", "derecha")), self.mapaPrincipal, 0, Lobo("-"))
                            
                            #elif self.mapaPrincipal[f][c].animal.nombre == "osoPolar":
                                #self.mapaPrincipal[f][c].animal.creaHijo(choice(("arriba", "abajo", "izquierda", "derecha")), self.mapaPrincipal, 0, OsoPolar("-"))
                            
                            #elif self.mapaPrincipal[f][c].animal.nombre == "tigre":
                                #self.mapaPrincipal[f][c].animal.creaHijo(choice(("arriba", "abajo", "izquierda", "derecha")), self.mapaPrincipal, 0, Tigre("-"))
                            
                            #elif self.mapaPrincipal[f][c].animal.nombre == "zorro":
                                #self.mapaPrincipal[f][c].animal.creaHijo(choice(("arriba", "abajo", "izquierda", "derecha")), self.mapaPrincipal, 0, Zorro("-"))
                            
                            #elif self.mapaPrincipal[f][c].animal.nombre == "cebra":
                                #self.mapaPrincipal[f][c].animal.creaHijo(choice(("arriba", "abajo", "izquierda", "derecha")), self.mapaPrincipal, 0, Cebra("-"))
                            
                            #elif self.mapaPrincipal[f][c].animal.nombre == "raton":
                                #self.mapaPrincipal[f][c].animal.creaHijo(choice(("arriba", "abajo", "izquierda", "derecha")), self.mapaPrincipal, 0, Raton("-"))
                            
                            #elif self.mapaPrincipal[f][c].animal.nombre == "vaca":
                                #self.mapaPrincipal[f][c].animal.creaHijo(choice(("arriba", "abajo", "izquierda", "derecha")), self.mapaPrincipal, 0, Vaca("-"))
                            
                            #elif self.mapaPrincipal[f][c].animal.nombre == "cerdo":
                                #self.mapaPrincipal[f][c].animal.creaHijo(choice(("arriba", "abajo", "izquierda", "derecha")), self.mapaPrincipal, 0, Cerdo("-"))
                            
                            #else:
                                #self.mapaPrincipal[f][c].animal.creaHijo(choice(("arriba", "abajo", "izquierda", "derecha")), self.mapaPrincipal, 0, Conejo("-"))

                    #elif self.mapaPrincipal[f][c].animal.hambre <= 60:
                        #if self.mapaPrincipal[f][c].animal.alimentacion == "carnivoro":
                            #self.mapaPrincipal[f][c].animal.cazar()
                        #else:
                            #self.mapaPrincipal[f][c].animal.huir()
                    else:
                        self.cambiaPosicionAnimales()  
#---------------------------------------------------
#Interfaz de la simulacion
#---------------------------------------------------
class Interfaz(Ecosistema):
    def __init__(self):
        super().__init__()
        super().creaMapaPrincipal()
        

        self.ventana = Tk()
        self.ventana.title("ajedrez")
        self.ventana.geometry(f"{str(cuadrado *columna +440)}x{str(cuadrado *fila +3)}")
        #self.ventana.resizable(0, 0)

        self.interfaz = Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)

        super().creaPlantas()
        super().creaAnimales()

    def __call__(self):
        self.ventana.mainloop()


    def dibujarPlantas(self):
        for f in range(fila):
            for c in range(columna):
                if self.mapaPrincipal[f][c].planta != "-":
                    self.mapaPrincipal[f][c].imagenPrincipalPlanta = self.interfaz.create_image(c*cuadrado +4, f*cuadrado  +4,
                                                                                                 image = self.mapaPrincipal[f][c].planta.imagen, anchor="nw")

    def dibujarAnimales(self):
        for f in range(fila):
            for c in range(columna):
                if self.mapaPrincipal[f][c].animal != "-":
                    self.mapaPrincipal[f][c].imagenPrincipalAnimal = self.interfaz.create_image(c*cuadrado +4, f*cuadrado +4,
                                                                                                 image = self.mapaPrincipal[f][c].animal.imagen, anchor="nw", tags="animales")
                    self.mapaPrincipal[f][c].animal.posicion = [f*cuadrado, c*cuadrado]

    def dibujarTablero(self):
        #self.interfaz.create_rectangle(x0, y0, x1, y1, fill=)
        for y in range(fila):
            for x in range(columna):
                self.interfaz.create_rectangle(x *cuadrado, y *cuadrado, (x +1) *cuadrado, (y +1) *cuadrado, fill=self.mapaPrincipal[y][x].color)

        entrada = ttk.Entry(width=50)
        entrada.place(x=columna*cuadrado +75, y= 10)

        boton1 = ttk.Button(text="enviar comando", width=25)
        boton1.place(x=columna*cuadrado +150, y=40)

        boton2 = ttk.Button(text="siguiente ciclo", width=70, command= lambda: (self.actualizaMapaPrincipal()))
        boton2.place(x=columna*cuadrado +2, y=fila*cuadrado -25)

    def actualizaMapaPrincipal(self):
        self.interfaz.delete("animales")

        self.cicloDeVida()
        self.dibujarAnimales()
        self.cantidadAnimalesTotales()    

interfaz = Interfaz()
interfaz.dibujarTablero()
interfaz.dibujarPlantas()
interfaz.dibujarAnimales()
#interfaz.cantidadAnimalesTotales()

interfaz()