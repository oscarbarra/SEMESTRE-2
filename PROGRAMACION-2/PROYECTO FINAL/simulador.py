#proyecto final de progra 2 
#hacer una interfas grafica con el comportamiento

class Organismo:
    def __init__(self, vida, energia, velocidad, posicion):
        self.vida = vida

        # determina la velocidad maxima  // determina la vida de la planta
        self.energia = energia # 0 /1

        # casillas que se mueve cuando 'caza' // determina el crecimiento de la planta
        # movimento *2 *energia 
        self.velocidad = velocidad

        # donde esta en la simulacion
        self.posicion = posicion

#minimo 10
class Animal(Organismo):
    def __init__(self, vida, energia, velocidad, posicion,alimentacion, hambre, sed, sexo, movimiento, vision):
        super().__init__(vida, energia, velocidad, posicion)

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

    def tomar_agua():
        pass

    def comer():
        pass

    def cazar():
        pass

    def huir():
        pass

    def reproducirse():
        pass

    def morir():
        pass

#minimo 5
class Planta(Organismo):
    def __init__(self, vida, energia, velocidad, posicion):
        super().__init__(vida, energia, velocidad, posicion)

    def fotosintesis():
        pass

    def reproducirse():
        pass

#minimo 3
class Ambiente:
    def __init__(self, temperatura):
        self.temepratura = temperatura

    # estados del clima 
    def clima_soleado():
        pass
    
    def clima_calido():
        pass

    def clima_frio():
        pass

    def clima_lluvia():
        pass

    # desastres naturales
    def terremoto():
        pass

    def errupcion_volcanica():
        pass

    def meteorito():
        pass


#gestiona el comportamiento
class Ecosistema:
    def __init__(self):
        pass