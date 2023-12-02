from tkinter import PhotoImage, Tk, Canvas
from random import choice

fila = 10
columna  = 10
alto = 40
ancho = 40

#---------------------------------------------------------------------
#---ANIMALES---
#---------------------------------------------------------------------

class Animal():
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

class Leon(Animal):
    def __init__(self):
        super().__init__("leon", 1250, 100)
        self.imagen = PhotoImage(file=f"PERSONAL\PROYECTO FINAL\{'IMAMENES'}\{'ANIMAL'}\{'leon'}.png")

class Conejo(Animal):
    def __init__(self):
        super().__init__("conejo", 500, 30)
        self.imagen = PhotoImage(file=f"PERSONAL\PROYECTO FINAL\{'IMAMENES'}\{'ANIMAL'}\{'conejo'}.png")

#---------------------------------------------------------------------
#---PLANTAS---
#---------------------------------------------------------------------

class Zanahoria():
    def __init__(self):
        self.imagen = PhotoImage(file=f"PERSONAL\PROYECTO FINAL\{'IMAMENES'}\{'PLANTA'}\{'zanahoria'}.png")

#---------------------------------------------------------------------
#---HABITATS---
#---------------------------------------------------------------------

class Habitat():
    def __init__(self, habitat, color="", animal="", planta=""):
        self.estado = "disponible"
        self.color = color
        self.habitat = habitat
        self.animal = animal
        self.planta = planta

class Desierto(Habitat):
    def __init__(self):
        super().__init__("desierto", "#F7E505")

class Bosque(Habitat):
    def __init__(self):
        super().__init__("bosque", "#61D850")

class Nieve(Habitat):
    def __init__(self):
        super().__init__("nieve", "#FFFFFF")

#---------------------------------------------------------------------
#---ECOSISTEMA---
#---------------------------------------------------------------------

class Ecosistema():
    def __init__(self):
        self.mapa_pincipal = [["" for c in range(columna)] for f in range(fila)]
    
    def Crea_Habitat(self):
        for f in range(fila):
            for c in range(columna):
                self.mapa_pincipal[f][c] = choice((Desierto(), Bosque(), Nieve()))

    def Crea_animal(self):
        for f in range(fila):
            for c in range(columna):
                if self.mapa_pincipal[f][c].estado == "disponible":
                    self.mapa_pincipal[f][c].animal = choice((Leon(), Conejo(), "", "", "", "","", "", "", ""))
                    self.mapa_pincipal[f][c].estado = "no disponible"

    def Crea_planta(self):
        for f in range(fila):
            for c in range(columna):
                if self.mapa_pincipal[f][c].estado == "disponible":
                    self.mapa_pincipal[f][c].planta = choice((Zanahoria(), "", "", "", "","", "", "", "", "", ""))
                    self.mapa_pincipal[f][c].estado = "no disponible"

#---------------------------------------------------------------------
#---INTERFAZ---
#---------------------------------------------------------------------
class Interfaz():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry(f"{fila*alto}x{columna*ancho}")

        self.ecosistema = Ecosistema()
        self.ecosistema.Crea_Habitat()
        self.ecosistema.Crea_animal()
        self.ecosistema.Crea_planta()

        self.mapa = Canvas(self.ventana)
        self.mapa.pack(fill="both", expand=True)

    def Pinta_Mapa(self):
        for f in range(fila):
            for c in range(columna):
                self.mapa.create_rectangle(ancho*c, alto*f, ancho*(c+1), alto*(f+1), fill=self.ecosistema.mapa_pincipal[f][c].color)

    def Pinta_Animal(self):
        for f in range(fila):
            for c in range(columna):
                if self.ecosistema.mapa_pincipal[f][c].animal != "":
                    self.mapa.create_image(ancho*c +4, alto*f +4, image=self.ecosistema.mapa_pincipal[f][c].animal.imagen, anchor="nw", tags="animales")

    def __call__(self):
        self.ventana.mainloop()


interfaz = Interfaz()
interfaz.Pinta_Mapa()
interfaz.Pinta_Animal()
interfaz()