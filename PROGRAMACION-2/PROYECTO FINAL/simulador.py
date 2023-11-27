#proyecto final de progra 2 
#hacer una interfas grafica con el comportamiento

from tkinter import Tk, Canvas, PhotoImage, ttk
from random import choice, randint

#---------------------------------------------------
#variables globales
#---------------------------------------------------
fila = 10; columna = 20; cuadrado = 40

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
#Animales de la simulacion#minimo 10
#---------------------------------------------------
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

    def actualizaPosicion(self, direccion, planta, contador):
        print(contador)
        if contador == 4:
            return
        
        elif direccion == "arriba":
            if self.posicion[0] -(self.movimiento *cuadrado) >= 0:
                self.posicion[0] = self.posicion[0] -(self.movimiento *cuadrado)
            else:
                self.actualizaPosicion("abajo", planta, contador +1)

        elif direccion == "abajo":
            if self.posicion[0] +(self.movimiento *cuadrado) <= 360:
                self.posicion[0] = self.posicion[0] +(self.movimiento *cuadrado)
            else:
                self.actualizaPosicion("izquierda", planta, contador +1)
        
        elif direccion == "izquierda":
            if self.posicion[1] -(self.movimiento *cuadrado) >= 0:
                self.posicion[1] = self.posicion[1] -(self.movimiento *cuadrado)
            else:
                self.actualizaPosicion("derecha", planta, contador +1)

        elif direccion == "derecha":
            if self.posicion[1] +(self.movimiento *cuadrado) <= 760: 
                self.posicion[1] = self.posicion[1] +(self.movimiento *cuadrado)
            else:
                self.actualizaPosicion("arriba", planta, contador +1)

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
        self.vision= 2
        
        super().__init__(self.imagen, self.vida, self.energia, self.velocidad, self.posicion, self.alimentacion, self.hambre, self.sed, self.sexo, self.movimiento, self.vision)

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
        self.vision = 3

        super().__init__(self.imagen, self.vida, self.energia, self.velocidad, self.posicion, self.alimentacion, self.hambre, self.sed, self.sexo, self.movimiento, self.vision)

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
        self.vision = 3

        super().__init__(self.imagen, self.vida, self.energia, self.velocidad, self.posicion, self.alimentacion, self.hambre, self.sed, self.sexo, self.movimiento, self.vision)

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
        self.vision = 2

       
        super().__init__(self.imagen, self.vida, self.energia, self.velocidad, self.posicion, self.alimentacion, self.hambre, self.sed, self.sexo, self.movimiento, self.vision)

#---------------------------------------------------
#Plantas de la simulacion #minimo 5
#---------------------------------------------------
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
        self.color = choice(("#F7E505", "#61D850", "#FFFFFF"))

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
        self.mapaSecundario = [[ "-" for c in range(columna)] for f in range(fila)]

    def creaMapaPrincipal(self):
        for f in range(fila):
            for c in range(columna):
                self.habitat = Habitat()
                self.mapaPrincipal[f][c] = self.habitat

    def creaPlantas(self):
            for f in range(fila):
                for c in range(columna):
                    planta = choice((Zanahoria([cuadrado*f, cuadrado*c]), FrutoRojo([cuadrado*f, cuadrado*c]), Hierba([cuadrado*f, cuadrado*c]),
                                                                "-", "-", "-", "-", "_", "-", "-", "-", "-", "_", "-", "-", "-", "-", "_", "-", "-", "-", "-", "_"))
                    if self.mapaPrincipal[f][c].planta == "-":
                        self.mapaPrincipal[f][c].planta = planta

    def creaAnimales(self):
        for f in range(fila):
            for c in range(columna):
                if self.mapaPrincipal[f][c].planta == "-":
                    animal = choice((Leon([cuadrado*f, cuadrado*c]), Conejo([cuadrado*f, cuadrado*c]),Tigre([cuadrado*f, cuadrado*c]), Cerdo([cuadrado*f, cuadrado*c]),
                                                            "-", "-", "-", "-", "_", "-", "-", "-", "-", "_", "-", "-", "-", "-", "_", "-", "-", "-", "-", "_"))
                    self.mapaPrincipal[f][c].animal = animal

    def creaMapaSecundario(self):
        for f in range(fila):
            for c in range(columna):
                self.mapaSecundario[f][c] = self.mapaPrincipal[f][c]

    def limpiaMapaSecundario(self):
            self.mapaSecundario = [[ "-" for c in range(columna)] for f in range(fila)]

    def actualizaPosicionAnimales(self):
        for f in range(fila):
            for c in range(columna):
                try:
                    self.mapaPrincipal[f][c].animal.actualizaPosicion(choice(("arriba", "abajo", "izquierda", "derecha")),self.mapaPrincipal[f][c].planta, 0)
                except AttributeError:
                    continue
                
    def cantidadAnimalesPantalla(self):
        contador = 0
        for f in range(fila):
            for c in range(columna):
                try:
                    if self.mapaSecundario[f][c].animal.nombre in ("leon", "tigre", "conejo", "cerdo"):
                        contador +=1
                except AttributeError:
                    continue
        print(contador)

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

    
#---------------------------------------------------
#Interfaz de la simulacion
#---------------------------------------------------
class Interfaz(Ecosistema):
    def __init__(self):
        super().__init__()
        super().creaMapaPrincipal()
        

        self.ventana = Tk()
        self.ventana.title("ajedrez")
        self.ventana.geometry(f"{str(cuadrado *columna)}x{str(cuadrado *fila +30)}")
        #self.ventana.resizable(0, 0)

        self.interfaz = Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)

        super().creaPlantas()
        super().creaAnimales()
        super().creaMapaSecundario()

    def __call__(self):
        self.ventana.mainloop()


    def dibujarPlantas(self):
        for f in range(fila):
            for c in range(columna):
                try:
                    self.mapaSecundario[f][c].imagenPrincipal = self.interfaz.create_image(self.mapaSecundario[f][c].planta.posicion[1] +4, self.mapaSecundario[f][c].planta.posicion[0] +4, image = self.mapaSecundario[f][c].planta.imagen, anchor="nw", tags=f"planta{f}{c}")
                except AttributeError:
                    continue

    def dibujarAnimales(self):
        for f in range(fila):
            for c in range(columna):
                try:
                    self.mapaSecundario[f][c].imagenPrincipalAnimal = self.interfaz.create_image(self.mapaSecundario[f][c].animal.posicion[1] +4, self.mapaSecundario[f][c].animal.posicion[0] +4, image = self.mapaSecundario[f][c].animal.imagen, anchor="nw", tags="animales")
                except AttributeError:
                    continue

    def dibujarTablero(self):
        #self.interfaz.create_rectangle(x0, y0, x1, y1, fill=)
        for y in range(fila):
            for x in range(columna):
                self.interfaz.create_rectangle(x *cuadrado, y *cuadrado, (x +1) *cuadrado, (y +1) *cuadrado, fill=self.mapaPrincipal[y][x].color)

        boton = ttk.Button(text="siguiente ciclo", width=132, command= lambda: (self.actualizaImagenesAnimales()))
        boton.place(x=0, y=402)

    def actualizaImagenesAnimales(self):
        self.interfaz.delete("animales")

        self.actualizaPosicionAnimales()
        self.limpiaMapaSecundario()
        self.creaMapaSecundario()
        self.dibujarAnimales()
        self.cantidadAnimalesPantalla()    

interfaz = Interfaz()
interfaz.dibujarTablero()
interfaz.dibujarPlantas()
interfaz.dibujarAnimales()
interfaz.cantidadAnimalesTotales()
interfaz.cantidadAnimalesPantalla()

interfaz()